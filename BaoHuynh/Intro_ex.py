# NTH FIBONACCI
def fibo_res(n):
    a = [0] * max(3, n + 1)
    a[1] = 0
    a[2] = 1
    for i in range(3, n + 1):
        a[i] = a[i - 1] + a[i - 2]
    return a[n]

# ARRAY OUT OF FIBONACCI ARRAY
def fibonacci_array(size):
    a = [0] * max(3, size + 1)
    if size == 1:
        print(0)
    elif size == 2:
        print(0, 1)
    else:
        a[1] = 0
        a[2] = 1
        print(f"{a[1]} {a[2]}", end=" ")
        for i in range(3, size + 1):
            a[i] = a[i - 1] + a[i - 2]
            print(a[i], end=" ")

# LARGEST ELEMENT IN AN ARRAY
def find_big(a, n):
    max_val = 0
    for i in range(n):
        if a[i] > max_val:
            max_val = a[i]
    return max_val

# TABULATE SIN, COS, TAN
def tabulate_trig():
    import math
    for x in range(5, 85, 5):
        rad = x / 180.0 * 3.14
        print(f"{math.sin(rad):.2f} {math.cos(rad):.2f} {math.tan(rad):.2f}")
    rad = 85 / 180.0 * 3.14
    print(f"{math.sin(rad):.2f} {math.cos(rad):.2f} {math.tan(rad):.2f}")

# TRANSPOSITION OF A SQUARE MATRIX
def transpose_matrice(a, size):
    for i in range(size - 1):
        j = i + 1
        while j < size:
            a[i][j], a[j][i] = a[j][i], a[i][j]
            j += 1

# CIRCLE CIRCUMFERENCE
def circle_circumference(r):
    pi = 3.1416
    return r * 2 * pi

# COMPOUND INTEREST
def compound_interest(a, n):
    i = 0.095
    return a * ((1 + i) ** n)

# SWAP USING MATH
def swap_math(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# CHECKING NEG POS 0
def check_sign(a):
    if a > 0:
        print("la so duong")
    elif a < 0:
        print("la so am")
    else:
        print("la so 0")

# MAX 3
def max_of_three(a, b, c):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val

# LINEAR EQUATION
def linear_equation(a, b):
    if a == 0 and b == 0:
        print("infinite solution")
    elif a == 0 and b != 0:
        print("no solution")
    else:
        print("ket qua la", -b / a)

# DAY OF MONTH AND YEAR
def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if year % 4 == 0:
            return 29
        else:
            return 28

# SUM PRODUCT OF ODD POSITIVE
def sum_product_odd_even(n):
    sum_odd = 0
    sum_even = 0
    pro_odd = 1
    pro_even = 1
    for i in range(1, n + 1, 2):
        sum_odd += i
        if i + 1 <= n:
            sum_even += (i + 1)
        pro_odd *= i
        if i + 1 <= n:
            pro_even *= (i + 1)
    return sum_odd, sum_even, pro_odd, pro_even

# CHECKING ISPRIME
def checkPrimeNumber(n):
    if n < 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

# UCLN
def gcd(a, b):
    while b != 0:
        so_du = a % b
        a = b
        b = so_du
    return a

# COUNTING FACTORS
def counting_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

# NAME SCORE AND PASSING STATUS
def student_status(names, scores):
    pass_status = []
    for score in scores:
        if score >= 50:
            pass_status.append("pass")
        else:
            pass_status.append("failed")
    for i in range(len(scores)):
        print(f"{names[i]:<5} {scores[i]}  {pass_status[i]:<5}")

# MULTIPLES ADDITION AVERAGE
def sum_tripple(a, b, c):
    return a + b + c

def mul_tripple(a, b, c):
    return a * b * c

def avg_tripple(a, b, c):
    return sum_tripple(a, b, c) / 3

# CALCULATE AREAS
def square(a):
    return a * a

def rectangle(a, b):
    return a * b

def triangle(h, a):
    return 0.5 * h * a

def circle(r):
    pi = 3.1416
    return r * r * pi

# CONVERT BINARY TO DECIMAL
def convertBinaryToDecimal(n):
    dec = 0
    length = len(n)
    for i in range(length - 1, -1, -1):
        if n[i] == '1':
            dec += 2 ** (length - 1 - i)
    return dec

# PRINT PRIMES IN RANGE
def printPrimes(lower, upper):
    for i in range(lower, upper + 1):
        if checkPrimeNumber(i):
            print(i, end=" ")

# REVERSE NUMBER
def reverseNum(n):
    reverse = 0
    mod = 10
    while n // mod != 0:
        mod *= 10
    mod = mod // 10
    while mod >= 1:
        reverse = reverse + (n % 10) * mod
        n = n // 10
        mod = mod // 10
    return reverse