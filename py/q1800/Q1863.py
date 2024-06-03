"""
 * 一个数组的 异或总和 定义为数组中所有元素按位 XOR 的结果；如果数组为 空 ，则异或总和为 0 。
 * 例如，数组 [2,5,6] 的 异或总和 为 2 XOR 5 XOR 6 = 1 。
 * 给你一个数组 nums ，请你求出 nums 中每个 子集 的 异或总和 ，计算并返回这些值相加之 和 。
 * 注意：在本题中，元素 相同 的不同子集应 多次 计数。
 * 数组 a 是数组 b 的一个 子集 的前提条件是：从 b 删除几个（也可能不删除）元素能够得到 a 。
 * 提示：
 * 1、1 <= nums.length <= 12
 * 2、1 <= nums[i] <= 20
 * 链接：https://leetcode.cn/problems/sum-of-all-subset-xor-totals
"""

from typing import List

#
# @lc app=leetcode.cn id=1863 lang=python3
#
# [1863] 找出所有子集的异或总和再求和
#

# @lc code=start
class Solution:

    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        def dfs(val, idx):
            nonlocal res
            if idx == n:
                # 终止递归
                res += val
                return
            # 考虑选择当前数字
            dfs(val ^ nums[idx], idx + 1)
            # 考虑不选择当前数字
            dfs(val, idx + 1)

        dfs(0, 0)
        return res
# @lc code=end



if __name__ == '__main__':
    # 6
    print(Solution().subsetXORSum([1,3]))
    # 28
    print(Solution().subsetXORSum([5,1,6]))
    # 480
    print(Solution().subsetXORSum([3,4,5,6,7,8]))
