"""
 * 链接：https://www.acwing.com/problem/content/4730/
"""

# n1, n2, k1, k2 = 2, 1, 1, 10  # 1
# n1, n2, k1, k2 = 2, 3, 1, 2 # 5
# n1, n2, k1, k2 = 2 ,4, 1 ,1 # 0
# n1, n2, k1, k2 = 100, 100, 10, 10  # 950492
# n1,n2 <= 100 k1,k2 <= 10
n1, n2, k1, k2 = map(int, input().split())

# dp[i1][i2][j1][j2] i1个黑子，i2个白子，最后一个分组是j1个黑子，j2个白子的情况的下的方案数
dp = [[[[0] * 12 for _ in range(12)] for __ in range(105)] for ___ in range(105)]
MOD = 10**8
dp[0][0][0][0] = 1
for i1 in range(n1 + 1):
    for i2 in range(n2 + 1):
        for j1 in range(k1 + 1):
            for j2 in range(k2 + 1):
                v = dp[i1][i2][j1][j2]
                # 放黑子
                if j1 < k1:
                    dp[i1 + 1][i2][j1 + 1][0] += v
                # 放白子
                if j2 < k2:
                    dp[i1][i2 + 1][0][j2 + 1] += v
ans = 0
for i in range(k1 + 1):
    for j in range(k2 + 1):
        ans += dp[n1][n2][i][j]
print(ans % MOD)