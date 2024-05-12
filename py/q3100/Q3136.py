"""
 * 有效单词 需要满足以下几个条件：
 * 1、至少 包含 3 个字符。
 * 2、由数字 0-9 和英文大小写字母组成。（不必包含所有这类字符。）
 * 3、至少 包含一个 元音字母 。
 * 4、至少 包含一个 辅音字母 。
 * 给你一个字符串 word 。如果 word 是一个有效单词，则返回 true ，否则返回 false 。
 * 注意：
 * 1、'a'、'e'、'i'、'o'、'u' 及其大写形式都属于 元音字母 。
 * 2、英文中的 辅音字母 是指那些除元音字母之外的字母。
 * 提示：
 * 1、1 <= word.length <= 20
 * 2、word 由英文大写和小写字母、数字、'@'、'#' 和 '$' 组成。
 * 链接：https://leetcode.cn/problems/valid-word/
"""


class Solution:

    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        c_num, c_a, c_v = 0, 0, 0
        for c in word:
            if c in '0123456789': c_num += 1
            elif c in 'aeiou' or c in 'AEIOU': c_v += 1
            elif c.islower() or c.isupper(): c_a += 1
            else: return False
        return bool(c_a and c_v)


if __name__ == '__main__':
    # True
    print(Solution().isValid("Hor"))
    # True
    print(Solution().isValid("234Adas"))
    # False
    print(Solution().isValid("b3"))
    # False
    print(Solution().isValid("a3$e"))
