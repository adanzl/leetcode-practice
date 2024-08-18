"""
 * 给你一个长度为 n 的整数数组 nums 和一个正整数 k 。
 * 一个数组的 能量值 定义为：
 * 1、如果 所有 元素都是依次 连续 且 上升 的，那么能量值为 最大 的元素。
 * 2、否则为 -1 。
 * 你需要求出 nums 中所有长度为 k 的 子数组 的能量值。
 * 请你返回一个长度为 n - k + 1 的整数数组 results ，其中 results[i] 是子数组 nums[i..(i + k - 1)] 的能量值。
 * 提示：
 * 1、1 <= n == nums.length <= 500
 * 2、1 <= nums[i] <= 10^5
 * 3、1 <= k <= n
 * 链接：https://leetcode.cn/problems/find-the-power-of-k-size-subarrays-i/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []

        for i in range(len(nums) - k + 1):
            valid = True
            for j in range(i + 1, i + k):
                if nums[j] != nums[j - 1] + 1:
                    valid = False
                    break
            ans.append(nums[i + k - 1] if valid else -1)
        return ans


if __name__ == '__main__':
    # [-1,4]
    print(Solution().resultsArray([1, 3, 4], 2))
    # [3,4,-1,-1,-1]
    print(Solution().resultsArray([1, 2, 3, 4, 3, 2, 5], k=3))
    # [-1,-1]
    print(Solution().resultsArray([2, 2, 2, 2, 2], k=4))
    # [-1,3,-1,3,-1]
    print(Solution().resultsArray([3, 2, 3, 2, 3, 2], k=2))
