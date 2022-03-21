import inspect
from abc import ABC, abstractmethod
from typing import List, Union

import tensorflow as tf
from tensorflow.python import keras

from core.internal.tensorflow.blocks.tensorflow_block_base import TensorflowBlockBase


class TensorflowModelBase(keras.Model, ABC):
    def __init__(self, modelName: str = None, **kwargs):
        super().__init__(**kwargs)
        self.modelName = modelName or self.__class__.__name__

    def get_model_blocks(self) -> List[TensorflowBlockBase]:
        constructorParameters = inspect.signature(self.__class__.__init__).parameters.keys()
        return [
            v for k, v in self.__dict__.items() if k in constructorParameters and isinstance(v, TensorflowBlockBase)
        ]

    @abstractmethod
    def get_loss(self, targets: Union[tf.Tensor, List[tf.Tensor]], training: bool, **kwargs) -> tf.Tensor:
        pass

    @abstractmethod
    def produce_metrics(
        self, targets: Union[tf.Tensor, List[tf.Tensor]], training: bool, globalStep: int, **kwargs
    ) -> None:
        pass

    @abstractmethod
    def get_outputs(self, *args, **kwargs) -> Union[tf.Tensor, List[tf.Tensor]]:
        pass
