"""
 * 给你一个长度为 n 的整数数组 nums，以及一个正整数 k 。
 * 将这个数组划分为一个或多个长度为 3 的子数组，并满足以下条件：
 * 1、nums 中的 每个 元素都必须 恰好 存在于某个子数组中。
 * 2、子数组中 任意 两个元素的差必须小于或等于 k 。
 * 返回一个 二维数组 ，包含所有的子数组。如果不可能满足条件，就返回一个空数组。如果有多个答案，返回 任意一个 即可。
 * 提示：
 * 1、n == nums.length
 * 2、1 <= n <= 10^5
 * 3、n 是 3 的倍数
 * 4、1 <= nums[i] <= 10^5
 * 5、1 <= k <= 10^5
 * 链接：https://leetcode.cn/problems/divide-array-into-arrays-with-max-difference
"""
from typing import List


class Solution:

    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        i = 0
        n = len(nums)
        nums.sort()
        while i < n:
            if nums[i + 2] - nums[i] <= k:
                ans.append(nums[i:i + 3])
            else:
                return []
            i += 3
        return ans


if __name__ == '__main__':
    # [[1,1,3],[3,4,5],[7,8,9]]
    print(Solution().divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], k=2))
    # []
    print(Solution().divideArray([1, 3, 3, 2, 7, 3], k=3))
