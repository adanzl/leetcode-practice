"""
 * 如果数组的每一对相邻元素都是两个奇偶性不同的数字，则该数组被认为是一个 特殊数组 。
 * 周洋哥有一个整数数组 nums 和一个二维整数矩阵 queries，对于 queries[i] = [from_i, to_i]，
 * 请你帮助周洋哥检查子数组 nums[from_i..to_i] 是不是一个 特殊数组 。
 * 返回布尔数组 answer，如果 nums[from_i..to_i] 是特殊数组，则 answer[i] 为 true ，否则，answer[i] 为 false 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 3、1 <= queries.length <= 10^5
 * 4、queries[i].length == 2
 * 5、0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
 * 链接：https://leetcode.cn/problems/special-array-ii/
"""
from typing import List


class Solution:

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = []
        p_sum = [0]
        v = nums[0] & 1
        for i in range(1, len(nums)):
            p_sum.append(p_sum[-1] + int(v == (nums[i] & 1)))
            v = nums[i] & 1
        for f, t in queries:
            ans.append(p_sum[t] - p_sum[f] == 0)
        return ans


if __name__ == '__main__':
    # [False]
    print(Solution().isArraySpecial([3, 4, 1, 2, 6], queries=[[0, 4]]))
    # [False, True]
    print(Solution().isArraySpecial([4, 3, 1, 6], queries=[[0, 2], [2, 3]]))
    #
    # print(Solution().isArraySpecial())
