"""
 * 给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：
 * 1、子数组大小 至少为 2 ，
 * 2、且子数组元素总和为 k 的倍数。
 * 如果存在，返回 true ；否则，返回 false 。
 * 如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。0 始终视为 k 的一个倍数。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^9
 * 3、0 <= sum(nums[i]) <= 2^31 - 1
 * 4、1 <= k <= 2^31 - 1
 * 链接：https://leetcode.com/problems/continuous-subarray-sum
"""
from typing import List


class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 前缀和的差同余，记录某个余数最早出现的位置即可
        remain_map = dict({0: 0})  # pre_sum[i] % k - i
        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]
            r = pre_sum[i + 1] % k
            if r in remain_map:
                if i - remain_map[r] > 0: return True
            else:
                remain_map[r] = i + 1
        return False


if __name__ == '__main__':
    # true
    print(Solution().checkSubarraySum([1, 1], 1))
    # false
    print(Solution().checkSubarraySum([1, 2, 12], 6))
    # false
    print(Solution().checkSubarraySum([0, 5, 0], 3))
    # true
    print(Solution().checkSubarraySum([0, 0, 5, 0], 3))
    # false
    print(Solution().checkSubarraySum([1, 0], 2))
    # true
    print(Solution().checkSubarraySum([23, 2, 4, 6, 6], 7))
    # false
    print(Solution().checkSubarraySum([23, 2, 6, 4, 7], 13))
    # true
    print(Solution().checkSubarraySum([23, 2, 4, 6, 7], 6))
    # true
    print(Solution().checkSubarraySum([23, 2, 6, 4, 7], 6))
    # false
    print(Solution().checkSubarraySum([23, 2, 6, 4, 7], 1 << 31))
