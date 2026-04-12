# THREE STRINGS
def threestring(a, b, c):
    p1 = 0
    p2 = 0
    count = 0
    for char in c:
        if p1 < len(a) and char == a[p1]:
            p1 += 1
        elif p2 < len(b) and char == b[p2]:
            p2 += 1
        else:
            count += 1
    return count

# PROBLEM A.TEAM
def check_team(a, row):
    sol = 0
    for j in range(row):
        if sum(a[j]) >= 2:
            sol += 1
    return sol

# B.DRINKS
def orange(a, n):
    return sum(a) / n

# ANTON AND DIGITS
def digit(k2, k3, k5, k6):
    min256 = min(k2, k5, k6)
    k2new = k2 - min256
    min32 = min(k3, k2new)
    return min256 * 256 + min32 * 32

# BAI TAP VE NHA
def result(N, Q, n, x):
    n.sort(key=lambda item: item[1])
    for i in range(Q):
        total_sum = 0
        for j in range(N):
            if x[i] < n[j][1]:
                print(total_sum)
                break
            else:
                total_sum += n[j][0]

# GIFTS FIXING
def move(a_arr, b_arr, num):
    minor = min(b_arr)
    mincan = min(a_arr)
    count = 0
    for i in range(num):
        count += max(b_arr[i] - minor, a_arr[i] - mincan)
    return count

# SUBSTRING REMOVAL
def alice(s):
    a = []
    count_ones = 0
    for char in s:
        if char == '1':
            count_ones += 1
        else:
            if count_ones > 0:
                a.append(count_ones)
                count_ones = 0
    if count_ones > 0:
        a.append(count_ones)
    a.sort(reverse=True)
    return sum(a[0::2])

# TOAN QUAN 2018 VNOI
def num_toan_quan(s, m):
    count = m
    a_vals = sorted([item[0] for item in s])
    b_vals = sorted([item[1] for item in s])
    
    i = 0
    while i < m - 1:
        while i < m - 1 and a_vals[i] == a_vals[i + 1]:
            count -= 1
            i += 1
        i += 1
        
    j = 0
    while j < m - 1:
        while j < m - 1 and b_vals[j] == b_vals[j + 1]:
            count -= 1
            j += 1
        j += 1
    return count

# MEDICINE
def num_medicine(s):
    s_list = list(s)
    count = len(s_list)
    for i in range(len(s_list) - 1):
        for j in range(i + 1, len(s_list)):
            if s_list[j] == '0':
                continue
            if s_list[i] == s_list[j]:
                s_list[j] = '0'
                count -= 1
    return count

# WORDPOW
def check_wordpow(s, t):
    j = 0
    for i in range(len(s)):
        if s[i].lower() == t[j].lower():
            j += 1
        if j == len(t):
            return True
    return False

# FIX YOU
def num_fix_you(a, row, col):
    count = 0
    for i in range(col - 1):
        if a[row - 1][i] != 'R':
            count += 1
    for i in range(row - 1):
        if a[i][col - 1] != 'D':
            count += 1
    return count

# HONEST COACH
def num_honest_coach(a, size):
    a.sort()
    min_diff = a[1] - a[0]
    for i in range(1, size - 1):
        if min_diff == 0:
            return 0
        if min_diff > a[i + 1] - a[i]:
            min_diff = a[i + 1] - a[i]
    return min_diff

# PETYA AND STAIRCASES
def check_petya(a, size, dirty):
    if dirty == 0:
        return True
    a.sort()
    if a[0] == 1 or a[dirty - 1] == size:
        return False
    for i in range(dirty - 2):
        if a[i] == a[i + 2] - 2:
            return False
    return True

# MOVE BRACKETS
def num_move_brackets(s, n):
    ok = 0
    count = 0
    for i in range(n):
        if ok == 0 and s[i] == ')':
            count += 1
            continue
        if s[i] == '(':
            ok += 1
        else:
            ok -= 1
    return count

