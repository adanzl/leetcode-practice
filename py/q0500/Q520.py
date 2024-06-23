"""
 * 我们定义，在以下情况时，单词的大写用法是正确的：
 * 1、全部字母都是大写，比如 "USA" 。
 * 2、单词中所有字母都不是大写，比如 "leetcode" 。
 * 3、如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。
 * 给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。
 * 提示：
 * 1、1 <= word.length <= 100
 * 2、word 由小写和大写英文字母组成
 * 链接：https://leetcode.cn/problems/detect-capital/
"""


class Solution:

    def detectCapitalUse(self, word: str) -> bool:
        return word == word.upper() or word == word.lower() or word == word.capitalize()


if __name__ == '__main__':
    # True
    print(Solution().detectCapitalUse("g"))
    # True
    print(Solution().detectCapitalUse("USA"))
    # False
    print(Solution().detectCapitalUse("FlaG"))
