"""
 * 链接：https://www.acwing.com/problem/content/4790/
"""

from math import gcd

n, m = map(int, input().split())
p = n // 2
if p > m:
    print(-1)
    exit()
v = min(5 * 10**8, m - p + 1)
s = set()
ans = []
while m > 0 and v > 1:
    ans.append(v)
    ans.append(v * 2)
    if len(ans) > n:
        # print(ans)
        # print(len(ans), m)
        print(-1)
        exit()
    s.add(v)
    s.add(v * 2)
    m -= v
    v = min(v - 1, m - (n - len(ans)) // 2 + 1)
    while v in s:
        v -= 1
for i in range(1, 10**9 + 1):
    if len(ans) == n:
        break
    if i in s: continue
    if ans and gcd(ans[-1], i) != 1: continue
    ans.append(i)
    s.add(i)
if len(ans) < n:
    print(-1)
    exit()
print(*ans, sep=' ')
