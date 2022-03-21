import inspect
from datetime import datetime


def _to_data(value):
    if isinstance(value, list):
        return [_to_data(v) for v in value]
    if isinstance(value, dict):
        return {k: _to_data(v) for k, v in value.items()}
    if isinstance(value, Storable):
        return value.to_data()
    if isinstance(value, set):
        return list(value)
    if isinstance(value, datetime):
        return value.isoformat()
    return value


class Storable:
    def __init__(self, **kwargs):
        pass

    def to_data(self):
        return {
            k: _to_data(v) for k, v in self.__dict__.items() if k in inspect.signature(self.__class__).parameters.keys()
        }

    @classmethod
    def from_data(cls, source):
        return cls._from_data(source=source, converters=None)

    @classmethod
    def _from_data(cls, source, converters=None):
        realParameters = set(cls.__init__.__code__.co_varnames)
        unknownParameters = set(source) - realParameters
        if len(unknownParameters) > 0:
            print(f"Unknown input in {cls.__name__}: {unknownParameters}")
        if converters is None:
            converters = {}
        converters = {k: datetime.fromisoformat(v) if v == "datetime" else v for k, v in converters.items()}
        return cls(**{k: converters[k](v) if k in converters else v for k, v in source.items() if k in realParameters})
