"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
 * 你可以对数组执行 至多 k 次操作：
 * 从数组中选择一个下标 i ，将 nums[i] 增加 或者 减少 1 。
 * 最终数组的频率分数定义为数组中众数的 频率 。
 * 请你返回你可以得到的 最大 频率分数。
 * 众数指的是数组中出现次数最多的数。一个元素的频率指的是数组中这个元素的出现次数。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、0 <= k <= 10^14
 * 链接：https://leetcode.cn/problems/apply-operations-to-maximize-frequency-score/
"""
from itertools import accumulate
from typing import List


class Solution:

    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        pre_sm = [0] + list(accumulate(nums))
        l, r = 1, n
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            valid = False
            for i in range(mid - 1, n):
                nn = mid // 2
                num = nums[i - mid + 1 + nn]
                v1 = num * nn - (pre_sm[i - mid + nn + 1] - pre_sm[i - mid + 1])
                v2 = pre_sm[i + 1] - pre_sm[i + 1 - mid + nn] - num * (mid - nn)
                if v1 + v2 <= k:
                    valid = True
                    break
            if valid:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().maxFrequencyScore([1, 2, 6, 4], k=3))
    # 10
    print(Solution().maxFrequencyScore([3, 20, 13, 2, 3, 15, 24, 19, 8, 13, 19, 20, 21], 45))
    # 3
    print(Solution().maxFrequencyScore([1, 4, 4, 2, 4], k=0))
