from src.Benchmark.ZDT import ZDT1,ZDT2, ZDT3, ZDT6 
from src.Benchmark.DTLZ import DTLZ1, DTLZ2, DTLZ5, DTLZ7

def get_problem(name, *args, **kwargs):
    name = name.lower()

    Problem = {
        'zdt1':ZDT1,
        'zdt2':ZDT2,
        'zdt3':ZDT3,
        'zdt6':ZDT6,
        'dtlz1':DTLZ1,
        'dtlz2':DTLZ2,
        'dtlz5':DTLZ5,
        'dtlz7':DTLZ7,
    }

    return Problem[name](*args, **kwargs)