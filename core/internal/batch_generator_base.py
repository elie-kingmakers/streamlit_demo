from abc import ABC, abstractmethod

from core.datamodel.data_batch import DataBatch
from core.store.batch_retriever import BatchRetriever


class BatchGeneratorBase(ABC):
    def __init__(self, dataRetriever: BatchRetriever, batchSize: int):
        self.dataRetriever = dataRetriever
        self.batchSize = batchSize

    def __next__(self):
        batch = self.dataRetriever.get_batch(batchSize=self.batchSize)
        return self.process_batch(batch=batch)

    @staticmethod
    @abstractmethod
    def process_batch(batch: DataBatch):
        pass
