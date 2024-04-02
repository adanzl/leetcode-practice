"""
 * 给你一个 非负 整数数组 nums 和一个整数 k 。
 * 如果一个数组中所有元素的按位或运算 OR 的值 至少 为 k ，那么我们称这个数组是 特别的 。
 * 请你返回 nums 中 最短特别非空 子数组 的长度，如果特别子数组不存在，那么返回 -1 。
 * 提示：
 * 1、1 <= nums.length <= 2*10^5
 * 2、0 <= nums[i] <= 10^9
 * 3、0 <= k <= 10^9
 * 链接：https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/
"""
from typing import Counter, List


class Solution:

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0: return 1
        n = len(nums)
        LIMIT = 0x3c3c3c3c3c3c
        ans, n = LIMIT, len(nums)
        l, r = 0, 0
        cnt = Counter()
        d_v = 0

        while r < n:
            while r < n and d_v < k:
                for i in range(nums[r].bit_length()):
                    if 1 << i & nums[r]:
                        cnt[i] += 1
                        d_v |= 1 << i
                r += 1
            while l <= r and d_v >= k:
                for i in range(nums[l].bit_length()):
                    if 1 << i & nums[l]:
                        cnt[i] -= 1
                        if cnt[i] == 0:
                            del cnt[i]
                            d_v &= ~(1 << i)
                ans = min(ans, r - l)
                l += 1
        return ans if ans != LIMIT else -1


if __name__ == '__main__':
    # 1
    print(Solution().minimumSubarrayLength([2, 3], k=1))
    # 1
    print(Solution().minimumSubarrayLength([1, 2], k=0))
    # 1
    print(Solution().minimumSubarrayLength([1, 2, 3], k=3))
    # -1
    print(Solution().minimumSubarrayLength([1, 12, 2, 5], 43))
    # 1
    print(Solution().minimumSubarrayLength([2, 24, 32, 1], 11))
    # 3
    print(Solution().minimumSubarrayLength([2, 1, 8], k=10))
