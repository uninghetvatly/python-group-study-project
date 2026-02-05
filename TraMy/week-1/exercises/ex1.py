# Tinh va in ra phan nguyen, phep du cua phep chia 2 so nguyen a, b
a = int(input())
b = int(input())

if b == 0:
    print("Invalid!")

nguyen = a // b
du = a % b

print(nguyen, du)