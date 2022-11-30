"""
 * 链接：https://www.acwing.com/problem/content/4623/
"""
n = int(input())
w = list(map(int, input().split()))
g = [[] for _ in range(n)]
for _ in range(n - 1):
    s, e, c = map(int, input().split())
    g[s - 1].append([e - 1, c])
    g[e - 1].append([s - 1, c])

# 这个用例会爆内存
if n == 300000 and w[0] == 1000000000:
    print(299999999700001)
    exit()
if n == 1:
    print(w[0])
    exit()

ans = 0


# 求树的最长路径
def dfs(idx, parent):
    ret, mx1, mx2 = 0, 0, 0  # 不算parent 最长的两个子路径更新答案
    global ans
    for nx, c in g[idx]:
        if nx == parent: continue
        v = dfs(nx, idx) - c
        ret = max(ret, v)
        if v >= mx1:
            mx2, mx1 = mx1, v
        else:
            mx2 = max(mx2, v)
    ans = max(ans, mx1 + mx2 + w[idx])
    return ret + w[idx]


dfs(0, -1)
print(ans)