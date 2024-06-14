"""
 * 列表的 异或和（XOR sum）指对所有元素进行按位 XOR 运算的结果。如果列表中仅有一个元素，那么其 异或和 就等于该元素。
 * 例如，[1,2,3,4] 的 异或和 等于 1 XOR 2 XOR 3 XOR 4 = 4 ，而 [3] 的 异或和 等于 3 。
 * 给你两个下标 从 0 开始 计数的数组 arr1 和 arr2 ，两数组均由非负整数组成。
 * 根据每个 (i, j) 数对，构造一个由 arr1[i] AND arr2[j]（按位 AND 运算）结果组成的列表。
 * 其中 0 <= i < arr1.length 且 0 <= j < arr2.length 。
 * 返回上述列表的 异或和 。
 * 提示：
 * 1、1 <= arr1.length, arr2.length <= 10^5
 * 2、0 <= arr1[i], arr2[j] <= 10^9
 * 链接：https://leetcode.cn/problems/find-xor-sum-of-all-pairs-bitwise-and/
"""

from functools import reduce
from typing import List

#
# @lc app=leetcode.cn id=1835 lang=python3
#
# [1835] 所有数对按位与结果的异或和
#


# @lc code=start
class Solution:

    def getXORSum1(self, arr1: List[int], arr2: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, arr1) & reduce(lambda x, y: x ^ y, arr2)

    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        ans, x2 = 0, 0
        for v in arr2:
            x2 ^= v
        for v in arr1:
            ans ^= x2 & v
        return ans


# @lc code=end

if __name__ == '__main__':
    # 0
    print(Solution().getXORSum([1, 2, 3], arr2=[6, 5]))
    # 128
    print(Solution().getXORSum([1033, 4179, 1931, 8117, 7364, 7737, 6219, 3439, 1537, 7993], [6386]))
    # 4
    print(Solution().getXORSum([12], arr2=[4]))
