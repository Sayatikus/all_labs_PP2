import math
def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

degrees = int(input("Input degree: "))
print("Degrees to radians: ", degrees_to_radians(degrees))