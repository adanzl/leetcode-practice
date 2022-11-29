"""
 * 链接：https://www.acwing.com/problem/content/description/4629/
"""
from math import gcd
lcm = lambda a, b: a * b // gcd(a, b)
# n = int(input())
# nx = list(map(int, input().split()))
n = 4
nx = list(map(int, "2 3 1 4".split()))  # 3
# nx = list(map(int, "4 4 4 4".split()))  # -1
# nx = list(map(int, "2 1 4 3".split()))  # 1

# 本题的意思是，每一个点都能找到一个目标点，并且通过t都能到达自己的目标点，求此时的最小t
vis = set()
l = []
for i in range(n):
    if i in vis: continue
    vis.add(i)
    p = nx[i] - 1
    vis.add(p)
    ln = 1
    while p != i:
        ln += 1
        p = nx[p] - 1
        if p in vis: break
        vis.add(p)
    if p != i:
        print(-1)
        exit()
    s= set()
    l.append(ln if ln & 1 else ln // 2)
ans = 1
for num in l:
    ans = lcm(ans, num)
print(ans)