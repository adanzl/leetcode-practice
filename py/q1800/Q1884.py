"""
 * 给你 2 枚相同 的鸡蛋，和一栋从第 1 层到第 n 层共有 n 层楼的建筑。
 * 已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都 会碎 ，从 f 楼层或比它低 的楼层落下的鸡蛋都 不会碎 。
 * 每次操作，你可以取一枚 没有碎 的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。
 * 如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。
 * 请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？
 * 提示：1 <= n <= 1000
 * 链接：https://leetcode.cn/problems/egg-drop-with-2-eggs-and-n-floors/
"""


class Solution:

    def twoEggDrop(self, n: int) -> int:
        # dp[i][j] 表示有 i + 1 枚鸡蛋时，验证 j 层楼需要的最少操作次数, dp[0][j] = j
        # 第一次操作可以选择在 [1, i] 范围内的任一楼层 k，如果鸡蛋破碎，接下来问题转化成 i = 0 时验证 k - 1 层需要的次数，总操作次数为 dp[0][k - 1] + 1；
        # 如果鸡蛋在 k 层丢下后没碎，接下来问题转化成 i = 1 时验证 j - k 层需要的次数， 即 dp[1][j - k], 总操作次数为 dp[1][j - k] + 1
        # 考虑最坏的情况，两者取最大值则有 dp[1][j] = min(dp[1][j], max(dp[0][k - 1] + 1, dp[1][j - k] + 1))
        dp = [n] * (n + 1)  # 2枚鸡蛋验证 n 层楼需要的最少操作次数
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):  # 第一枚扔到第 j 层
                dp[i] = min(dp[i], max(j, dp[i - j] + 1))
        return dp[n]


if __name__ == '__main__':
    # 2
    print(Solution().twoEggDrop(2))
    # 14
    print(Solution().twoEggDrop(100))