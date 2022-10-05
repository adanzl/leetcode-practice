"""
 * 你的赛车可以从位置 0 开始，并且速度为 +1 ，在一条无限长的数轴上行驶。赛车也可以向负方向行驶。赛车可以按照由加速指令 'A' 和倒车指令 'R' 组成的指令序列自动行驶。
 * 1、当收到指令 'A' 时，赛车这样行驶：
 *  - position += speed
 *  - speed *= 2
 * 2、当收到指令 'R' 时，赛车这样行驶：
 *  - 如果速度为正数，那么speed = -1
 *  - 否则 speed = 1
 * 当前所处位置不变。
 * 例如，在执行指令 "AAR" 后，赛车位置变化为 0 --> 1 --> 3 --> 3 ，速度变化为 1 --> 2 --> 4 --> -1 。
 * 给你一个目标位置 target ，返回能到达目标位置的最短指令序列的长度。
 * 提示：1 <= target <= 10^4
 * 链接：https://leetcode.cn/problems/race-car/
"""


class Solution:

    def race_car(self, target: int) -> int:
        k = target.bit_length()
        inf = 0x3c3c3c3c
        dp = [inf for i in range(target + 1)]
        dp[0] = 0
        for i in range(1, target + 1):
            for j in range(1, k + 1):
                n = 2**j - 1
                if n > i:  # 超过 i 点 + 1 次转向
                    dp[i] = min(dp[i], dp[n - i] + j + 1)
                    break
                elif n == i:  # 到达 i 点
                    dp[i] = j
                    break
                else:  # 正向走j次未到达 i 点，尝试反向走x次，更新最优解
                    for x in range(j):
                        # m点的位置就是 (2**j - 1) - (2**x - 1), j 和 x 是分别正向和反向A指令数量， +2 是因为需要两次倒车指令
                        dp[i] = min(dp[i], dp[i - (n - (2**x - 1))] + j + 2 + x)
        return dp[-1]


if __name__ == '__main__':
    # 12
    print(Solution().race_car(20))
    # 45
    print(Solution().race_car(10000))
    # 5
    print(Solution().race_car(4))
    # 5
    print(Solution().race_car(6))
    # 2
    print(Solution().race_car(3))