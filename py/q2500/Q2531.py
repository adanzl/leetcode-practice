"""
 * 给你两个下标从 0 开始的字符串 word1 和 word2 。
 * 一次 移动 由以下两个步骤组成：
 * 1、选中两个下标 i 和 j ，分别满足 0 <= i < word1.length 和 0 <= j < word2.length ，
 * 2、交换 word1[i] 和 word2[j] 。
 * 如果可以通过 恰好一次 移动，使 word1 和 word2 中不同字符的数目相等，则返回 true ；否则，返回 false 。
 * 提示：
 * 1、1 <= word1.length, word2.length <= 10^5
 * 2、word1 和 word2 仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/make-number-of-distinct-characters-equal/
"""
from typing import Counter


class Solution:

    # 统计 word1 字符出现次数 c_1 以及 word2 字符出现次数 c_2 ：
    # 如果 x == y，那么移动后不同字符数目不变，如果此时 c_1 和 c_2 的长度相同，那么返回 true；
    # 如果 x != y，那么就看 x 的个数是否为 1，y 的个数是否为 1，x 是否出现在 word2 中，y 是否出现在 word1 中来计算不同字符的变化量
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        for x, c in c1.items():
            for y, d in c2.items():
                if y == x:  # 无变化
                    if len(c1) == len(c2): return True
                elif len(c1) - (c == 1) + (c1[y] == 0) == \
                     len(c2) - (d == 1) + (c2[x] == 0):  # 计算变化量
                    return True
        return False


if __name__ == '__main__':
    # False
    print(Solution().isItPossible("ac", word2="b"))
    # True
    print(Solution().isItPossible("abcc", word2="aab"))
    # True
    print(Solution().isItPossible("abcde", word2="fghij"))
