"""
 * 定义一个数组 arr 的 转换数组 convert 为：
 * convert[i] = arr[i] + max(arr[0..i])，其中 max(arr[0..i]) 是满足 0 <= j <= i 的所有 arr[j] 中的最大值。
 * 定义一个数组 arr 的 分数 为 arr 转换数组中所有元素的和。
 * 给你一个下标从 0 开始长度为 n 的整数数组 nums ，请你返回一个长度为 n 的数组 ans ，其中 ans[i]是前缀 nums[0..i] 的分数。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/find-the-score-of-all-prefixes-of-an-array/
"""
from typing import List


class Solution:

    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans = []
        mx = nums[0]
        for num in nums:
            mx = max(mx, num)
            c = num + mx
            ans.append((ans[-1] if ans else 0) + c)
        return ans


if __name__ == '__main__':
    # [4,10,24,36,56]
    print(Solution().findPrefixScore([2, 3, 7, 5, 10]))
    # [2,4,8,16,32,64]
    print(Solution().findPrefixScore([1, 1, 2, 4, 8, 16]))
