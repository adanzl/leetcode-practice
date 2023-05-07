"""
 * 给你一个长度为 n 的整数数组 nums ，请你求出每个长度为 k 的子数组的 美丽值 。
 * 一个子数组的 美丽值 定义为：如果子数组中第 x 小整数 是 负数 ，那么美丽值为第 x 小的数，否则美丽值为 0 。
 * 请你返回一个包含 n - k + 1 个整数的数组，依次 表示数组中从第一个下标开始，每个长度为 k 的子数组的 美丽值 。
 * 子数组指的是数组中一段连续 非空 的元素序列。
 * 提示：
 * 1、n == nums.length 
 * 2、1 <= n <= 10^5
 * 3、1 <= k <= n
 * 4、1 <= x <= k 
 * 5、-50 <= nums[i] <= 50 
 * 链接：https://leetcode.cn/problems/sliding-subarray-beauty/
"""
from typing import List
from sortedcontainers import SortedList


class Solution:

    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        st = SortedList()
        n = len(nums)
        ans = []
        for i in range(k):
            st.add(nums[i])
        for i in range(k, n):
            ans.append(min(st[x - 1], 0))
            st.discard(nums[i - k])
            st.add(nums[i])
        ans.append(min(st[x - 1], 0))
        return ans


if __name__ == '__main__':
    # [-1,-2,-2]
    print(Solution().getSubarrayBeauty([1, -1, -3, -2, 3], k=3, x=2))
    # [-1,-2,-3,-4]
    print(Solution().getSubarrayBeauty([-1, -2, -3, -4, -5], k=2, x=2))
    # [-3,0,-3,-3,-3]
    print(Solution().getSubarrayBeauty([-3, 1, 2, -3, 0, -3], k=2, x=1))
