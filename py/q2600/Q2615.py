"""
 * 给你一个下标从 0 开始的整数数组 nums 。现有一个长度等于 nums.length 的数组 arr 。
 * 对于满足 nums[j] == nums[i] 且 j != i 的所有 j ，arr[i] 等于所有 |i - j| 之和。如果不存在这样的 j ，则令 arr[i] 等于 0 。
 * 返回数组 arr 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/sum-of-distances/
"""
from typing import List


class Solution:

    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ids = dict()
        pre_sm = dict()
        for i, v in enumerate(nums):
            ids.setdefault(v, {})
            ids[v][i] = len(ids[v])
            pre_sm.setdefault(v, [0])
            pre_sm[v].append(pre_sm[v][-1] + i)
        for i, v in enumerate(nums):
            ii = ids[v][i]
            ans[i] = (i * ii - pre_sm[v][ii]) + pre_sm[v][-1] - pre_sm[v][ii + 1] - (len(ids[v]) - ii - 1) * i
        return ans


if __name__ == '__main__':
    # [5,0,3,4,0]
    print(Solution().distance([1, 3, 1, 1, 2]))
    # [0,0,0]
    print(Solution().distance([0, 5, 3]))
