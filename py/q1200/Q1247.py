"""
 * 有两个长度相同的字符串 s1 和 s2，且它们其中 只含有 字符 "x" 和 "y"，你需要通过「交换字符」的方式使这两个字符串相同。
 * 每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。
 * 交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。也就是说，我们可以交换 s1[i] 和 s2[j]，但不能交换 s1[i] 和 s1[j]。
 * 最后，请你返回使 s1 和 s2 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回 -1 。
 * 提示：
 * 1、1 <= s1.length, s2.length <= 1000
 * 2、s1, s2 只包含 'x' 或 'y'。
 * 链接：https://leetcode.cn/problems/minimum-swaps-to-make-strings-equal/
"""
from typing import List


class Solution:

    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0, 0
        n = len(s1)
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy += 1
            if a == 'y' and b == 'x':
                yx += 1
        if (xy + yx) % 2 == 1:
            return -1
        return xy // 2 + yx // 2 + xy % 2 + yx % 2


if __name__ == '__main__':
    # 1
    print(Solution().minimumSwap("xx", s2="yy"))
    # 2
    print(Solution().minimumSwap("xy", s2="yx"))
    # -1
    print(Solution().minimumSwap("xx", s2="xy"))
    # 4
    print(Solution().minimumSwap("xxyyxyxyxx", s2="xyyxyxxxyx"))
