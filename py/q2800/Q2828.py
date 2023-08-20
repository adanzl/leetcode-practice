"""
 * 给你一个字符串数组 words 和一个字符串 s ，请你判断 s 是不是 words 的 首字母缩略词 。
 * 如果可以按顺序串联 words 中每个字符串的第一个字符形成字符串 s ，则认为 s 是 words 的首字母缩略词。
 * 例如，"ab" 可以由 ["apple", "banana"] 形成，但是无法从 ["bear", "aardvark"] 形成。
 * 如果 s 是 words 的首字母缩略词，返回 true ；否则，返回 false 。
 * 提示：
 * 1、1 <= words.length <= 100
 * 2、1 <= words[i].length <= 10
 * 3、1 <= s.length <= 100
 * 4、words[i] 和 s 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/check-if-a-string-is-an-acronym-of-words/
"""
from typing import List


class Solution:

    def isAcronym(self, words: List[str], s: str) -> bool:
        return s == ''.join(map(lambda x: x[0], words))


if __name__ == '__main__':
    # True
    print(Solution().isAcronym(["alice", "bob", "charlie"], s="abc"))
    # False
    print(Solution().isAcronym(["an", "apple"], s="a"))
    # True
    print(Solution().isAcronym(["never", "gonna", "give", "up", "on", "you"], s="ngguoy"))
