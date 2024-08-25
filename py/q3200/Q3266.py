"""
 * 给你一个整数数组 nums ，一个整数 k  和一个整数 multiplier 。
 * 你需要对 nums 执行 k 次操作，每次操作中：
 * 1、找到 nums 中的 最小 值 x ，如果存在多个最小值，选择最 前面 的一个。
 * 2、将 x 替换为 x * multiplier 。
 * k 次操作以后，你需要将 nums 中每一个数值对 10^9 + 7 取余。
 * 请你返回执行完 k 次乘运算以及取余运算之后，最终的 nums 数组。
 * 提示：
 * 1、1 <= nums.length <= 10^4
 * 2、1 <= nums[i] <= 10^9
 * 3、1 <= k <= 10^9
 * 4、1 <= multiplier <= 10^6
 * 链接：https://leetcode.cn/problems/final-array-state-after-k-multiplication-operations-ii/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        MOD = 10**9 + 7
        if multiplier == 1: return nums
        n = len(nums)
        mx = max(nums)
        tree = [[INF, -1] for _ in range(2 << n.bit_length())]

        # set_value(0, 0, n - 1, ii + 1, i, 1)
        def set_value(o, l, r, idx, val):
            # o: 根节点 l：区间左端点 r：区间右端点 idx：更新下标 val：更新值
            if l == r:
                tree[o] = val
                return
            mid = (l + r) >> 1
            if idx <= mid:
                set_value(o * 2 + 1, l, mid, idx, val)
            else:
                set_value(o * 2 + 2, mid + 1, r, idx, val)
            process(o, l, r)

        def query(o, l, r, L, R):
            if l == L and r == R:
                return tree[o]
            mid = (l + r) >> 1
            if R <= mid:
                return query(o * 2 + 1, l, mid, L, R)
            if L >= mid + 1:
                return query(o * 2 + 2, mid + 1, r, L, R)
            return min(query(o * 2 + 1, l, mid, L, mid), query(o * 2 + 2, mid + 1, r, mid + 1, R))

        def process(o, l, r):
            if l == r: return
            a, b = tree[o * 2 + 1], tree[o * 2 + 2]
            tree[o] = min(a, b)

        for i, num in enumerate(nums):
            set_value(0, 0, n - 1, i, [num, i])
        ii = 0
        a = 0
        while ii < k:
            val_mn = query(0, 0, n - 1, 0, n - 1)
            v = val_mn[0] * multiplier
            nums[val_mn[1]] = v
            set_value(0, 0, n - 1, val_mn[1], [v, val_mn[1]])
            ii += 1
            if v > mx and a == 0:  # 这个时候出现了循环~
                a, r = divmod(k - ii, n)
                ii = k - r
        for i in range(n):
            nums[i] = (nums[i] * pow(multiplier, a, MOD)) % MOD
        return nums


if __name__ == '__main__':
    # [108,72]
    print(Solution().getFinalState([3, 2], 4, 6))
    #
    print(Solution().getFinalState([
        2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288,
        1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912
    ], 1000000000, 2))
    # [1]
    print(Solution().getFinalState([1], 1000000000, 1))
    # [16,8]
    print(Solution().getFinalState([1, 2], k=3, multiplier=4))
    # [198168519]
    print(Solution().getFinalState([161209470], k=56851412, multiplier=39846))
    # [8,4,6,5,6]
    print(Solution().getFinalState([2, 1, 3, 5, 6], k=5, multiplier=2))
    # [999999307,999999993]
    print(Solution().getFinalState([100000, 2000], k=2, multiplier=1000000))
