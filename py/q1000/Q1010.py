"""
 * 在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
 * 返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望下标数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。
 * 提示：
 * 1、1 <= time.length <= 6 * 10^4
 * 2、1 <= time[i] <= 500
 * 链接：https://leetcode.cn/problems/pairs-of-songs-with-total-durations-divisible-by-60/
"""
from collections import Counter
from typing import List


class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = Counter([v % 60 for v in time])
        ans = 0
        for v, c in cnt.items():
            if v != 30 and v != 0:
                ans += c * cnt[(60 - v) % 60]
        ans //= 2
        ans += cnt[30] * (cnt[30] - 1) // 2
        ans += cnt[0] * (cnt[0] - 1) // 2
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().numPairsDivisibleBy60([60, 60, 60]))
    # 3
    print(Solution().numPairsDivisibleBy60([30, 20, 150, 100, 40]))
