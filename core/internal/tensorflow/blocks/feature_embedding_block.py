from typing import List, Union

import tensorflow as tf
from tensorflow.python.keras import layers

from core.internal.tensorflow.blocks.tensorflow_block_base import TensorflowBlockBase


class FeatureEmbeddingBlock(TensorflowBlockBase):
    def __init__(self, categoricalIds: Union[List[int], List[str]], embeddingDimension: int, blockName: str):
        super().__init__(blockName=blockName)
        self.categoricalIds = categoricalIds
        self.embeddingDimension = embeddingDimension
        self.numCategories = len(categoricalIds)
        self.idLookupTable = tf.lookup.StaticHashTable(
            initializer=tf.lookup.KeyValueTensorInitializer(
                keys=self.categoricalIds, values=list(range(self.numCategories))
            ),
            default_value=0,
            name=f"idLookupTable_{self.blockName}",
        )
        self.embeddingMatrix = layers.Embedding(
            input_dim=self.numCategories,
            output_dim=self.embeddingDimension,
            embeddings_initializer=tf.random_normal_initializer(),
            name=f"embeddingMatrix_{self.blockName}",
        )

    def get_outputs(self, inputs: tf.Tensor, *args, **kwargs) -> tf.Tensor:  # pylint: disable=unused-argument
        with tf.name_scope(f"embeddingBlock_{self.blockName}"):
            itemIds = self.idLookupTable.lookup(keys=inputs)
            return self.embeddingMatrix(inputs=itemIds)
