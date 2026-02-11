# Note dùng để ghi lại những lỗi cá nhân mắc phải trong quá trình học ngôn ngữ Python
## In ra số chữ số thập phân sau dấu chấm
```python
print(":.2f".format(c * 9 / 5 + 32))
```
Sai do thiếu dấu {}. Sửa thành:
```python
print("{:.2f}".format(c * 9 / 5 + 32))
```
## Lỗi khi dùng range trong loop
```python
n = int(input())
chan = 0
le = 0
for x in n:
    if x % 2 == 0:
        chan+=1
    else:
        le+=1
print(chan, le)
```
Lỗi do trong range không thể check số nguyên, nó thường dùng để check chuỗi. Sửa thành:
```python
n = input()
chan = 0
le = 0
for x in n:
    if int(x) % 2 == 0:
        chan+=1
    else:
        le+=1
print(chan, le)
```
## Lỗi để số float trong range
```python
for i in range(2, (n**0.5) + 1):
```
Khi căn thì sẽ tạo ra số float, mà range chỉ có thể để số nguyên, ta nên ép kiểu như sau:
```python
for i in range(2, int(n**0.5) + 1):
```