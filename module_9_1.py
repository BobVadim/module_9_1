def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        smallest_number = min(int_list)
        results[min.__name__] = smallest_number
        max_number = max(int_list)
        results[max.__name__] = max_number
        old_number = len(int_list)
        results[len.__name__] = old_number
        sum_number = sum(int_list)
        results[sum.__name__] = sum_number
        sort_number = sorted(int_list)
        results[sorted.__name__] = sort_number

    return print(results)


apply_all_func([34, 345, 17.77,  655, 999.13, 5566, 17], min)
