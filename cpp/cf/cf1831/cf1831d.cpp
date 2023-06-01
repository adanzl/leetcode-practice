/**
 * 链接:https://codeforces.com/contest/1831/problem/D
 */
#include <bits/stdc++.h>
#include <iostream>
#include <vector>
using namespace std;
typedef long long LL;
const LL NMAX = 2e5 + 5, SQR_MAX = 635, MOD = 1e9 + 7;

int fr[SQR_MAX][NMAX];
LL a[NMAX], b[NMAX];

void test_case() {
    LL n, ans = 0;
    cin >> n;
    LL lim = sqrt(n * 2);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) {
        cin >> b[i];
        if (a[i] <= lim) fr[a[i]][b[i]]++;
    }
    for (LL i = 0; i < n; i++) {
        if (a[i] <= lim) {
            if (a[i] * a[i] - b[i] >= 1 && a[i] * a[i] - b[i] <= n) ans += fr[a[i]][a[i] * a[i] - b[i]];
        }
    }
    for (int i = 2; i <= lim; i += 2) { ans -= fr[i][i * i / 2]; }
    ans /= 2;

    for (int i = 0; i < n; i++) {
        for (int j = 1; j <= lim && j < a[i] && j * a[i] <= 2 * n; j++) {
            if (j * a[i] - b[i] >= 1 && j * a[i] - b[i] <= n) ans += fr[j][j * a[i] - b[i]];
        }
    }
    for (int i = 0; i < n; i++) {
        if (a[i] <= lim) fr[a[i]][b[i]] = 0;
    }
    cout << ans << endl;
}

int main() {
    ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    int t;
    cin >> t;
    while (t--) test_case();
    return 0;
}