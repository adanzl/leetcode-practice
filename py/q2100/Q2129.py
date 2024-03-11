"""
 * 给你一个字符串 title ，它由单个空格连接一个或多个单词组成，每个单词都只包含英文字母。
 * 请你按以下规则将每个单词的首字母 大写 ：
 * 1、如果单词的长度为 1 或者 2 ，所有字母变成小写。
 * 2、否则，将单词首字母大写，剩余字母变成小写。
 * 请你返回 大写后 的 title 。
 * 提示：
 * 1、1 <= title.length <= 100
 * 2、title 由单个空格隔开的单词组成，且不含有任何前导或后缀空格。
 * 3、每个单词由大写和小写英文字母组成，且都是 非空 的。
 * 链接：https://leetcode.cn/problems/capitalize-the-title
"""


class Solution:

    def capitalizeTitle(self, title: str) -> str:
        ans = []
        for s in title.split(' '):
            if len(s) <= 2:
                ans.append(s.lower())
            else:
                ans.append(s[0].upper() + s[1:].lower())
        return ' '.join(ans)


if __name__ == '__main__':
    # "Capitalize The Title"
    print(Solution().capitalizeTitle("capiTalIze tHe titLe"))
    # "First Letter of Each Word"
    print(Solution().capitalizeTitle("First leTTeR of EACH Word"))
    # "i Love Leetcode"
    print(Solution().capitalizeTitle("i lOve leetcode"))
