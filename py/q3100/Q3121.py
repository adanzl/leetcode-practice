"""
 * 给你一个字符串 word。如果 word 中同时出现某个字母 c 的小写形式和大写形式，
 * 并且 每个 小写形式的 c 都出现在第一个大写形式的 c 之前，则称字母 c 是一个 特殊字母 。
 * 返回 word 中 特殊字母 的数量。
 * 提示：
 * 1、1 <= word.length <= 2 * 10^5
 * 2、word 仅由小写和大写英文字母组成。
 * 链接：https://leetcode.cn/problems/count-the-number-of-special-characters-ii/
"""


class Solution:

    def numberOfSpecialChars(self, word: str) -> int:
        lower = upper = invalid = 0
        for c in map(ord, word):
            bit = 1 << (c & 31)
            if c & 32:  # 小写字母
                lower |= bit
                if upper & bit:  # c 也在 upper 中
                    invalid |= bit  # 不合法
            else:  # 大写字母
                upper |= bit
        # 从交集 lower & upper 中去掉不合法的字母 invalid
        return (lower & upper & ~invalid).bit_count()


if __name__ == '__main__':
    # 0
    print(Solution().numberOfSpecialChars("cCceDC"))
    # 0
    print(Solution().numberOfSpecialChars("AbBCab"))
    # 3
    print(Solution().numberOfSpecialChars("aaAbcBC"))
    # 0
    print(Solution().numberOfSpecialChars("abc"))
    # 0
    print(Solution().numberOfSpecialChars("abBCab"))
