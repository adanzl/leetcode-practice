"""
 * 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
 * 提示：
 * 1、1 <= s.length <= 10^4
 * 2、s 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/remove-duplicate-letters/
"""
from collections import *


class Solution:

    def removeDuplicateLetters(self, s: str) -> str:
        remain = Counter(s)
        ss = deque()
        for c in s:
            remain[c] -= 1
            if c in ss: continue
            while ss and ord(ss[-1]) > ord(c) and remain[ss[-1]] > 0:
                ss.pop()
            ss.append(c)
        return "".join(ss)


if __name__ == "__main__":
    # "bed"
    print(Solution().removeDuplicateLetters("edebbed"))
    # "abc"
    print(Solution().removeDuplicateLetters("abacb"))
    # "acdb"
    print(Solution().removeDuplicateLetters("cbacdcbc"))
    # "abc"
    print(Solution().removeDuplicateLetters("bcabc"))
