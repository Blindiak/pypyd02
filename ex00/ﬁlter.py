def ft_filter(function_to_apply, list_of_inputs):
    v_type = type(list_of_inputs)
    r = v_type()
    for list_elem in list_of_inputs:
        if function_to_apply(list_elem):
            r += list_elem
