"""
 * 给你一个整数数组 hours，表示以 小时 为单位的时间，返回一个整数，表示满足 i < j 且 hours[i] + hours[j] 构成 整天 的下标对 i, j 的数目。
 * 整天 定义为时间持续时间是 24 小时的 整数倍 。
 * 例如，1 天是 24 小时，2 天是 48 小时，3 天是 72 小时，以此类推。
 * 提示：
 * 1、1 <= hours.length <= 5 * 10^5
 * 2、1 <= hours[i] <= 10^9
 * 链接：https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-ii/
"""
from typing import Counter, List


class Solution:

    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        cnt = Counter()
        for h in hours:
            ans += cnt[(24 - h % 24) % 24]
            cnt[h % 24] += 1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().countCompleteDayPairs([12, 12, 30, 24, 24]))
    # 3
    print(Solution().countCompleteDayPairs([72, 48, 24, 3]))
