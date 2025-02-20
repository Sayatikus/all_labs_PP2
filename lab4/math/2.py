def trapezoid_area(height, base1, base2):
    return (base1 + base2) * height / 2
height = int(input())
base1 = int(input())
base2 = int(input())
area = trapezoid_area(height, base1, base2)
print("Expected Output:", area)