n, q = map(int, input().split())
parent = [i for i in range(n + 1)]
g = [[] for _ in range(n + 1)]
ans = []


def find(x, parent):
    if parent[x] == x: return x
    parent[x] = find(parent[x], parent)
    return parent[x]


query = [[] for _ in range(n + 1)]
for i in range(q):
    l = list(map(int, input().split()))
    if len(l) == 2:
        x, y = l
        r1, r2 = find(x, parent), find(y, parent)
        if r1 == r2:
            query[x].append([y, len(ans)])
            query[y].append([x, len(ans)])
        ans.append(-1)
    else:
        x, y, w = l
        r1, r2 = find(x, parent), find(y, parent)
        parent[r1] = r2
        g[x].append([y, w])
        g[y].append([x, w])

vis = [False] * (n + 1)
for i in range(1, n + 1):
    if not vis[find(i, parent)]:
        g[0].append([i, 0])
        g[i].append([0, 0])
        vis[find(i, parent)] = True

vis = [False] * (n + 1)
dis = [0] * (n + 1)


def dfs(root, v):
    dis[root] = v
    for nx, c in g[root]:
        if vis[nx]: continue
        vis[nx] = True
        dfs(nx, v + c)


dfs(0, 0)

fa = [i for i in range(n + 1)]
vis = [False] * (n + 1)


def tarjan(u):
    for nx, c in g[u]:  # 遍历与U相邻的所有节点v
        if vis[nx]: continue
        vis[nx] = True
        tarjan(nx)  # 递归v
        fa[find(nx, fa)] = find(u, fa)  # 把v合并到u上，即将v的父节点设为u
    for e, idx in query[u]:  # 遍历与u有询问关系的节点v
        if vis[e]:
            lca = find(e, fa)
            ans[idx] = dis[u] + dis[e] - 2 * dis[lca]
            # print(idx, u, e, lca, dis, dis[u], dis[e], dis[lca])


tarjan(0)
print(*ans, sep='\n')
