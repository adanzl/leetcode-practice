/**
 * 链接：https://iai.sh.cn/problem/721
 */
#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const LL INF = 1e18;
const LL N = 3e5 + 5;

int n, q, _clock = 1;
vector<pair<LL, LL>> g[N], query[N];
LL parent[N], fa[N], dis[N], vis[N], ans[N], cnt_q = 0;

LL _find(LL x, LL* p) {
  if (p[x] == x) return x;
  return p[x] = _find(p[x], p);
}

void dfs(LL root, LL pre, LL v) {
  dis[root] = v;
  for (LL i = 0; i < g[root].size(); i++) {
    LL nx = g[root][i].first, c = g[root][i].second;
    if (nx == pre) continue;
    dfs(nx, root, v + c);
  }
}

void tarjan(LL u) {
  for (LL i = 0; i < g[u].size(); i++) {
    LL nx = g[u][i].first;
    if (vis[nx] == _clock) continue;
    vis[nx] = _clock;
    tarjan(nx);
    fa[_find(nx, fa)] = _find(u, fa);
  }
  for (LL i = 0; i < query[u].size(); i++) {
    LL e = query[u][i].first, idx = query[u][i].second;
    if (vis[e] == _clock) {
      LL lca = _find(e, fa);
      ans[idx] = dis[u] + dis[e] - 2 * dis[lca];
    }
  }
}

int main() {
  cin >> n >> q;
  for (int i = 1; i <= n; i++) {
    parent[i] = i;
    fa[i] = i;
  }

  while (q--) {
    LL x, y, w;
    cin >> x >> y;
    if (getchar() == ' ') {
      cin >> w;
      LL r1 = _find(x, parent), r2 = _find(y, parent);
      parent[r1] = r2;
      g[x].push_back(make_pair(y, w));
      g[y].push_back(make_pair(x, w));
    } else {
      if (_find(x, parent) != _find(y, parent)) {
        ans[cnt_q] = -1;
      } else {
        query[x].push_back(make_pair(y, cnt_q));
        query[y].push_back(make_pair(x, cnt_q));
      }
      ++cnt_q;
    }
  }
  for (int i = 1; i <= n; i++) {
    if (_find(i, parent) == i) {
      g[0].push_back(make_pair(i, 0));
      g[i].push_back(make_pair(0, 0));
    }
  }
  dfs(0, 0, 0);

  tarjan(0);
  for (int i = 0; i < cnt_q; i++) {
    cout << ans[i] << endl;
  }
  return 0;
}
