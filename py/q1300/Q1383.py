"""
 * 给定两个整数 n 和 k，以及两个长度为 n 的整数数组 speed 和 efficiency。现有 n 名工程师，编号从 1 到 n。
 * 其中 speed[i] 和 efficiency[i] 分别代表第 i 位工程师的速度和效率。
 * 从这 n 名工程师中最多选择 k 名不同的工程师，使其组成的团队具有最大的团队表现值。
 * 团队表现值 的定义为：一个团队中「所有工程师速度的和」乘以他们「效率值中的最小值」。
 * 请你返回该团队的​​​​​​最大团队表现值，由于答案可能很大，请你返回结果对 10^9 + 7 取余后的结果。
 * 提示：
 * 1、1 <= k <= n <= 10^5
 * 2、speed.length == n
 * 3、efficiency.length == n
 * 4、1 <= speed[i] <= 10^5
 * 5、1 <= efficiency[i] <= 10^8
 * 链接：https://leetcode.cn/problems/maximum-performance-of-a-team/
"""

from heapq import heappop, heappush
from typing import List

#
# @lc app=leetcode.cn id=1383 lang=python3
#
# [1383] 最大的团队表现值
#


# @lc code=start
class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        ss = sorted([[e, s] for s, e in zip(speed, efficiency)], reverse=True)
        h, sm = [], 0
        for e, s in ss:
            heappush(h, s)
            sm += s
            if len(h) > k:
                sm -= heappop(h)
            ans = max(ans, e * sm)
        return ans % MOD


# @lc code=end

if __name__ == '__main__':
    # 60
    print(Solution().maxPerformance(6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=2))
    # 68
    print(Solution().maxPerformance(6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=3))
    # 72
    print(Solution().maxPerformance(6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=4))