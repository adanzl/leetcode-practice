from ast import main

'''
给你一个字符串 text ，该字符串由若干被空格包围的单词组成。每个单词由一个或者多个小写英文字母组成，并且两个单词之间至少存在一个空格。题目测试用例保证 text 至少包含一个单词 。
请你重新排列空格，使每对相邻单词之间的空格数目都 相等 ，并尽可能 最大化 该数目。如果不能重新平均分配所有空格，请 将多余的空格放置在字符串末尾 ，这也意味着返回的字符串应当与原 text 字符串的长度相等。
返回 重新排列空格后的字符串 。
提示：
1、1 <= text.length <= 100
2、text 由小写英文字母和 ' ' 组成
3、text 中至少包含一个单词
链接：https://leetcode.cn/problems/rearrange-spaces-between-words
'''


class Solution:
    def reorderSpaces(self, text: str) -> str:
        c_pad = text.count(' ')
        words = text.split()
        if len(words) == 1:
            return words[0] + ' ' * c_pad
        per_space, end_space = divmod(c_pad, len(words) - 1)
        return (' ' * per_space).join(words) + ' ' * end_space


if __name__ == '__main__':

    print(Solution().reorderSpaces("  this   is  a sentence "))
    print(Solution().reorderSpaces("  this   sentence "))
