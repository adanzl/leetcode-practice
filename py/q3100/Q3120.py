"""
 * 给你一个字符串 word。如果 word 中同时存在某个字母的小写形式和大写形式，则称这个字母为 特殊字母 。
 * 返回 word 中 特殊字母 的数量。
 * 提示：
 * 1、1 <= word.length <= 50
 * 2、word 仅由小写和大写英文字母组成。
 * 链接：https://leetcode.cn/problems/count-the-number-of-special-characters-i/
"""


class Solution:

    def numberOfSpecialChars(self, word: str) -> int:
        # 对于大写英文字母：其二进制从右往左第 6 个比特值一定是 0。
        # 对于小写英文字母：其二进制从右往左第 6 个比特值一定是 1。
        # 对于任何英文字母：其小写字母二进制低 5 位，一定和其大写字母二进制低 5 位相等。
        mask = [0, 0]
        for c in map(ord, word):
            mask[c >> 5 & 1] |= 1 << (c & 31)
        return (mask[0] & mask[1]).bit_count()


if __name__ == '__main__':
    # 3
    print(Solution().numberOfSpecialChars("aaAbcBC"))
    # 0
    print(Solution().numberOfSpecialChars("abc"))
    # 1
    print(Solution().numberOfSpecialChars("abBCab"))
