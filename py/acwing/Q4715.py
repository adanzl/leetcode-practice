"""
 * 链接：https://www.acwing.com/problem/content/description/4718/
"""

from collections import defaultdict, Counter

n = int(input())
s = input()
g = defaultdict(list)
parent = [i for i in range(n)]
cnt = Counter()


def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]


for i in range(n - 1):
    r, r1 = find(i), find(i + 1)
    if s[i] == '=':
        parent[r1] = r
        cnt[r] += 0
    elif s[i] == '>':
        g[r1].append(r)
        cnt[r] += 1
        cnt[r1] += 0
    else:
        g[r].append(r1)
        cnt[r] += 0
        cnt[r1] += 1
q = []
for k, v in cnt.items():
    if v == 0: q.append(k)
num = 1
arr = [0] * n
while q:
    tmp = q
    q = []
    for idx in tmp:
        arr[idx] = num
        for nx in g[idx]:
            cnt[nx] -= 1
            if cnt[nx] == 0: q.append(nx)
    num += 1
for i in range(n):
    arr[i] = arr[find(i)]
# print(parent)
print(" ".join([str(num) for num in arr]))
