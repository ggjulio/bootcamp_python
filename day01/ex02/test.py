from vector import Vector
import numpy as np

print ("\nBasic test :")
v1 =   Vector([-3.0, -2.0, -1.0, 1.0, 2.0, 3.0])
v2 = np.array([-3.0, -2.0, -1.0, 1.0, 2.0, 3.0])

n = 5

print("me :", v1 * n)
print("np :",   v2 * n)

print ("\n__add__ :")
print("me :", v1 + n)
print("np :",   v2 + n)

print ("\n__radd__ :")
print("me :", n + v1)
print("np :", n + v2)

print ("\n__sub__ :")
print("me :", v1 - n)
print("np :", v2 - n)

print ("\n__rsub__ :")
print("me :", n - v1)
print("np :", n - v2)

print ("\n__truediv__ :")
print("me :", v1 / n)
print("np :", v2 / n)

print ("\n__rtruediv__ :")
print("me :", n / v1)
print("np :", n / v2)

print ("\n__mul__ :")
print("me :", v1 * n)
print("np :", v2 * n)

print ("\n__rmul__ :")
print("me :", n * v1)
print("np :", n * v2)


v = Vector(3)
print(v)

v = Vector((10, 15))
print(v)

v = Vector(5)
print(v)
print(v * .5)

