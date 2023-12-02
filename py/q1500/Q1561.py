"""
 * 有 3n 堆数目不一的硬币，你和你的朋友们打算按以下方式分硬币：
 * 1、每一轮中，你将会选出 任意 3 堆硬币（不一定连续）。
 * 2、Alice 将会取走硬币数量最多的那一堆。
 * 3、你将会取走硬币数量第二多的那一堆。
 * 4、Bob 将会取走最后一堆。
 * 5、重复这个过程，直到没有更多硬币。
 * 给你一个整数数组 piles ，其中 piles[i] 是第 i 堆中硬币的数目。
 * 返回你可以获得的最大硬币数目。
 * 提示：
 * 1、3 <= piles.length <= 10^5
 * 2、piles.length % 3 == 0
 * 3、1 <= piles[i] <= 10^4
 * 链接：https://leetcode.cn/problems/maximum-number-of-coins-you-can-get
"""

from typing import List

#
# @lc app=leetcode.cn id=1561 lang=python3
#
# [1561] 你可以获得的最大硬币数目
#


# @lc code=start
class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles, reverse=True)[1:len(piles) // 3 * 2:2])


# @lc code=end

if __name__ == '__main__':
    # 9
    print(Solution().maxCoins([2, 4, 1, 2, 7, 8]))
    # 4
    print(Solution().maxCoins([2, 4, 5]))
    # 18
    print(Solution().maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]))
