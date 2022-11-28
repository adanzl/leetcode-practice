"""
 * 链接：https://www.acwing.com/problem/content/description/4715/
"""

l = input().split()
n, r1, r2 = int(l[0]), int(l[1]), int(l[2])
arr = input().split()
parent = [0] * n
idx = 0
for i in range(n - 1):
    if i + 1 == r1:
        idx += 1
    parent[idx] = int(arr[i])
    idx += 1

np = parent[:]
p = r2
while p != r1:
    t = p
    p = parent[p - 1]
    np[p - 1] = t
del np[r2 - 1]
print(' '.join([str(i) for i in np]))