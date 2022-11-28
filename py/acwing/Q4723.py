"""
 * 链接：https://www.acwing.com/problem/content/4726/
"""
n = int(input())
m = 5
arr = 'abcde'
while n >= m:
    n -= m
    m <<= 1
cnt = m // 5
a, r = divmod(n, cnt)
print(arr[a - 1] if r == 0 else arr[a])
