"""
 * 给你一个下标从 0 开始长度为 n 的整数数组 nums 和一个整数 target ，请你返回满足 0 <= i < j < n 且 nums[i] + nums[j] < target 的下标对 (i, j) 的数目。
 * 提示：
 * 1、1 <= nums.length == n <= 50
 * 2、-50 <= nums[i], target <= 50
 * 链接：https://leetcode.cn/problems/count-pairs-whose-sum-is-less-than-target/
"""
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().countPairs( [-1,1,2,3,1], target = 2))
    # 10
    print(Solution().countPairs([-6,2,5,-2,-7,-1,3], target = -2))