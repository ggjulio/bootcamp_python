def ft_reduce(f, list_of_inputs):
	result = list_of_inputs[0]
	for x in list_of_inputs[1:]:
	    result = f(result, x)

	return(result)