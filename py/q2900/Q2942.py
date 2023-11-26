"""
 * 给你一个下标从 0 开始的字符串数组 words 和一个字符 x 。
 * 请你返回一个 下标数组 ，表示下标在数组中对应的单词包含字符 x 。
 * 注意 ，返回的数组可以是 任意 顺序。
 * 提示：
 * 1、1 <= words.length <= 50
 * 2、1 <= words[i].length <= 50
 * 3、x 是一个小写英文字母。
 * 4、words[i] 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/find-words-containing-character/
"""
from typing import List


class Solution:

    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)):
            if x in words[i]:
                ans.append(i)
        return ans


if __name__ == '__main__':
    # [0,1]
    print(Solution().findWordsContaining(["leet", "code"], x="e"))
    # [0,2]
    print(Solution().findWordsContaining(["abc", "bcd", "aaaa", "cbc"], x="a"))
    # []
    print(Solution().findWordsContaining(["abc", "bcd", "aaaa", "cbc"], x="z"))
