from src.Benchmark.ZDT import ZDT1,ZDT2, ZDT3, ZDT4, ZDT6 
from src.Benchmark.DTLZ import DTLZ1, DTLZ2, DTLZ3,DTLZ4, DTLZ5, DTLZ7
from src.Benchmark.constraintfunc import Binhkorn, ChanKong, ConstrEx, TNK
from src.Benchmark.noconstraintfun import Fonsecaf, Kursawe, Viennet
def get_problem(name, *args, **kwargs):
    name = name.lower()

    Problem = {
        'zdt1':ZDT1,
        'zdt2':ZDT2,
        'zdt3':ZDT3,
        'zdt4':ZDT4,
        'zdt6':ZDT6,
        'dtlz1':DTLZ1,
        'dtlz2':DTLZ2,
        'dtlz3':DTLZ3,
        'dtlz4':DTLZ4,
        'dtlz5':DTLZ5,
        'dtlz7':DTLZ7,
        'binhkorn':Binhkorn,
        'chankong':ChanKong,
        'fonsecaf': Fonsecaf,
        'kursawe': Kursawe,
        'viennet': Viennet,
        'constrex': ConstrEx,
        'tnk':TNK,
    }

    return Problem[name](*args, **kwargs)