def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    print(results)


apply_all_func([6, 20, 15, 9,45], max, min)
apply_all_func([6, 20, 15, 9], len, sum, sorted)
