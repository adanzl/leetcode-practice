"""
 * 给你一个字符串 word ，该字符串由数字和小写英文字母组成。
 * 请你用空格替换每个不是数字的字符。例如，"a123bc34d8ef34" 将会变成 " 123  34 8  34" 。注意，剩下的这些整数为（相邻彼此至少有一个空格隔开）："123"、"34"、"8" 和 "34" 。
 * 返回对 word 完成替换后形成的 不同 整数的数目。
 * 只有当两个整数的 不含前导零 的十进制表示不同， 才认为这两个整数也不同。
 * 提示：
 * 1、1 <= word.length <= 1000
 * 2、word 由数字和小写英文字母组成
 * 链接：https://leetcode.cn/problems/number-of-different-integers-in-a-string/
"""

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = list(word)
        for i in range(len(s)):
            if not s[i].isdigit():
                s[i] = ' '
        ss = set()
        for w in ''.join(s).split():
            ss.add(int(w))
        return len(ss)


if __name__ == '__main__':
    # 3
    print(Solution().numDifferentIntegers("a123bc34d8ef34"))
    # 2
    print(Solution().numDifferentIntegers("leet1234code234"))
    # 1
    print(Solution().numDifferentIntegers("a1b01c001"))