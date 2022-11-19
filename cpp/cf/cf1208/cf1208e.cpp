/**
 * 链接：https://codeforces.com/contest/1208/problem/E
 */

#include <bits/stdc++.h>
using namespace std;

#define LL long long
LL read() {
    LL sum = 0;
    char c = getchar();
    bool f = 0;
    while (c < '0' || c > '9') {
        if (c == '-')
            f = 1;
        c = getchar();
    }
    while (c >= '0' && c <= '9') {
        sum = sum * 10 + c - '0';
        c = getchar();
    }
    if (f)
        return -sum;
    return sum;
}
const int N = 1000005;
int n, w, l, S[N], q[N];
LL a[N], b[N];
int main() {
    n = read();
    w = read();
    int i, j, k, s, h, t, mx;
    for (i = 1; i <= n; i++) {
        l = read();
        mx = 0;
        for (j = 1; j <= l; j++)
            S[j] = read(), mx = max(mx, S[j]);
        h = 1;
        t = 0;
        k = max(w - l + 1, l + 1);
        for (j = 1; j <= l; j++) {
            while (h <= t && q[h] + (w - l) < j)
                h++;
            while (h <= t && S[j] >= S[q[t]])
                t--;
            q[++t] = j;
            if (S[q[h]] < 0 && j <= w - l)
                ;
            else
                a[j] += S[q[h]];
        }
        h = 1;
        t = 0;
        for (j = w; j >= k; j--) {
            s = j - (w - l);
            while (h <= t && q[h] > j)
                h++;
            while (h <= t && S[s] >= S[q[t]])
                t--;
            q[++t] = s;
            if (S[q[h]] < 0 && j > l)
                ;
            else
                a[j] += S[q[h]];
        }
        b[l + 1] += mx, b[k] -= mx;
    }
    LL R = 0;
    for (i = 1; i <= w; i++) {
        R += b[i];
        printf("%lld ", R + a[i]);
    }
    return 0;
}
