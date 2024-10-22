"""
 * 给你一个长度为 n 的 质数 数组 nums 。你的任务是返回一个长度为 n 的数组 ans ，对于每个下标 i ，以下 条件 均成立：
 * ans[i] OR (ans[i] + 1) == nums[i]
 * 除此以外，你需要 最小化 结果数组里每一个 ans[i] 。
 * 如果没法找到符合 条件 的 ans[i] ，那么 ans[i] = -1 。
 * 质数 指的是一个大于 1 的自然数，且它只有 1 和自己两个因数。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、2 <= nums[i] <= 1000
 * 3、nums[i] 是一个质数。
 * 链接：https://leetcode.cn/problems/construct-the-minimum-bitwise-array-i/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            c = 0
            while 1 << c & num:
                c += 1
            if c:
                ans.append(num - (1 << (c - 1)))
            else:
                ans.append(-1)
        return ans


if __name__ == '__main__':
    # [-1,1,4,3]
    print(Solution().minBitwiseArray([2, 3, 5, 7]))
    # [9,12,15]
    print(Solution().minBitwiseArray([11, 13, 31]))
    # [-1,1,4,3]
    print(Solution().minBitwiseArray([2, 3, 5, 7]))
