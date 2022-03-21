from multiprocessing import Pool, cpu_count
from typing import Callable, Iterable


def run_multiprocessing(functionToProcess: Callable, parameterList: Iterable, threads: int = None):
    with Pool(round(cpu_count() / 2) if not threads else threads) as pool:
        results = pool.map(functionToProcess, parameterList)
        pool.close()
        pool.join()
        pool.terminate()
        return results
