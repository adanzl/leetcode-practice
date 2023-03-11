"""
 * 给你一个正整数数组 nums 。
 * 如果数组 nums 的子集中的元素乘积是一个 无平方因子数 ，则认为该子集是一个 无平方 子集。
 * 无平方因子数 是无法被除 1 之外任何平方数整除的数字。
 * 返回数组 nums 中 无平方 且 非空 的子集数目。因为答案可能很大，返回对 10^9 + 7 取余的结果。
 * nums 的 非空子集 是可以由删除 nums 中一些元素（可以不删除，但不能全部删除）得到的一个数组。如果构成两个子集时选择删除的下标不同，则认为这两个子集不同。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、1 <= nums[i] <= 30
 * 链接：https://leetcode.cn/problems/count-the-number-of-square-free-subsets/
"""
from typing import List


class Solution:

    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def func(x):
            # 分解质因数
            p = 2
            num = x
            p_map = {}
            while p * p <= num:
                if num % p == 0:
                    x = 0
                    while num % p == 0:
                        num //= p
                        x += 1
                    p_map[p] = p_map.get(p, 0) + x
                else:
                    p += 1
            if num > 1:
                p_map[num] = 1
            return p_map

        arr = [0] * (2**10)
        PRIM = {2: 0, 3: 1, 5: 2, 7: 3, 11: 4, 13: 5, 17: 6, 19: 7, 23: 8, 29: 9}
        ans = 0
        for num in nums:
            p_map = func(num)
            n_arr = arr[:]
            if p_map and max(list(p_map.values())) > 1:
                continue
            ans += 1
            mask = 0
            for k in p_map.keys():
                mask |= 1 << PRIM[k]
            for i in range(2**10):
                if i & mask: continue
                ans = (ans + arr[i]) % MOD
                n_arr[i | mask] += (arr[i]) % MOD
            n_arr[mask] += 1
            arr = n_arr

        return ans


if __name__ == '__main__':
    # 3
    print(Solution().squareFreeSubsets([3, 4, 4, 5]))
    # 39
    print(Solution().squareFreeSubsets([8, 11, 17, 2, 25, 29, 21, 20, 4, 22]))
    # 1
    print(Solution().squareFreeSubsets([1]))