"""
 * 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
 * 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
 * 提示：
 * 1、1 <= s.length <= 300
 * 2、1 <= wordDict.length <= 1000
 * 3、1 <= wordDict[i].length <= 20
 * 4、s 和 wordDict[i] 仅有小写英文字母组成
 * 5、wordDict 中的所有字符串 互不相同
 * 链接：https://leetcode.cn/problems/word-break/
"""

from functools import cache
from typing import *


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def dfs(start):
            if start == len(s): return True
            for i in range(start + 1, len(s) + 1):
                if s[start:i] in wordDict:
                    if dfs(i): return True
            return False

        return dfs(0)


if __name__ == '__main__':
    # true
    print(Solution().wordBreak("leetcode", ["leet", "code"]))
    # true
    print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
    # false
    print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
