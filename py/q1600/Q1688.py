"""
 * 给你一个整数 n ，表示比赛中的队伍数。比赛遵循一种独特的赛制：
 * 1、如果当前队伍数是 偶数 ，那么每支队伍都会与另一支队伍配对。总共进行 n / 2 场比赛，且产生 n / 2 支队伍进入下一轮。
 * 2、如果当前队伍数为 奇数 ，那么将会随机轮空并晋级一支队伍，其余的队伍配对。总共进行 (n - 1) / 2 场比赛，且产生 (n - 1) / 2 + 1 支队伍进入下一轮。
 * 返回在比赛中进行的配对次数，直到决出获胜队伍为止。
 * 提示：1 <= n <= 200
 * 链接：https://leetcode.cn/problems/count-of-matches-in-tournament
"""

#
# @lc app=leetcode.cn id=1688 lang=python3
#
# [1688] 比赛中的配对次数
#


# @lc code=start
class Solution:

    def numberOfMatches(self, n: int) -> int:
        return n - 1  # 输的队伍无法晋级、只有一支队伍获胜，所以n-1场比赛


# @lc code=end

if __name__ == '__main__':
    # 6
    print(Solution().numberOfMatches(7))
    # 13
    print(Solution().numberOfMatches(14))
