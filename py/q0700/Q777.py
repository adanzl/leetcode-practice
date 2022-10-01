"""
 * 在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。
 * 一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。
 * 现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时， 返回True。
 * 提示：
 * 1、1 <= len(start) = len(end) <= 10000。
 * 2、start和end中的字符串仅限于'L', 'R'和'X'。
 * 链接：https://leetcode.cn/problems/swap-adjacent-in-lr-string/
"""
from typing import *


class Solution:

    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        i1, i2 = 0, 0
        # "XL" - "LX" "RX" - "XR"
        while i1 < n and i2 < n:
            while i1 < n and start[i1] == 'X':
                i1 += 1
            while i2 < n and end[i2] == 'X':
                i2 += 1
            if i1 >= n or i2 >= n:
                break
            if start[i1] != end[i2]:
                return False
            if start[i1] == 'L':
                if i1 < i2: return False
            else:
                if i1 > i2: return False
            i1 += 1
            i2 += 1
        while i1 < n and start[i1] == 'X':
            i1 += 1
        while i2 < n and end[i2] == 'X':
            i2 += 1
        return i1 == i2


if __name__ == '__main__':
    # True
    print(Solution().canTransform("RXXLRXRXL", "XRLXXRRLX"))
    # False
    print(Solution().canTransform("XX", "LL"))
    # True
    print(Solution().canTransform("XXXXXLXXXX", "LXXXXXXXXX"))