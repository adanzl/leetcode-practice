"""
 * 给你一个下标从 0 开始的整数数组 nums 。在一步操作中，你可以执行以下步骤：
 * 1、从 nums 选出 两个 相等的 整数
 * 2、从 nums 中移除这两个整数，形成一个 数对
 * 请你在 nums 上多次执行此操作直到无法继续执行。
 * 返回一个下标从 0 开始、长度为 2 的整数数组 answer 作为答案，其中 answer[0] 是形成的数对数目，answer[1] 是对 nums 尽可能执行上述操作后剩下的整数数目。
 * 链接：https://leetcode.cn/problems/maximum-number-of-pairs-in-array
"""
from collections import Counter
from typing import List


class Solution:

    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ret = [0, 0]
        cnt = Counter(nums)
        for c in cnt.values():
            ret[0] += c // 2
            ret[1] += c % 2
        return ret


if __name__ == '__main__':
    # [3, 1]
    print(Solution().numberOfPairs([1, 3, 2, 1, 3, 2, 2]))
    # [1, 0]
    print(Solution().numberOfPairs([1, 1]))
    # [0, 1]
    print(Solution().numberOfPairs([0]))