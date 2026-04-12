# CAU 1
def reverse_string(s):
    return s[::-1]

# CAU 2
def recover(s):
    return s.swapcase()

# CAU 3
def find_substring(s, subs):
    return s.find(subs)

# CAU 5
def process_string(s):
    return " ".join(s.split())

# CAU 6
def cutstring(s, index):
    if index < 0 or index >= len(s):
        return ""
    return s[index:]

# CAU 10
def longpali(s):
    for size in range(len(s), 1, -1):
        for i in range(len(s) - size + 1):
            sub = s[i:i+size]
            if sub == sub[::-1]:
                return sub
    return ""

# CAU 7
def findallid(s1, s2):
    res = [i for i, char in enumerate(s1) if char == s2[0]]
    return res if res else [-1]

# CAU 8
def replacestring(s, s1, s2):
    return s.replace(s1, s2)

# CAU 11
def longnonrep(s):
    for size in range(len(s), 1, -1):
        for i in range(len(s) - size + 1):
            sub = s[i:i+size]
            if len(set(sub)) == len(sub):
                return size
    return 1 if len(s) > 0 else 0

# CAU 12
def findmaxcol(arr, row, col):
    max_sum = float('-inf')
    max_id = -1
    for j in range(col):
        col_sum = sum(arr[i][j] for i in range(row))
        if col_sum >= max_sum:
            max_sum = col_sum
            max_id = j
    return max_id

# CAU 13
def digprod(arr, row, col):
    prod = 1
    for i in range(min(row, col)):
        prod *= arr[i][i]
    return prod

# BAI 14
def issymetric(arr, size):
    for i in range(size):
        for j in range(size):
            if arr[i][j] != arr[j][i]:
                return False
    return True

# BAI 16
def num_ascend(arr, row, col):
    count = 0
    for i in range(row):
        is_ascend = True
        for j in range(col - 1):
            if arr[i][j] > arr[i][j + 1]:
                is_ascend = False
                break
        if is_ascend:
            count += 1
    return count

# BAI 17
def num_primecol(arr, row, col):
    def isprime(n):
        if n <= 1: 
            return False
        if n == 2: 
            return True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: 
                return False
        return True
    
    count = 0
    for j in range(col):
        col_sum = sum(arr[i][j] for i in range(row))
        if isprime(col_sum):
            count += 1
    return count

# BAI 19
def submatrix(arr, row, col):
    count = 0
    for i in range(row - 1):
        for j in range(col - 1):
            sub_sum = arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1]
            if sub_sum % 2 != 0:
                count += 1
    return count

# MOST FREQUENT CHARACTER
def mostFrequentCharacter(s):
    if not s: 
        return None, 0
    s = s.lower()
    freq_map = {}
    for char in s:
        if char != '0':
            freq_map[char] = freq_map.get(char, 0) + 1
    if not freq_map: 
        return None, 0
    max_freq = max(freq_map.values())
    res_char = min([char for char, freq in freq_map.items() if freq == max_freq])
    return res_char, max_freq

# CONVERT TO BASE M
def convertToBaseM(n, m=2):
    if n == 0:
        return 0
    return n % m + 10 * convertToBaseM(n // m, m)

# CALCULATE POWER
def calculate_power(n, e):
    if e == 1:
        return n
    return n * calculate_power(n, e - 1)

# GCD RECURSION
def gcdRecursion(p, q):
    if q == 0:
        return p
    return gcdRecursion(q, p % q)

# COUNT WAY SUM OF SQUARE
def countWaySumOfSquare(x):
    def count_ways(x_val, maxsquare):
        if x_val == 0: 
            return 1
        if x_val < 0 or maxsquare == 0: 
            return 0
        square = maxsquare * maxsquare
        return count_ways(x_val - square, maxsquare - 1) + count_ways(x_val, maxsquare - 1)
    
    return count_ways(x, int(x**0.5))