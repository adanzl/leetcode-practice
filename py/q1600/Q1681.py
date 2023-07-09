"""
 * 给你一个整数数组 nums 和一个整数 k 。你需要将这个数组划分到 k 个相同大小的子集中，使得同一个子集里面没有两个相同的元素。
 * 一个子集的 不兼容性 是该子集里面最大值和最小值的差。
 * 请你返回将数组分成 k 个子集后，各子集 不兼容性 的 和 的 最小值 ，如果无法分成分成 k 个子集，返回 -1 。
 * 子集的定义是数组中一些数字的集合，对数字顺序没有要求。
 * 提示：
 * 1、1 <= k <= nums.length <= 16
 * 2、nums.length 能被 k 整除。
 * 3、1 <= nums[i] <= nums.length
 * 链接：https://leetcode.cn/problems/minimum-incompatibility/
"""
from collections import Counter
from functools import cache
from typing import List


class Solution:

    def minimumIncompatibility(self, a: List[int], k: int) -> int:
        if any(c > k for c in Counter(a).values()):  # 鸽巢原理
            return -1
        inf = 10**10
        n = len(a)
        size = n // k
        a.sort()  # 排序，便于判断重复

        @cache
        def dfs(left: int, pre: int) -> int:
            if left == 0: return 0
            if left.bit_count() % size == 0:  # 创建一个新的组
                lb = left & -left  # 选择 low_bit 作为第一个数
                return dfs(left ^ lb, lb.bit_length() - 1)
            res = inf
            last = a[pre]
            for i in range(pre + 1, n):  # 枚举这个组的下一个数
                if left >> i & 1 and a[i] != last:  # 组内不能有重复数字，且 a 中重复数字只需枚举一次
                    last = a[i]
                    res = min(res, last - a[pre] + dfs(left ^ (1 << i), i))
            return res

        return dfs((1 << n) - 2, 0)


if __name__ == '__main__':
    # 4
    print(Solution().minimumIncompatibility([1, 2, 1, 4], k=2))
    # 6
    print(Solution().minimumIncompatibility([6, 3, 8, 1, 3, 1, 2, 2], k=4))
    # -1
    print(Solution().minimumIncompatibility([5, 3, 3, 6, 3, 3], k=3))
