# Function tra ve funtion

def power(n):
    def inner(x):
        return x ** n
    return inner

square = power(2)
cube = power(3)

print(square(4))  # 16
print(cube(2))    # 8