"""
 * 你有两个果篮，每个果篮中有 n 个水果。给你两个下标从 0 开始的整数数组 basket1 和 basket2 ，用以表示两个果篮中每个水果的成本。
 * 你希望两个果篮相等。为此，可以根据需要多次执行下述操作：
 * 1、选中两个下标 i 和 j ，并交换 basket1 中的第 i 个水果和 basket2 中的第 j 个水果。
 * 2、交换的成本是 min(basket1_i,basket2_j) 。
 * 根据果篮中水果的成本进行排序，如果排序后结果完全相同，则认为两个果篮相等。
 * 返回使两个果篮相等的最小交换成本，如果无法使两个果篮相等，则返回 -1 。
 * 提示：
 * 1、basket1.length == basket2.length
 * 2、1 <= basket1.length <= 10^5
 * 3、1 <= basket1_i,basket2_i <= 10^9
 * 链接：https://leetcode.cn/problems/rearranging-fruits/
"""
from typing import Counter, List


class Solution:

    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt1, cnt2 = Counter(basket1), Counter(basket2)
        cnt = cnt1 + cnt2
        for v in cnt.values():
            if v & 1: return -1
        tar = sorted([[v, c // 2] for v, c in cnt.items()])

        total = 0
        for v, c in tar:
            total += abs(cnt1[v] - c)

        ans = 0
        r = 0
        for v, c in tar:
            cc = min(total // 2 - r, abs(c - cnt1[v]))
            if v < tar[0][0] * 2:
                ans += v * cc
            else:
                ans += tar[0][0] * 2 * cc
            r += cc
            if r >= total // 2: break
        return ans


if __name__ == '__main__':
    # 48
    print(Solution().minCost([84, 80, 43, 8, 80, 88, 43, 14, 100, 88], basket2=[32, 32, 42, 68, 68, 100, 42, 84, 14, 8]))
    # 1
    print(Solution().minCost([4, 2, 2, 2], basket2=[1, 4, 1, 2]))
    # -1
    print(Solution().minCost([2, 3, 4, 1], basket2=[3, 2, 5, 1]))
