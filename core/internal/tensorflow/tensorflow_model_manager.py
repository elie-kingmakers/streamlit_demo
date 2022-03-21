import json
from datetime import datetime
from pathlib import Path
from typing import List, Union
from uuid import uuid4

import tensorflow as tf
from tqdm.auto import tqdm

from core.internal.batch_generator_base import BatchGeneratorBase
from core.internal.tensorflow.tensorflow_model_base import TensorflowModelBase


class TensorflowModelManager:
    def __init__(
        self,
        model: TensorflowModelBase,
        optimizer: tf.keras.optimizers.Optimizer,
        trainingBatchGenerator: BatchGeneratorBase,
        evaluationBatchGenerator: BatchGeneratorBase,
        projectPath: Union[Path, str],
    ):
        self.model = model
        self.optimizer = optimizer
        self.trainingBatchGenerator = trainingBatchGenerator
        self.evaluationBatchGenerator = evaluationBatchGenerator
        self.projectPath = projectPath

        self.dateMade = datetime.now().date()
        self.uuid = str(uuid4())[:4]
        self.globalStep = 0
        self.trainingSummaryWriter = None
        self.evaluationSummaryWriter = None
        tf.get_logger().setLevel("ERROR")

    @property
    def modelSavePath(self) -> str:
        return f'{self.projectPath}/{self.dateMade.strftime("%Y%m%d")}/{self.uuid}/model'

    @property
    def evaluationSavePath(self) -> str:
        return f'{self.projectPath}/{self.dateMade.strftime("%Y%m%d")}/{self.uuid}/predictions'

    @property
    def tensorboardPath(self) -> str:
        return f'{self.projectPath}/{self.dateMade.strftime("%Y%m%d")}/{self.uuid}/tensorboard'

    def initialise(self) -> None:
        Path(self.tensorboardPath, self.model.modelName).mkdir(parents=True, exist_ok=True)
        self.trainingSummaryWriter = tf.summary.create_file_writer(
            logdir=str(Path(self.tensorboardPath, self.model.modelName, "train"))
        )
        self.evaluationSummaryWriter = tf.summary.create_file_writer(
            logdir=str(Path(self.tensorboardPath, self.model.modelName, "evaluate"))
        )

    def save_model(self) -> None:
        modelDirectory = Path(self.modelSavePath, self.model.modelName, str(self.globalStep))
        modelDirectory.mkdir(parents=True, exist_ok=False)
        tf.saved_model.save(self.model, export_dir=str(modelDirectory), signatures={"output": self.model.get_outputs})
        for modelBlock in self.model.get_model_blocks():
            with open(f"{modelDirectory}/{modelBlock.blockName}.json", "w") as blockSaveFile:
                json.dump(modelBlock.get_config(), blockSaveFile)
        self.model.save_weights(filepath=f"{modelDirectory}/{self.model.modelName}.h5", save_format="h5")

    def train_step(self, withTracing) -> tf.Tensor:
        inputs, targets = next(self.trainingBatchGenerator)
        if withTracing:
            tf.summary.trace_on(graph=True, profiler=False)

        with tf.GradientTape() as tape:
            loss = self.model.get_loss(targets=targets, training=True, **inputs)
        grads = tape.gradient(loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(grads, self.model.trainable_variables))

        with self.trainingSummaryWriter.as_default():  # pylint: disable=not-context-manager
            tf.summary.scalar(name="Loss", data=loss, step=self.globalStep)
            if withTracing:
                tf.summary.trace_export(
                    name=f"{self.model.modelName}{self.globalStep}",
                    step=self.globalStep,
                    profiler_outdir=str(Path(self.tensorboardPath, self.model.modelName, "trainGraph")),
                )
        self.globalStep += 1
        return loss

    def evaluation_step(self, withTracing) -> tf.Tensor:
        inputs, targets = next(self.evaluationBatchGenerator)
        if withTracing:
            tf.summary.trace_on(graph=True, profiler=False)
        loss = self.model.get_loss(targets=targets, training=False, **inputs)
        with self.evaluationSummaryWriter.as_default():  # pylint: disable=not-context-manager
            tf.summary.scalar(name="Loss", data=loss, step=self.globalStep)
            self.model.produce_metrics(targets=targets, training=False, globalStep=self.globalStep, **inputs)
            if withTracing:
                tf.summary.trace_export(
                    name=f"{self.model.modelName}{self.globalStep}",
                    step=self.globalStep,
                    profiler_outdir=str(Path(self.tensorboardPath, self.model.modelName, "evaluateGraph")),
                )
        return loss

    def run(self, stepCount: int, evaluationSteps: List[int], tracingSteps: List[int]) -> None:
        self.initialise()
        for step in tqdm(range(stepCount)):
            if step in evaluationSteps:
                self.save_model()
                self.evaluation_step(withTracing=step in tracingSteps)
            self.train_step(withTracing=step in tracingSteps)
        self.save_model()
