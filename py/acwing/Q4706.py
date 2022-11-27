"""
 * 链接：https://www.acwing.com/problem/content/description/4709/
"""

# 总起点到终点的边经过2次，其余的边经过一次
n = int(input())
g = [[] for _ in range(n)]
tot = 0
for i in range(n - 1):
    x, y, w = map(int, input().split())
    g[x - 1].append([y - 1, w])
    g[y - 1].append([x - 1, w])
    tot += w
dis = [0] * n

q = [[0, -1, 0]]
while q:
    t = q[:]
    q = []
    for idx, p, v in t:
        dis[idx] = v
        for nx, c in g[idx]:
            if nx == p: continue
            q.append([nx, idx, v + c])

print(tot * 2 - max(dis))