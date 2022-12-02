"""
 * 如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 接近 ：
 * 1、操作 1：交换任意两个 现有 字符。
 * 例如，abcde -> aecdb
 * 2、操作 2：将一个 现有 字符的每次出现转换为另一个 现有 字符，并对另一个字符执行相同的操作。
 * 例如，aacabb -> bbcbaa（所有 a 转化为 b ，而所有的 b 转换为 a ）
 * 你可以根据需要对任意一个字符串多次使用这两种操作。
 * 给你两个字符串，word1 和 word2 。如果 word1 和 word2 接近 ，就返回 true ；否则，返回 false 。
 * 提示：
 * 1、1 <= word1.length, word2.length <= 10^5
 * 2、word1 和 word2 仅包含小写英文字母
 * 链接：https://leetcode.cn/problems/determine-if-two-strings-are-close/
"""
from collections import Counter


class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        cnt1, cnt2 = Counter(word1), Counter(word2)
        return sorted(cnt1.values()) == sorted(cnt2.values()) and cnt1.keys() == cnt2.keys()


if __name__ == '__main__':
    # True
    print(Solution().closeStrings("abc", "bca"))
    # False
    print(Solution().closeStrings("a", "aa"))
    # True
    print(Solution().closeStrings("cabbba", "abbccc"))
    # False
    print(Solution().closeStrings("cabbba", "aabbss"))
