import math

# Viet function tra ve dien tich hinh tron
def circle_area(r):
    if r < 0:
        return None
    return math.pi*r*r

r = float(input())
print(circle_area(r))