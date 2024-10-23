"""
 * 给你一个由 n 个整数组成的数组 nums，以及两个整数 k 和 x。
 * 数组的 x-sum 计算按照以下步骤进行：
 * 1、统计数组中所有元素的出现次数。
 * 2、仅保留出现次数最多的前 x 个元素的每次出现。如果两个元素的出现次数相同，则数值 较大 的元素被认为出现次数更多。
 * 3、计算结果数组的和。
 * 注意，如果数组中的不同元素少于 x 个，则其 x-sum 是数组的元素总和。
 * 返回一个长度为 n - k + 1 的整数数组 answer，其中 answer[i] 是 子数组 nums[i..i + k - 1] 的 x-sum。
 * 子数组 是数组内的一个连续 非空 的元素序列。
 * 提示：
 * 1、1 <= n == nums.length <= 50
 * 2、1 <= nums[i] <= 50
 * 3、1 <= x <= k <= nums.length
 * 链接：https://leetcode.cn/problems/find-x-sum-of-all-k-long-subarrays-i
"""
from typing import Counter, List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt = Counter()
        ans = []
        for i, num in enumerate(nums):
            cnt[num] += 1
            if i >= k:
                cnt[nums[i - k]] -= 1
            if i >= k - 1:
                ss = sorted([[c, v] for v, c in cnt.items()], reverse=True)
                ans.append(0)
                for j in range(min(x, len(ss))):
                    ans[-1] += ss[j][0] * ss[j][1]
        return ans


if __name__ == '__main__':
    # [13]
    print(Solution().findXSum([9, 2, 2], 3, 3))
    # [6,10,12]
    print(Solution().findXSum([1, 1, 2, 2, 3, 4, 2, 3], k=6, x=2))
    # [11,15,15,15,12]
    print(Solution().findXSum([3, 8, 7, 8, 7, 5], k=2, x=2))
