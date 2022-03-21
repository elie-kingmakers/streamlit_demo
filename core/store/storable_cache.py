import gzip
import json
from pathlib import Path
from typing import Type, Union

from core.datamodel.storable import Storable
from core.store.base_storable_cache import BaseStorableCache
from core.utils.saving import safe_json_dumps


class StorableCache(BaseStorableCache):
    def __init__(self, elementType: Type[Storable], fileName: Union[str, Path], writeable: bool = False):
        super().__init__(elementType=elementType, writeable=writeable)
        self.fileName = fileName
        self.file = None

    def _open(self):
        self.file = gzip.open(filename=self.fileName, mode="wt" if self.writeable else "rt")
        return self

    def _close(self):
        self.file.close()

    def _add(self, element):
        self.file.write(safe_json_dumps(data=element.to_data()) + "\n")

    def _get(self):
        for line in self.file:
            yield self.elementType.from_data(source=json.loads(line.rstrip()))
