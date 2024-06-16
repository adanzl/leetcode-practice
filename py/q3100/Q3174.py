"""
 * 给你一个字符串 s 。
 * 你的任务是重复以下操作删除 所有 数字字符：
 * 删除 第一个数字字符 以及它左边 最近 的 非数字 字符。
 * 请你返回删除所有数字字符以后剩下的字符串。
 * 提示：
 * 1、1 <= s.length <= 100
 * 2、s 只包含小写英文字母和数字字符。
 * 3、输入保证所有数字都可以按以上操作被删除。
 * 链接：https://leetcode.cn/problems/clear-digits/description/
"""


class Solution:

    def clearDigits(self, s: str) -> str:
        ss = []
        for c in s:
            if c.isdigit():
                ss.pop()
            else:
                ss.append(c)
        return "".join(ss)


if __name__ == '__main__':
    # "abc"
    print(Solution().clearDigits("abc"))
    # ""
    print(Solution().clearDigits("cb34"))
