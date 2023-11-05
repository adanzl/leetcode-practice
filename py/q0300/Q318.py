"""
 * 给你一个字符串数组 words ，找出并返回 length(words[i]) * length(words[j]) 的最大值，并且这两个单词不含有公共字母。
 * 如果不存在这样的两个单词，返回 0 。
 * 提示：
 * 1、2 <= words.length <= 1000
 * 2、1 <= words[i].length <= 1000
 * 3、words[i] 仅包含小写字母
 * 链接：https://leetcode.cn/problems/maximum-product-of-word-lengths
"""
from typing import List


class Solution:

    def maxProduct(self, words: List[str]) -> int:

        def convert(word):
            ret = 0
            for c in word:
                ret |= 1 << (ord(c) - ord('a') + 1)
            return ret

        arr = [convert(w) for w in words]
        ans = 0
        for i in range(len(words)):
            for j in range(i):
                if arr[i] & arr[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans


if __name__ == '__main__':
    # 16
    print(Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
    # 4
    print(Solution().maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
    # 0
    print(Solution().maxProduct(["a", "aa", "aaa", "aaaa"]))
