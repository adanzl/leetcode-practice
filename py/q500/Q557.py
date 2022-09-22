"""
 * 给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
 * 提示：
 * 1、1 <= s.length <= 5 * 10^4
 * 2、s 包含可打印的 ASCII 字符。
 * 3、s 不包含任何开头或结尾空格。
 * 4、s 里 至少 有一个词。
 * 5、s 中的所有单词都用一个空格隔开。
 * 链接：https://leetcode.cn/problems/reverse-words-in-a-string-iii/
"""


class Solution:

    def reverseWords(self, s: str) -> str:
        return " ".join([ss[::-1] for ss in s.split()])


if __name__ == '__main__':
    # "s'teL ekat edoCteeL tsetnoc"
    print(Solution().reverseWords("Let's take LeetCode contest"))
    # "doG gniD"
    print(Solution().reverseWords("God Ding"))