"""
 * 给你一个长度为 n 的整数数组 score ，其中 score[i] 是第 i 位运动员在比赛中的得分。所有得分都 互不相同 。
 * 运动员将根据得分 决定名次 ，其中名次第 1 的运动员得分最高，名次第 2 的运动员得分第 2 高，依此类推。
 * 运动员的名次决定了他们的获奖情况：
 * 1、名次第 1 的运动员获金牌 "Gold Medal" 。
 * 2、名次第 2 的运动员获银牌 "Silver Medal" 。
 * 3、名次第 3 的运动员获铜牌 "Bronze Medal" 。
 * 4、从名次第 4 到第 n 的运动员，只能获得他们的名次编号（即，名次第 x 的运动员获得编号 "x"）。
 * 使用长度为 n 的数组 answer 返回获奖，其中 answer[i] 是第 i 位运动员的获奖情况。
 * 提示：
 * 1、n == score.length
 * 2、1 <= n <= 10^4
 * 3、0 <= score[i] <= 10^6
 * 4、score 中的所有值 互不相同
 * 链接：https://leetcode.cn/problems/relative-ranks
"""

from typing import List

#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#


# @lc code=start
class Solution:

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ss = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        n = len(score)
        ans = [''] * n
        for ii, s in enumerate(sorted([[s, i] for i, s in enumerate(score)], reverse=True)):
            ans[s[1]] = ss[ii] if ii < 3 else str(ii + 1)
        return ans


# @lc code=end

if __name__ == '__main__':
    # ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
    print(Solution().findRelativeRanks([5, 4, 3, 2, 1]))
    # ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
    print(Solution().findRelativeRanks([10, 3, 8, 9, 4]))
