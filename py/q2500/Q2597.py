"""
 * 给你一个由正整数组成的数组 nums 和一个 正 整数 k 。
 * 如果 nums 的子集中，任意两个整数的绝对差均不等于 k ，则认为该子数组是一个 美丽 子集。
 * 返回数组 nums 中 非空 且 美丽 的子集数目。
 * nums 的子集定义为：可以经由 nums 删除某些元素（也可能不删除）得到的一个数组。只有在删除元素时选择的索引不同的情况下，两个子集才会被视作是不同的子集。
 * 提示：
 * 1、1 <= nums.length <= 20
 * 2、1 <= nums[i], k <= 1000
 * 链接：https://leetcode.cn/problems/the-number-of-beautiful-subsets/
"""
from collections import Counter, defaultdict
from typing import List


class Solution:

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        groups = defaultdict(Counter)
        for x in nums:
            groups[x % k][x] += 1
        ans = 1
        for cnt in groups.values():
            g = sorted(cnt.items())
            m = len(g)
            f = [0] * (m + 1)
            f[0] = 1
            f[1] = 1 << g[0][1]
            for i in range(1, m):
                if g[i][0] - g[i - 1][0] == k:
                    f[i + 1] = f[i] + f[i - 1] * ((1 << g[i][1]) - 1)
                else:
                    f[i + 1] = f[i] << g[i][1]
            ans *= f[m]
        return ans - 1  # -1 去掉空集


if __name__ == '__main__':
    # 4
    print(Solution().beautifulSubsets([2,4,6], k = 2))
    # 1
    print(Solution().beautifulSubsets([1], k=1))
