from ft_map import ft_map
from ft_reduce import ft_reduce
from ft_filter import ft_filter
from functools import reduce

###############################################
##############      ft_map         ############
###############################################

items = [1, 2, 3, 4, 5]
print("map    :", list(map(lambda x: x**2, items)))

print("ft_map :", list(ft_map(lambda x: x**2, items)))


###############################################
##############      filter         ############
###############################################

number_list = range(-5, 5)
print("filter    :", list(filter(lambda x: x < 0, number_list)))
print("ft_filter :", list(ft_filter(lambda x: x < 0, number_list)))



###############################################
##############      reduce         ############
###############################################



print("reduce    :", reduce((lambda x, y: x * y), [1, 2, 3, 4]))
print("ft_reduce :", ft_reduce((lambda x, y: x * y), [1, 2, 3, 4]))

