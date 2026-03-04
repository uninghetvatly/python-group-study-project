# Kiem tra so hoan hao

def is_perfect(n):
    if n <= 1:
        return False
    count = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            count = count + i
    if count == n:
        return True
    else:
        return False

print(is_perfect(6))   # True
print(is_perfect(28))  # True
print(is_perfect(12))  # False