# Nhap vao n, dem so luong so nguyen to trong n
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = input()
counter = 0
for x in n:
    if is_prime(int(x)):
        counter+=1
print(counter)