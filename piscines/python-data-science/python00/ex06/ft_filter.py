def ft_filter(function_to_apply, list_of_inputs):
    """This function iterates the second element
    applying the first function on each element
    which is a predicate (returns a bool)
    and returns a new iterator with the
    elements which return True"""
    return iter([i for i in list_of_inputs if function_to_apply(i)])
