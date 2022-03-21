from itertools import groupby


def get_data_batches(data, numBatches: int = None):
    batchIds = [list(v) for k, v in groupby(list(range(len(data))), key=lambda x: x // (len(data) / numBatches))]
    return [[data[index] for index in batchIndices] for batchIndices in batchIds]
