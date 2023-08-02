"""
 * 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
 * 提示：
 * 1、1 <= nums.length <= 6
 * 2、-10 <= nums[i] <= 10
 * 3、nums 中的所有整数 互不相同
 * 链接：https://leetcode.cn/problems/permutations/
"""
from itertools import permutations
from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(p) for p in permutations(nums)]


if __name__ == '__main__':
    # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(Solution().permute([1, 2, 3]))
    # [[0, 1], [1, 0]]
    print(Solution().permute([0, 1]))
    # [[1]]
    print(Solution().permute([1]))
