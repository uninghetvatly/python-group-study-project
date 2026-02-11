# Nhap vao n, in ra so luong chu so chan, so le cua n
n = input()
chan = 0
le = 0
for x in n:
    if int(x) % 2 == 0:
        chan+=1
    else:
        le+=1
print(chan, le)