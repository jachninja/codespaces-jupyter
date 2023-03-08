"""
This is a template of how to solve a quadratic. 
We will improve it with time.
"""

import math
# ax**2 + bx + c = 0
# x0 = (-b + sqrt(b*b - 4 *a*c))/(2*a)
# x1 = (-b - sqrt(b*b - 4 *a*c))/(2*a)


a = 1
b = -10
c = 10

x0 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
x1 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)

print(f"x0 = {x0}")
print(f"x1 = {x1}")

