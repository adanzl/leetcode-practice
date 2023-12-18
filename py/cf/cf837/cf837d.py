"""
 * PyPy 3-64
 * 链接：https://codeforces.com/problemset/problem/837/D
"""


class Solution:

    def func(self, nums, k):
        n = len(nums)
        dp = [[-1] * (k * 25 + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for num in nums:
            c2, c5 = bin(num ^ (num - 1)).count('1') - 1, 0
            while num % 5 == 0:
                c5 += 1
                num //= 5
            for i in range(k, 0, -1):
                for j in range(k * 25, c5 - 1, -1):
                    if dp[i - 1][j - c5] != -1:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j - c5] + c2)
        ans = 0
        for i, cnt2 in enumerate(dp[k]):
            ans = max(ans, min(i, cnt2))
        return ans


if __name__ == '__main__':
    # 3
    # print(Solution().func([50, 4, 20], 2))
    # # 3
    # print(Solution().func([15, 16, 3, 25, 9], 3))
    # # 0
    # print(Solution().func([9, 77, 13], 3))
    n, k = input("").split()
    print(Solution().func([int(_) for _ in input("").split()], int(k)))
