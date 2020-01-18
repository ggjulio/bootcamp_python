def ft_filter(f, list_of_inputs):
    return (x for x in list_of_inputs if f(x))
