from src.Benchmark.ZDT import ZDT1
from src.Benchmark.ZDT import ZDT2

def get_problem(name, *args, **kwargs):
    name = name.lower()

    Problem = {
        'zdt1':ZDT1,
        'zdt2':ZDT2,
    }

    return Problem[name](*args, **kwargs)