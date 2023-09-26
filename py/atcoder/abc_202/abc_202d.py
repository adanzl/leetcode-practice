"""
 * 链接：https://atcoder.jp/contests/abc202/tasks/abc202_d
"""
import math

a, b, k = 2, 2, 2  # aabb->abab->abba->baab->baba->bbaa
a, b, k = 2, 2, 4  # baab
a, b, k = 2, 2, 5  # baba
a, b, k = 30, 30, 118264581564861424  # bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# a, b, k = list(map(int, input().split()))

calc = lambda a, b: math.factorial(a + b) // math.factorial(a) // math.factorial(b)

k -= 1
arr = []
while a and b and k:
    cc = calc(a - 1, b)  # 假设最高位是个 a
    if cc <= k:  # a 不够
        arr.append('b')
        b -= 1
        k -= cc
    else:  # 超了
        a -= 1
        arr.append('a')

for _ in range(a):
    arr.append('a')
for _ in range(b):
    arr.append('b')
print(''.join(arr))