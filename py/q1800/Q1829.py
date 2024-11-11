"""
 * 给你一个 有序 数组 nums ，它由 n 个非负整数组成，同时给你一个整数 maximumBit 。
 * 你需要执行以下查询 n 次：
 * 1、找到一个非负整数 k < 2maximumBit ，使得 
 *      nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k 的结果 最大化 。
 *      k 是第 i 个查询的答案。
 * 2、从当前数组 nums 删除 最后 一个元素。
 * 请你返回一个数组 answer ，其中 answer[i]是第 i 个查询的结果。
 * 提示：
 * 1、nums.length == n
 * 2、1 <= n <= 10^5
 * 3、1 <= maximumBit <= 20
 * 4、0 <= nums[i] < 2maximumBit
 * 5、nums 中的数字已经按 升序 排好序。
 * 链接：https://leetcode.cn/problems/maximum-xor-for-each-query
"""

from functools import reduce
from operator import xor
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=1829 lang=python3
# @lcpr version=20003
#
# [1829] 每个查询的最大异或值
#

# @lc code=start


class Solution:

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        vv = reduce(xor, nums)
        ans = []
        for i in range(len(nums) - 1, -1, -1):
            val = 0
            for j in range(maximumBit):
                if 1 << j & vv == 0:
                    val += 1 << j
            ans.append(val)
            vv ^= nums[i]
        return ans


# @lc code=end

if __name__ == '__main__':
    # [0,3,2,3]
    print(Solution().getMaximumXor([0, 1, 1, 3], maximumBit=2))
    # [5,2,6,5]
    print(Solution().getMaximumXor([2, 3, 4, 7], maximumBit=3))
    # [4,3,6,4,6,7]
    print(Solution().getMaximumXor([0, 1, 2, 2, 5, 7], maximumBit=3))
