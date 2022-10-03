"""
 * 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
 * 我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
 * 所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
 * 请你返回「表现良好时间段」的最大长度。
 * 提示：
 * 1 <= hours.length <= 10^4
 * 0 <= hours[i] <= 16
 * 链接：https://leetcode.cn/problems/longest-well-performing-interval/
"""

from typing import *


class Solution:

    def longestWPI(self, hours: List[int]) -> int:
        ans = 0
        pre_sum = 0
        idx_dic = dict()
        for i, h in enumerate(hours):
            pre_sum += 1 if h > 8 else -1
            if pre_sum > 0:
                ans = max(ans, i + 1)
            if idx_dic.__contains__(pre_sum - 1):
                ans = max(ans, i - idx_dic[pre_sum - 1])
            idx_dic.setdefault(pre_sum, i)
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().longestWPI([9, 9, 6, 0, 6, 6, 9]))
    # 0
    print(Solution().longestWPI([6, 6, 6]))
    # 1
    print(Solution().longestWPI([6, 6, 9]))
