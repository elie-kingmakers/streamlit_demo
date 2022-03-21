# pylint: disable=arguments-differ,abstract-method,unused-argument
import tensorflow as tf

from core.internal.tensorflow.blocks.tensorflow_block_base import TensorflowBlockBase
from core.internal.tensorflow.tensorflow_model_base import TensorflowModelBase


class BasicExampleBlock(TensorflowBlockBase):
    def __init__(self, callReturnValue=20):
        super().__init__()
        self.callReturnValue = callReturnValue

    def get_outputs(self, inputs, *args, **kwargs):
        return self.callReturnValue


class ExampleBatchGenerator:
    def __init__(self, returnValue):
        self.returnValue = tf.constant(returnValue, shape=(1, 1), dtype=tf.float32)

    def __next__(self):
        return {"inputValue": self.returnValue}, self.returnValue + 1


class ExampleTrainableBlock(TensorflowBlockBase):
    def __init__(self, requiredOutputSize, **kwargs):
        super().__init__(**kwargs)
        self.requiredOutputSize = requiredOutputSize
        self.exampleDenseLayer = tf.keras.layers.Dense(units=self.requiredOutputSize)

    def get_outputs(self, inputs):
        return self.exampleDenseLayer(inputs=inputs)


class ExampleTensorflowModel(TensorflowModelBase):
    def __init__(self, exampleBlock):
        super().__init__(modelName=None)
        self.exampleBlock = exampleBlock

    def get_loss(self, targets, training=None, **kwargs):
        outputs = self.get_outputs(inputValue=kwargs["inputValue"])
        return tf.reduce_sum(outputs - targets)

    def produce_metrics(self, targets, training, globalStep, **kwargs):
        pass

    @tf.function(input_signature=[tf.TensorSpec(shape=[None, 1], dtype=tf.float32, name="inputValue")])
    def get_outputs(self, inputValue):  # pylint: disable=no-self-use
        return self.exampleBlock.get_outputs(inputs=inputValue)
