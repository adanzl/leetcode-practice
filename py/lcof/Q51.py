"""
 * 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
 * 限制：0 <= 数组长度 <= 50000
 * 链接：https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
"""
from bisect import bisect_left, bisect_right, insort_left
from typing import List


class BIT:

    def __init__(self, n):
        self.tree = [0] * n

    def add(self, i, val):
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i  # low_bit

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res


class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        # 树状数组
        b = sorted(nums)
        t = BIT(len(nums) + 1)
        ans = 0
        for i, num in enumerate(nums):
            idx = bisect_right(b, num)  # 离散化
            ans += i - t.query(idx)
            t.add(bisect_left(b, num) + 1, 1)
        return ans

    def reversePairs1(self, nums: List[int]) -> int:
        # 二分搜索
        a = []
        ans, n = 0, len(nums)
        for num in nums:
            ans += len(a) - bisect_right(a, num)
            insort_left(a, num)
        return ans


if __name__ == '__main__':
    # 5
    print(Solution().reversePairs([7, 5, 6, 4]))
    # 4
    print(Solution().reversePairs([1, 3, 2, 3, 1]))
