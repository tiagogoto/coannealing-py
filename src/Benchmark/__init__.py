

def get_problem(name, *args, **kwargs):
    name.lower()

    Problem = {
        'zdt1':ZDT1,
        'zdt2':ZDT2,
    }

    return Problem[name](*args, **kwargs)