"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
 * 如果子数组中所有元素都相等，则认为子数组是一个 等值子数组 。注意，空数组是 等值子数组 。
 * 从 nums 中删除最多 k 个元素后，返回可能的最长等值子数组的长度。
 * 子数组 是数组中一个连续且可能为空的元素序列。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= nums.length
 * 3、0 <= k <= nums.length
 * 链接：https://leetcode.cn/problems/find-the-longest-equal-subarray/
"""
import bisect
from typing import List


class Solution:

    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        arr = [[] for _ in range(n + 1)]  # [e_idx + 1, length, diff, pre_sum]
        ln, v = 0, 0
        ans = 0

        def update(i):
            nonlocal ans
            lst = [i - 1, 0, 0, 0] if not arr[v] else arr[v][-1]
            diff = i - lst[0] - ln + lst[2]
            sm = lst[3] + ln
            arr[v].append([i, ln, diff, sm])
            idx = bisect.bisect_left(arr[v], diff - k, key=lambda x: x[2])
            pre_sum = arr[v][idx - 1][3] if idx > 0 else 0
            return sm - pre_sum

        for i, num in enumerate(nums):
            if num == v:
                ln += 1
            else:
                ans = max(ans, update(i))
                ln, v = 1, num
        ans = max(ans, update(n))
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().longestEqualSubarray([1, 3, 2, 3, 1, 3], k=3))
    # 4
    print(Solution().longestEqualSubarray([1, 1, 2, 2, 1, 1], k=2))
