import os
import shutil
from pathlib import Path
from unittest import TestCase

import tensorflow as tf

from core.internal.tensorflow.tensorflow_model_manager import TensorflowModelManager
from core.tests.test_internal.test_tensorflow.example_tensorflow_classes import (
    ExampleBatchGenerator,
    ExampleTensorflowModel,
    ExampleTrainableBlock,
)


class TestTensorflowModelManager(TestCase):

    # TODO(Mike): tests are interdependent here, don't really know how to separate some of them

    def __init__(self, methodName="runTest"):
        super().__init__(methodName=methodName)
        self.savePath = "./tensorflow_tests"
        self.outputSize = 1
        self.exampleTrainableBlock = ExampleTrainableBlock(requiredOutputSize=self.outputSize)
        self.trainingBatchGenerator = ExampleBatchGenerator(returnValue=5)
        self.evaluationBatchGenerator = ExampleBatchGenerator(returnValue=15)

    def setUp(self) -> None:
        self.exampleTrainableModel = ExampleTensorflowModel(exampleBlock=self.exampleTrainableBlock)
        self.exampleModelManager = TensorflowModelManager(
            model=self.exampleTrainableModel,
            optimizer=tf.keras.optimizers.Adam(learning_rate=1),
            trainingBatchGenerator=self.trainingBatchGenerator,
            evaluationBatchGenerator=self.evaluationBatchGenerator,
            projectPath=f"{self.savePath}/trainable",
        )

    def tearDown(self):
        super().tearDown()
        shutil.rmtree(self.savePath)

    def test_initialise(self):
        self.assertIsNone(self.exampleModelManager.trainingSummaryWriter)
        self.assertIsNone(self.exampleModelManager.evaluationSummaryWriter)
        self.exampleModelManager.initialise()
        self.assertIsNotNone(self.exampleModelManager.trainingSummaryWriter)
        self.assertIsNotNone(self.exampleModelManager.evaluationSummaryWriter)

    def test_train_step(self):
        self.exampleModelManager.initialise()
        loss = self.exampleModelManager.train_step(withTracing=True)
        self.assertIsNotNone(loss)
        self.assertNotEqual(loss.numpy(), 0)

    def test_gradients_applied_in_train(self):
        self.exampleModelManager.initialise()
        self.exampleModelManager.train_step(withTracing=False)
        weights1 = self.exampleModelManager.model.exampleBlock.exampleDenseLayer.weights[
            0
        ].numpy()  # need numpy call here, otherwise pointer returned
        self.exampleModelManager.train_step(withTracing=False)
        weights2 = self.exampleModelManager.model.exampleBlock.exampleDenseLayer.weights[0].numpy()
        self.assertFalse((weights1 == weights2).all())

    def test_evaluate(self):
        self.exampleModelManager.initialise()
        loss = self.exampleModelManager.evaluation_step(withTracing=True)
        self.assertIsNotNone(loss)
        self.assertNotEqual(loss.numpy(), 0)

    def test_gradients_not_applied_in_evaluation(self):
        self.exampleModelManager.initialise()
        self.exampleModelManager.evaluation_step(withTracing=False)
        weights1 = self.exampleModelManager.model.exampleBlock.exampleDenseLayer.weights[
            0
        ].numpy()  # need numpy call here, otherwise pointed returned
        self.exampleModelManager.evaluation_step(withTracing=False)
        weights2 = self.exampleModelManager.model.exampleBlock.exampleDenseLayer.weights[0].numpy()
        self.assertTrue((weights1 == weights2).all())

    def test_save_model(self):
        self.exampleModelManager.initialise()
        self.exampleModelManager.train_step(withTracing=True)
        modelSaveDirectory = Path(
            self.exampleModelManager.modelSavePath,
            self.exampleModelManager.model.modelName,
            str(self.exampleModelManager.globalStep),
        )
        self.exampleModelManager.save_model()
        self.assertTrue(os.path.exists(modelSaveDirectory))
        self.assertTrue(os.path.exists(f"{modelSaveDirectory}/assets"))
        self.assertTrue(os.path.exists(f"{modelSaveDirectory}/variables"))
        self.assertTrue(os.path.exists(f"{modelSaveDirectory}/{self.exampleTrainableBlock.blockName}.json"))
        self.assertTrue(os.path.exists(f"{modelSaveDirectory}/saved_model.pb"))
        self.assertTrue(os.path.exists(f"{modelSaveDirectory}/{self.exampleModelManager.model.modelName}.h5"))
