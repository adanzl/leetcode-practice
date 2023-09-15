"""
 * 给你一个下标从 0 开始长度为 n 的整数数组 stations ，其中 stations[i] 表示第 i 座城市的供电站数目。
 * 每个供电站可以在一定 范围 内给所有城市提供电力。换句话说，如果给定的范围是 r ，在城市 i 处的供电站可以给所有满足 |i - j| <= r 且 0 <= i, j <= n - 1 的城市 j 供电。
 * |x| 表示 x 的 绝对值 。比方说，|7 - 5| = 2 ，|3 - 10| = 7 。
 * 一座城市的 电量 是所有能给它供电的供电站数目。
 * 政府批准了可以额外建造 k 座供电站，你需要决定这些供电站分别应该建在哪里，这些供电站与已经存在的供电站有相同的供电范围。
 * 给你两个整数 r 和 k ，如果以最优策略建造额外的发电站，返回所有城市中，最小供电站数目的最大值是多少。
 * 这 k 座供电站可以建在多个城市。
 * 提示：
 * 1、n == stations.length
 * 2、1 <= n <= 10^5
 * 3、0 <= stations[i] <= 10^5
 * 4、0 <= r <= n - 1
 * 5、0 <= k <= 10^9
 * 链接：https://leetcode.cn/problems/maximize-the-minimum-powered-city/
"""

from typing import List

#
# @lc app=leetcode.cn id=2528 lang=python3
#
# [2528] 最大化城市的最小供电站数目
#


# @lc code=start
class Solution:

    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        diff = [0] * (n + 1)
        for i, v in enumerate(stations):
            diff[max(0, i - r)] += v
            diff[min(n, i + r + 1)] -= v

        def check(mn_v):
            sm, cnt = 0, 0
            dd = diff[:]
            for i in range(n):
                sm += dd[i]
                if sm < mn_v:
                    cnt += mn_v - sm
                    dd[i] += mn_v - sm
                    dd[min(n, i + r * 2 + 1)] -= mn_v - sm
                    if cnt > k: return False
                    sm = mn_v
            return True

        lp, rp = 0, 10**11
        ans = 0
        while lp <= rp:
            mid = lp + (rp - lp) // 2
            if check(mid):
                ans = mid
                lp = mid + 1
            else:
                rp = mid - 1
        return ans


# @lc code=end

if __name__ == '__main__':
    # 5
    print(Solution().maxPower([1, 2, 4, 5, 0], r=1, k=2))
    # 4
    print(Solution().maxPower([4, 4, 4, 4], r=0, k=3))