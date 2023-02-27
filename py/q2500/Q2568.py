"""
 * 给你一个下标从 0 开始的整数数组 nums 。
 * 如果存在一些整数满足 0 <= index_1 < index_2 < ... < index_k < nums.length ，得到 nums[index_1] | nums[index_2] | ... | nums[index_k] = x ，
 * 那么我们说 x 是 可表达的 。换言之，如果一个整数能由 nums 的某个子序列的或运算得到，那么它就是可表达的。
 * 请你返回 nums 不可表达的 最小非零整数 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-impossible-or/
"""
from typing import List


class Solution:

    def minImpossibleOR(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for num in nums:
            if num > ans + 1:
                return ans + 1
            nn = num
            while nn:
                low = nn & -nn
                if low > ans + 1:
                    return ans + 1
                nn -= low
            ans |= num
        return ans + 1


if __name__ == '__main__':
    # 4
    print(Solution().minImpossibleOR([2, 1]))
    # 1
    print(Solution().minImpossibleOR([5, 3, 2]))
    # 64
    print(Solution().minImpossibleOR([4, 32, 16, 8, 8, 75, 1, 2]))
