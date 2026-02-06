# Kiem tra nam nhuan
num = int(input())
if num < 0:
    print("INVALID")
    exit()
if num % 400 == 0 or (num % 4 == 0 and num % 100 != 0):
    print("YES")
else:
    print("NO")