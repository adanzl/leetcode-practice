"""
 * 给你一个整数数组 nums ，你可以在 nums 上执行下述操作 任意次 ：
 * 如果 gcd(nums[i], nums[j]) > 1 ，交换 nums[i] 和 nums[j] 的位置。
 * 其中 gcd(nums[i], nums[j]) 是 nums[i] 和 nums[j] 的最大公因数。
 * 如果能使用上述交换方式将 nums 按 非递减顺序 排列，返回 true ；否则，返回 false 。
 * 提示：
 * 1、1 <= nums.length <= 3 * 10^4
 * 2、2 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/gcd-sort-of-an-array/
"""

from functools import cache
from itertools import pairwise
from typing import List

#
# @lc app=leetcode.cn id=1998 lang=python3
#
# [1998] 数组的最大公因数排序
#


# @lc code=start
class Solution:

    def gcdSort(self, nums: List[int]) -> bool:
        n = max(nums)
        parent = [i for i in range(n + 5)]

        @cache
        def prime_map(x):
            # 分解质因数
            p, num, p_map = 2, x, {}
            while p * p <= num:
                if num % p == 0:
                    x = 0
                    while num % p == 0:
                        num //= p
                        x += 1
                    p_map[p] = p_map.get(p, 0) + x
                else:
                    p += 1
            if num > 1:
                p_map[num] = 1
            return p_map

        def find(x):
            if parent[x] == x: return x
            parent[x] = find(parent[x])
            return parent[x]

        for i, num in enumerate(nums):
            m = prime_map(num)
            for pa, pb in pairwise(m.keys()):
                r0, r1 = find(pa), find(pb)
                parent[r0] = r1
        arr = sorted([[num, i] for i, num in enumerate(nums)])
        for i, [num, idx] in enumerate(arr):
            v0, v1 = list(prime_map(num).keys())[0], list(prime_map(nums[i]).keys())[0]
            if find(v0) != find(v1):
                return False
        return True


# @lc code=end

if __name__ == '__main__':
    # True
    print(Solution().gcdSort([7, 21, 3]))
    # False
    print(Solution().gcdSort([5, 2, 6, 2]))
    # True
    print(Solution().gcdSort([10, 5, 9, 3, 15]))
