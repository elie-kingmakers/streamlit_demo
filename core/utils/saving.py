import json

import numpy as np


def safe_json_dumps(data):
    def _json_convert_numpy(value):
        if isinstance(value, (np.int32, np.int64)):
            return int(value)
        if isinstance(value, (np.float32, np.float64)):
            return float(value)
        if isinstance(value, np.ndarray):
            return value.tolist()
        raise TypeError(f"{value} (type: {type(value)}) can't be converted for json.dumps")

    return json.dumps(data, default=_json_convert_numpy)
