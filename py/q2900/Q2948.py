"""
 * 给你一个下标从 0 开始的 正整数 数组 nums 和一个 正整数 limit 。
 * 在一次操作中，你可以选择任意两个下标 i 和 j，
 * 如果 满足 |nums[i] - nums[j]| <= limit ，则交换 nums[i] 和 nums[j] 。
 * 返回执行任意次操作后能得到的 字典序最小的数组 。
 * 如果在数组 a 和数组 b 第一个不同的位置上，数组 a 中的对应元素比数组 b 中的对应元素的字典序更小，
 * 则认为数组 a 就比数组 b 字典序更小。例如，数组 [2,10,3] 比数组 [10,2,3] 字典序更小，
 * 下标 0 处是两个数组第一个不同的位置，且 2 < 10 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、1 <= limit <= 10^9
 * 链接：https://leetcode.cn/problems/make-lexicographically-smallest-array-by-swapping-elements/
"""

import bisect
from collections import defaultdict
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=2948 lang=python3
#
# [2948] 交换得到字典序最小的数组
#


# @lc code=start
class Solution:

    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        ans = []
        n = len(nums)
        parent = [i for i in range(n)]
        def find(x):
            r = x
            while parent[r] != r:
                r = parent[r]
            while parent[x] != r:
                parent[x], x = r, parent[x]
            return r
        ss =  sorted([[num, i] for i, num in enumerate(nums)])
        for i in range(n-1):
            if abs(ss[i][0] - ss[i + 1][0]) <= limit :
                r0, r1 = find(ss[i][1]), find(ss[i+1][1])
                parent[r1] = r0
        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[find(i)].append(num)
        for v in d.values():
            v.sort()
        for i in range(n):
            ans.append(d[find(i)].pop(0))
        return ans


# @lc code=end

if __name__ == '__main__':
    # [1,56,34,84,60,62,38,76,49,39]
    print(Solution().lexicographicallySmallestArray([1, 60, 34, 84, 62, 56, 39, 76, 49, 38], 4))
    # [1,3,5,8,9]
    print(Solution().lexicographicallySmallestArray([1, 5, 3, 9, 8], limit=2))
    # [1,6,7,18,1,2]
    print(Solution().lexicographicallySmallestArray([1, 7, 6, 18, 2, 1], limit=3))
    # [1,7,28,19,10]
    print(Solution().lexicographicallySmallestArray([1, 7, 28, 19, 10], limit=3))
