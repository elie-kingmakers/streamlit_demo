from typing import Any, List


class DataBatch:
    def __init__(self, data: List[Any]):
        self.data = data

    def __iter__(self):
        for value in self.data:
            yield value

    def __len__(self):
        return len(self.data)
