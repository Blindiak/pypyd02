def ft_reduce(function_to_apply, list_of_inputs):
    it = iter(list_of_inputs)
    r = next(it)
    for elem in it:
        r = function_to_apply(r, elem)
    return r
