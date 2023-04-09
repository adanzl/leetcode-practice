"""
 * 给你一个整数数组 nums 。请你创建一个满足以下条件的二维数组：
 * 1、二维数组应该 只 包含数组 nums 中的元素。
 * 2、二维数组中的每一行都包含 不同 的整数。
 * 3、二维数组的行数应尽可能 少 。
 * 返回结果数组。如果存在多种答案，则返回其中任何一种。
 * 请注意，二维数组的每一行上可以存在不同数量的元素。
 * 提示：
 * 1、1 <= nums.length <= 200
 * 2、1 <= nums[i] <= nums.length
 * 链接：https://leetcode.cn/problems/convert-an-array-into-a-2d-array-with-conditions/
"""
from typing import List


class Solution:

    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for num in nums:
            for s in ans:
                if num not in s:
                    s.append(num)
                    break
            else:
                ans.append([num])
        return ans


if __name__ == '__main__':
    # [[1,3,4,2],[1,3],[1]]
    print(Solution().findMatrix([1, 3, 4, 1, 2, 3, 1]))
    # [[4,3,2,1]]
    print(Solution().findMatrix([1, 2, 3, 4]))
