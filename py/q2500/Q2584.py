"""
 * 给你一个长度为 n 的整数数组 nums ，下标从 0 开始。
 * 如果在下标 i 处 分割 数组，其中 0 <= i <= n - 2 ，使前 i + 1 个元素的乘积和剩余元素的乘积互质，则认为该分割 有效 。
 * 例如，如果 nums = [2, 3, 3] ，那么在下标 i = 0 处的分割有效，因为 2 和 9 互质，而在下标 i = 1 处的分割无效，因为 6 和 3 不互质。
 * 在下标 i = 2 处的分割也无效，因为 i == n - 1 。
 * 返回可以有效分割数组的最小下标 i ，如果不存在有效分割，则返回 -1 。
 * 当且仅当 gcd(val1, val2) == 1 成立时，val1 和 val2 这两个值才是互质的，其中 gcd(val1, val2) 表示 val1 和 val2 的最大公约数。
 * 提示：
 * 1、n == nums.length
 * 2、1 <= n <= 10^4
 * 3、1 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/split-the-array-to-make-coprime-products/
"""
from typing import List


class Solution:

    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)
        p_idx_map = dict()  # p_map[p] 表示质数 p 出现的最右下标
        p_map = []
        for i, num in enumerate(nums):
            p_map.append([1])
            p = 2
            while p * p <= num:
                if num % p == 0:
                    r = p_idx_map.get(p, 0)
                    p_idx_map[p] = max(r, i)
                    p_map[-1].append(p)
                    while num % p == 0:
                        num //= p
                else:
                    p += 1
            if num > 1:
                r = p_idx_map.get(num, 0)
                p_idx_map[num] = max(r, i)
                p_map[-1].append(num)
        arr = []
        r_mx_idx = 0
        for i in range(n):
            r_idx = max([p_idx_map.get(p, 0) for p in p_map[i]])
            if i and r_mx_idx < i:
                return i - 1
            r_mx_idx = max(r_mx_idx, r_idx)
            arr.append(r_idx)
        return -1

    def findValidSplit1(self, nums: List[int]) -> int:
        left = {}  # left[p] 表示质数 p 首次出现的下标
        right = [0] * len(nums)  # right[i] 表示左端点为 i 的区间的右端点的最大值

        def f(p: int, i: int) -> None:
            if p in left:
                right[left[p]] = i  # 记录左端点 l 对应的右端点的最大值
            else:
                left[p] = i  # 第一次遇到质数 p

        for i, x in enumerate(nums):
            d = 2
            while d * d <= x:  # 分解质因数
                if x % d == 0:
                    f(d, i)
                    x //= d
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1: f(x, i)
        max_r = 0
        for l, r in enumerate(right):
            if l > max_r:  # 最远可以遇到 max_r
                return max_r  # 也可以写 l-1
            max_r = max(max_r, r)
        return -1


if __name__ == '__main__':
    # -1
    print(Solution().findValidSplit([4, 7, 15, 8, 3, 5]))
    # 2
    print(Solution().findValidSplit([4, 7, 8, 15, 3, 5]))
