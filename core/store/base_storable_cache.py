from abc import ABC, abstractmethod
from typing import Type

from core.datamodel.storable import Storable


class BaseStorableCache(ABC):
    def __init__(self, elementType: Type[Storable], writeable: bool = False):
        super().__init__()
        self.elementType = elementType
        self.writeable = writeable
        self.modified = False
        self.isOpen = False

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # pylint: disable=invalid-name
        self.close()

    def __iter__(self):
        return self

    def __next__(self):
        self.check_if_open()
        return next(self._get())

    def check_if_open(self):
        if not self.isOpen:
            raise Exception(f"{self.__class__.__name__} is not open")

    def open(self):
        if self.isOpen:
            raise Exception(f"{self.__class__.__name__} is already open")
        self.isOpen = True
        self._open()
        return self

    def add(self, element):
        self.check_if_open()
        self.modified = True
        self._add(element=element)

    def load(self):
        return list(self)

    def close(self):
        self.check_if_open()
        if self.modified and not self.writeable:
            raise Exception(f"{self.__class__.__name__} was modified but not saved")
        self._close()

    @abstractmethod
    def _open(self):
        pass

    @abstractmethod
    def _add(self, element):
        pass

    @abstractmethod
    def _get(self):
        pass

    @abstractmethod
    def _close(self):
        pass
