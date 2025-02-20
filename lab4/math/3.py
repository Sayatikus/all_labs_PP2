import math
n = int(input("n: "))
a = int(input("a: "))
S = (n * (a ** 2)) / 4 * (1/math.tan(math.pi/n))
print(int(S))