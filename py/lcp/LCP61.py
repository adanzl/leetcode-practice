"""
 * 力扣城计划在两地设立「力扣嘉年华」的分会场，气象小组正在分析两地区的气温变化趋势，对于第 i ~ (i+1) 天的气温变化趋势，将根据以下规则判断：
 * 1、若第 i+1 天的气温 高于 第 i 天，为 上升 趋势
 * 2、若第 i+1 天的气温 等于 第 i 天，为 平稳 趋势
 * 3、若第 i+1 天的气温 低于 第 i 天，为 下降 趋势
 * 已知 temperatureA[i] 和 temperatureB[i] 分别表示第 i 天两地区的气温。
 * 组委会希望找到一段天数尽可能多，且两地气温变化趋势相同的时间举办嘉年华活动。请分析并返回两地气温变化趋势相同的最大连续天数。
 * 即最大的 n，使得第 i~i+n 天之间，两地气温变化趋势相同
 * 提示：
 * 1、2 <= temperatureA.length == temperatureB.length <= 1000
 * 2、-20 <= temperatureA[i], temperatureB[i] <= 40
 * 链接：https://leetcode.cn/problems/6CE719/
 * 链接：https://leetcode.cn/contest/season/2022-fall/problems/6CE719/
"""
from typing import *


class Solution:

    def temperatureTrend(self, ta: List[int], tb: List[int]) -> int:
        ans, pre = 0, 0
        for i in range(1, len(ta)):
            f1, f2 = ta[i] - ta[i - 1], tb[i] - tb[i - 1]
            f1 = 1 if f1 > 0 else -1 if f1 < 0 else 0
            f2 = 1 if f2 > 0 else -1 if f2 < 0 else 0
            if f1 == f2:
                pre += 1
            else:
                pre = 0
            ans = max(ans, pre)
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().temperatureTrend([21, 18, 18, 18, 31], [34, 32, 16, 16, 17]))
    # 3
    print(Solution().temperatureTrend([5, 10, 16, -6, 15, 11, 3], [16, 22, 23, 23, 25, 3, -16]))