"""
 * 给你一个下标从 0 开始的整数数组 stones ，数组中的元素 严格递增 ，表示一条河中石头的位置。
 * 一只青蛙一开始在第一块石头上，它想到达最后一块石头，然后回到第一块石头。同时每块石头 至多 到达 一次。
 * 一次跳跃的 长度 是青蛙跳跃前和跳跃后所在两块石头之间的距离。
 * 更正式的，如果青蛙从 stones[i] 跳到 stones[j] ，跳跃的长度为 |stones[i] - stones[j]| 。
 * 一条路径的 代价 是这条路径里的 最大跳跃长度 。
 * 请你返回这只青蛙的 最小代价 。
 * 提示：
 * 1、2 <= stones.length <= 10^5
 * 2、0 <= stones[i] <= 10^9
 * 3、stones[0] == 0
 * 4、stones 中的元素严格递增。
 * 链接：https://leetcode.cn/problems/frog-jump-ii/
"""
from typing import List


class Solution:

    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        i1, i2 = 0, 0
        ans = 0
        for i in range(1, n):
            ans = max(ans, stones[i] - stones[i1])
            i1 += 1
            i += 1
            if i > n - 1:
                ans = max(ans, stones[-1] - stones[i2])
                break
            ans = max(ans, stones[i] - stones[i2])
            i2 += 1
        return ans


if __name__ == '__main__':
    # 5
    print(Solution().maxJump([0, 2, 5, 6, 7]))
    # 9
    print(Solution().maxJump([0, 3, 9]))
    #
    # print(Solution().maxJump( [0,2,5,6,7]))