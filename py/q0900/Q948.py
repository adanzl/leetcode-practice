"""
 * 你的初始 能量 为 power，初始 分数 为 0，只有一包令牌以整数数组 tokens 给出。其中 tokens[i] 是第 i 个令牌的值（下标从 0 开始）。
 * 你的目标是通过有策略地使用这些令牌以 最大化 总 分数。在一次行动中，你可以用两种方式中的一种来使用一个 未被使用的 令牌（但不是对同一个令牌使用两种方式）：
 * 1、朝上：如果你当前 至少 有 tokens[i] 点 能量 ，可以使用令牌 i ，失去 tokens[i] 点 能量 ，并得到 1 分 。
 * 2、朝下：如果你当前至少有 1 分 ，可以使用令牌 i ，获得 tokens[i] 点 能量 ，并失去 1 分 。
 * 在使用 任意 数量的令牌后，返回我们可以得到的最大 分数 。
 * 提示：
 * 1、0 <= tokens.length <= 1000
 * 2、0 <= tokens[i], power < 10^4
 * 链接：https://leetcode.cn/problems/bag-of-tokens
"""

from typing import List

#
# @lc app=leetcode.cn id=948 lang=python3
#
# [948] 令牌放置
#


# @lc code=start
class Solution:

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        if len(tokens) == 0: return 0
        ans = 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            while l <= r and tokens[l] <= power:
                power -= tokens[l]
                l += 1
                ans += 1
            if r - l > 0 and ans > 0:
                ans -= 1
                power += tokens[r]
                r -= 1
            else:
                break
        return ans


# @lc code=end

if __name__ == '__main__':
    # 0
    print(Solution().bagOfTokensScore([100], power=50))
    # 1
    print(Solution().bagOfTokensScore([200, 100], power=150))
    # 2
    print(Solution().bagOfTokensScore([100, 200, 300, 400], power=200))
