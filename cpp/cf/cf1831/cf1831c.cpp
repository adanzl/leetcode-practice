/**
 * 链接：https://codeforces.com/contest/1831/problem/C
 */

#include <bits/stdc++.h>
#include <vector>
using namespace std;

const int NMAX = 2e5 + 5;
int dp[NMAX], id[NMAX];
vector<pair<int, int>> edg[NMAX];

void dfs(int u) {
    for (auto p : edg[u]) {
        if (dp[p.first] == 0) {
            dp[p.first] = dp[u] + (p.second <= id[u]);
            id[p.first] = p.second;
            dfs(p.first);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false); // 取消 cin 和 stdin 的同步
    int nCase;
    cin >> nCase;
    while (nCase--) {
        int n;
        cin >> n;
        for (int i = 0; i <= n; i++) {
            edg[i].clear();
            dp[i] = id[i] = 0;
        }
        for (int i = 1; i < n; i++) {
            int u, v;
            cin >> u >> v;
            edg[u].push_back({v, i});
            edg[v].push_back({u, i});
        }
        dp[1] = 1;
        dfs(1);
        int ans = 0;
        for (int i = 1; i <= n; i++)
            ans = max(ans, dp[i]);
        cout << ans << endl;
    }
    return 0;
}