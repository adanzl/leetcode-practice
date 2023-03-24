"""
 * 给你一个正整数 num ，请你将它分割成两个非负整数 num1 和 num2 ，满足：
 * 1、num1 和 num2 直接连起来，得到 num 各数位的一个排列。换句话说，num1 和 num2 中所有数字出现的次数之和等于 num 中所有数字出现的次数。
 * 2、num1 和 num2 可以包含前导 0 。
 * 请你返回 num1 和 num2 可以得到的和的 最小 值。
 * 注意：
 * 1、num 保证没有前导 0 。
 * 2、num1 和 num2 中数位顺序可以与 num 中数位顺序不同。
 * 提示：10 <= num <= 10^9
 * 链接：https://leetcode.cn/problems/split-with-minimum-sum/
"""
from typing import List


class Solution:

    def splitNum(self, num: int) -> int:
        arr = sorted([int(c) for c in list(str(num))])
        n1, n2 = arr[0], arr[1]
        i = 2
        while i < len(arr):
            n1 = n1 * 10 + arr[i]
            i += 1
            if i >= len(arr): break
            n2 = n2 * 10 + arr[i]
            i += 1
        return n1 + n2


if __name__ == '__main__':
    # 59
    print(Solution().splitNum(4325))
    # 687
    print(Solution().splitNum(687))