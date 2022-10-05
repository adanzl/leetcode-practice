"""
 * 给定一个由 0 和 1 组成的数组 arr ，将数组分成  3 个非空的部分 ，使得所有这些部分表示相同的二进制值。
 * 如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：
 * 1、arr[0], arr[1], ..., arr[i] 为第一部分；
 * 2、arr[i + 1], arr[i + 2], ..., arr[j - 1] 为第二部分；
 * 3、arr[j], arr[j + 1], ..., arr[arr.length - 1] 为第三部分。
 * 4、这三个部分所表示的二进制值相等。
 * 如果无法做到，就返回 [-1, -1]。
 * 注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，而不会是 3。此外，前导零也是被允许的，所以 [0,1,1] 和 [1,1] 表示相同的值。
 * 提示：
 * 1、3 <= arr.length <= 3 * 10^4
 * 2、arr[i] 是 0 或 1
 * 链接：https://leetcode.cn/problems/three-equal-parts/
"""
from typing import *


class Solution:

    def threeEqualParts(self, arr: List[int]) -> List[int]:
        pos = []
        n = len(arr)
        for i in range(n):
            if arr[i] == 1:
                pos.append(i)
        if len(pos) == 0: return [0, 2]
        if len(pos) % 3 != 0: return [-1, -1]
        l = len(pos) // 3
        t0 = n - pos[-1] - 1  # tail 0
        i = t0 + pos[l - 1]  # tail 0 + pos[l]
        if i >= pos[-1]: return [-1, -1]
        j = pos[-l - 1] + t0 + 1
        j1 = pos[-l]  # first 1 of part3
        if n - 1 - j1 != i - pos[0]: return [-1, -1]
        # check p1: pos[0] - i, p2: x - j-1, p3: j1 - n-1
        for k in range(i - pos[0] + 1):
            if arr[i - k] != arr[j - 1 - k] or arr[j - 1 - k] != arr[n - 1 - k]: return [-1, -1]
        return [i, j]


if __name__ == '__main__':
    # [0,3]
    print(Solution().threeEqualParts([1, 0, 1, 0, 1]))
    # [-1,-1]
    print(Solution().threeEqualParts([1, 1, 0, 1, 1]))
    # [0,2]
    print(Solution().threeEqualParts([1, 1, 0, 0, 1]))
