"""
 * 给你一个正整数数组 nums 和一个整数 k 。
 * 一次操作中，你可以将数组的最后一个元素删除，将该元素添加到一个集合中。
 * 请你返回收集元素 1, 2, ..., k 需要的 最少操作次数 。
 * 提示：
 * 1、1 <= nums.length <= 50
 * 2、1 <= nums[i] <= nums.length
 * 3、1 <= k <= nums.length
 * 4、输入保证你可以收集到元素 1, 2, ..., k 。
 * 链接：https://leetcode.cn/problems/minimum-operations-to-collect-elements/
"""
from typing import List


class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        s = set()
        i = len(nums) - 1
        while i >= 0 and len(s) < k:
            if nums[i] <= k: s.add(nums[i])
            i -= 1
        return len(nums) - i - 1


if __name__ == '__main__':
    # 4
    print(Solution().minOperations([3,1,5,4,2], k = 2))
    # 5
    print(Solution().minOperations([3, 1, 5, 4, 2], k=5))
    # 4
    print(Solution().minOperations([3,2,5,3,1], k = 3))