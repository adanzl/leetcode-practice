"""
 * 给你一个下标从 0 开始的字符串数组 words 和两个整数：left 和 right 。
 * 如果字符串以元音字母开头并以元音字母结尾，那么该字符串就是一个 元音字符串 ，其中元音字母是 'a'、'e'、'i'、'o'、'u' 。
 * 返回 words[i] 是元音字符串的数目，其中 i 在闭区间 [left, right] 内。
 * 提示：
 * 1、1 <= words.length <= 1000
 * 2、1 <= words[i].length <= 10
 * 3、words[i] 仅由小写英文字母组成
 * 4、0 <= left <= right < words.length
 * 链接：https://leetcode.cn/problems/count-the-number-of-vowel-strings-in-range/
"""
from typing import List


class Solution:

    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        return sum(1 for word in words[left:right + 1] if word[0] in 'aeiou' and word[-1] in 'aeiou')


if __name__ == '__main__':
    # 2
    print(Solution().vowelStrings(["are", "amy", "u"], left=0, right=2))
    # 3
    print(Solution().vowelStrings(["hey", "aeo", "mu", "ooo", "artro"], left=1, right=4))
