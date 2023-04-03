"""
 * 给你一个正整数数组 arr（可能存在重复的元素），请你返回可在 一次交换（交换两数字 arr[i] 和 arr[j] 的位置）后得到的、按字典序排列小于 arr 的最大排列。
 * 如果无法这么操作，就请返回原数组。
 * 提示：
 * 1、1 <= arr.length <= 10^4
 * 2、1 <= arr[i] <= 10^4
 * 链接：https://leetcode.cn/problems/previous-permutation-with-one-swap/
"""
import bisect
from typing import List


class Solution:

    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        a = [[arr[-1], n - 1]]
        for i in range(n - 2, -1, -1):
            idx = bisect.bisect_left(a, [arr[i], i])
            if idx > 0:
                arr[i], arr[a[idx - 1][1]] = arr[a[idx - 1][1]], arr[i]
                return arr
            bisect.insort(a, [arr[i], i], key=lambda x: (x[0], -x[1]))
        return arr


if __name__ == '__main__':
    # [1,3,1,3]
    print(Solution().prevPermOpt1([3, 1, 1, 3]))
    # [3,1,2]
    print(Solution().prevPermOpt1([3, 2, 1]))
    # [1,1,5]
    print(Solution().prevPermOpt1([1, 1, 5]))
    # [1,7,4,6,9]
    print(Solution().prevPermOpt1([1, 9, 4, 6, 7]))
