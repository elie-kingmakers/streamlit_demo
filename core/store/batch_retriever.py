from abc import ABC, abstractmethod

from core.datamodel.data_batch import DataBatch


class BatchRetriever(ABC):
    @abstractmethod
    def get_batch(self, batchSize: int) -> DataBatch:
        raise NotImplementedError(f"{self.__class__.__name__} must implement `get_batch` function")