# BOARD MOVES
def num_board_moves(size):
    total_sum = 0
    if size == 1:
        return 0
    for i in range(size, 2, -2):
        total_sum += (i * 4 - 4) * (i // 2)
    return total_sum

# TWO SHUFFLED SEQUENCES
def sequence(a, size):
    a.sort()
    x = [a[0]]
    y = []
    for i in range(1, size):
        if a[i] == a[i - 1]:
            if i < size - 1 and a[i] == a[i + 1]:
                return False, [], []
            else:
                y.append(a[i])
        else:
            x.append(a[i])
    return True, x, y

# SIMILAR PAIRS
def check_similar_pairs(a, size):
    chan = []
    le = []
    for i in range(size):
        if a[i] % 2 == 0:
            chan.append(a[i])
        else:
            le.append(a[i])
    if len(chan) % 2 == 0:
        return True
    else:
        for i in range(size - 1):
            for j in range(i + 1, size):
                if abs(a[i] - a[j]) == 1:
                    return True
    return False

# TWO TEAM COMPOSING
def num_two_team(a, size):
    if size == 1:
        return 0
    elif size == 2:
        return 1
    else:
        a.sort()
        maxx = 1
        count = 0
        i = 0
        while True:
            count += 1
            dup = 1
            while i != size - 1 and a[i] == a[i + 1]:
                dup += 1
                i += 1
            maxx = max(maxx, dup)
            if i < size - 1:
                i += 1
            else:
                break
        return max(min(count - 1, maxx), min(count, maxx - 1))

# FROG JUMP
def num_frog_jump(a):
    s = 'R' + a + 'R'
    i = 0
    maxd = 1
    while i < len(s) - 1:
        d = 1
        while i + 1 < len(s) and s[i + 1] == 'L':
            d += 1
            i += 1
        maxd = max(maxd, d)
        i += 1
    return maxd

# BAD SEQUENCE
def check_bad_sequence(s):
    if len(s) % 2 != 0:
        return False
    if len(s) == 0:
        return True
    st = [s[0]]
    for i in range(1, len(s)):
        if len(st) > 0 and st[-1] == '(' and s[i] == ')':
            st.pop()
            continue
        st.append(s[i])
    if len(st) == 0:
        return True
    if len(st) > 0 and st[-1] == '(':
        st.pop()
        if len(st) > 0 and st[-1] == ')':
            st.pop()
        if len(st) == 0:
            return True
        return False
    return False

# INCREASING MATRIX
def num_increasing_matrix(a, row, col):
    for i in range(row - 1, 0, -1):
        for j in range(col - 2, -1, -1):
            if a[i][j] == 0:
                a[i][j] = min(a[i + 1][j], a[i][j + 1]) - 1
                if a[i][j] <= a[i - 1][j] or a[i][j] <= a[i][j - 1]:
                    return -1
            if a[i][j] <= a[i - 1][j] or a[i][j] <= a[i][j - 1] or a[i][j] >= a[i + 1][j] or a[i][j] >= a[i][j + 1]:
                return -1
    return sum(sum(row_vals) for row_vals in a)

# SONG COMPRESSION
def num_song_compression(n, m, a, b):
    suma = sum(a)
    sumb = sum(b)
    diff = sorted([a[i] - b[i] for i in range(n)])
    
    if suma <= m:
        return 0
    elif sumb > m:
        return -1
    else:
        temp = suma - m
        i = n - 1
        while temp > 0 and i >= 0:
            temp -= diff[i]
            i -= 1
        return n - (i + 1)

# BOAT COMPETITION
def num_boat_competition(a, size):
    a.sort()
    maxx = 1
    for s in range(2, 101):
        pt1 = 0
        pt2 = size - 1
        count = 0
        while pt1 < pt2:
            if a[pt1] + a[pt2] == s:
                count += 1
                pt1 += 1
                pt2 -= 1
            elif a[pt1] + a[pt2] < s:
                pt1 += 1
            else:
                pt2 -= 1
        maxx = max(maxx, count)
    return maxx

# WATERSLIDE
def num_waterslide(a, size):
    count = 0
    for i in range(size - 1):
        if a[i] > a[i + 1]:
            count += a[i] - a[i + 1]
    return count

# MAKE IT GOOD
def num_make_it_good(a, size):
    i = size - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    while i > 0 and a[i - 1] <= a[i]:
        i -= 1
    return i

# K_TH DOT NOT DIVISIBLE BY N
def num_kth_dot(n, k):
    div = k // (n - 1)
    left = k % (n - 1)
    return div * n + left if left != 0 else div * n - 1

# BOOK READING
def num_book_reading(n, m):
    if m > n:
        return 0
    mlast = m % 10
    if mlast == 0:
        return 0
    store = []
    val = mlast
    i = 1
    s = 0
    while True:
        val = (i * mlast) % 10
        if val in store:
            break
        store.append(val)
        s += val
        i += 1
    rep = (n // m) // len(store)
    left = (n // m) % len(store)
    sumleft = sum(store[:left])
    return s * rep + sumleft

# BALANCED TEAM
def num_balanced_team(size, a):
    a.sort()
    max_count = 1
    j = 0
    for i in range(size):
        while j < size and a[j] - a[i] <= 5:
            j += 1
            max_count = max(max_count, j - i)
    return max_count

# REMOVE K NUM FROM N
def num_remove_k(k, n):
    s = str(n)
    size = len(s) - k
    if k >= len(s):
        return -1
    res = ""
    id = 0
    remov = k
    while id < len(s) and remov != 0:
        maxx = s[id]
        maxxid = id
        countid = 0
        for i in range(1, remov + 1):
            if id + i < len(s) and s[id + i] > maxx:
                maxx = s[id + i]
                countid = i
                maxxid = id + i
        remov -= countid
        res += maxx
        id = maxxid + 1
        if len(res) == size:
            return int(res)
    res += s[maxxid + 1:]
    return int(res[:size])

# POSTCARD
def res_postcard(s, k):
    count_alpha = sum(1 for char in s if char.isalpha())
    count_cane = s.count('?')
    count_star = s.count('*')
    
    if count_alpha == k:
        return "".join(c for c in s if c.isalpha())
    elif count_alpha < k and count_star > 0:
        res = ""
        added = False
        for i in range(len(s)):
            if s[i] == '?' or s[i] == '*':
                continue
            res += s[i]
            if i + 1 < len(s) and s[i + 1] == '*' and not added:
                res += s[i] * (k - count_alpha)
                added = True
        return res
    elif count_alpha > k and count_star + count_cane >= count_alpha - k:
        res = ""
        removals = count_alpha - k
        for i in range(len(s)):
            if s[i].isalpha():
                if i + 1 < len(s) and (s[i + 1] == '*' or s[i + 1] == '?') and removals > 0:
                    removals -= 1
                else:
                    res += s[i]
        return res
    return "Impossible"

# BRACKET SUBSEQUENCE
def result_bracket_subsequence(s, k):
    del_count = (len(s) - k) // 2
    res = []
    for char in s:
        if del_count > 0 and char == ')' and res and res[-1] == '(':
            res.pop()
            del_count -= 1
        else:
            res.append(char)
    return "".join(res)

# DOORS BREAKING
def num_doors_breaking(size, a, x, y):
    if x > y:
        return size
    count = sum(1 for val in a if val <= x)
    return (count + 1) // 2

# DECIMAL TO BINARY
def detobi(num):
    if not num:
        return 0
    return num % 2 + 10 * detobi(num // 2)

# SUM DIGIT
def sumdigit(n):
    if n < 10:
        return n
    return n % 10 + sumdigit(n // 10)

# THREE PARTS OF AN ARRAY
def num_three_parts(a, size):
    sum1 = 0
    sum3 = 0
    id1 = -1
    id3 = size
    max_sum = 0
    while id1 < id3:
        if sum1 < sum3:
            id1 += 1
            if id1 < id3:
                sum1 += a[id1]
        elif sum1 > sum3:
            id3 -= 1
            if id1 < id3:
                sum3 += a[id3]
        else:
            max_sum = sum1
            id1 += 1
            id3 -= 1
            if id1 < id3:
                sum1 += a[id1]
                sum3 += a[id3]
    return max_sum

# SEAT ARRANGEMENTS
def process_seat_arrangements(a, r, c, k):
    num = 0
    if k > r and k > c:
        return 0
    for i in range(r):
        count = 0
        for j in range(c):
            if a[i][j] == '.':
                count += 1
            else:
                count = 0
            if count >= k:
                num += 1
    if k == 1:
        return num
    for j in range(c):
        count_c = 0
        for i in range(r):
            if a[i][j] == '.':
                count_c += 1
            else:
                count_c = 0
            if count_c >= k:
                num += 1
    return num

# DIVIDING NUMBER
def num_dividing_number(n):
    sum_total = n * (n + 1) // 2
    target = sum_total // 2
    subset = []
    for i in range(n, 0, -1):
        if target >= i:
            target -= i
            subset.append(i)
    diff = sum_total - 2 * sum(subset)
    print(diff)
    print(len(subset), *subset)

# UNIQUE COLORS
def num_unique_colors(arr):
    return 4 - len(set(arr))

# SERIES OF CRIMES
def find_series_of_crimes(s, row, col):
    store = []
    for i in range(row):
        for j in range(col):
            if s[i][j] == '*':
                store.append((i, j))
    
    res_row = store[0][0] ^ store[1][0] ^ store[2][0]
    res_col = store[0][1] ^ store[1][1] ^ store[2][1]
    print(f"{res_row + 1} {res_col + 1}")

# VUA KEO
def process_vua_keo(arr, mem, prefix_sum, size, latest_id, ith_change):
    if ith_change > latest_id and latest_id != -1:
        return latest_id + 1
    for i in range(size - 1):
        if mem[i] == -1:
            continue
        prefix_sum[i + 1] = prefix_sum[i + 1] + mem[i] - arr[i]
        if prefix_sum[i] == arr[i]:
            latest_id = i
            return i + 1
    if prefix_sum[size - 1] == arr[size - 1]:
        return size
    return -1