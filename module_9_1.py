some_ints = [1, 11, 25, 78, 100]


def apply_all_func(int_list, *functions):
    result = {}
    for func in functions:
        func_work = func(int_list)
        result.update({func.__name__: func_work})
    return result


test = apply_all_func(some_ints, min, max, len, sum, sorted)
print(test)
