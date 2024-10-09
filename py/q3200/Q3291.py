"""
 * 给你一个字符串数组 words 和一个字符串 target。
 * 如果字符串 x 是 words 中 任意 字符串的 前缀，则认为 x 是一个 有效 字符串。
 * 现计划通过 连接 有效字符串形成 target ，请你计算并返回需要连接的 最少 字符串数量。
 * 如果无法通过这种方式形成 target，则返回 -1。
 * 提示：
 * 1、1 <= words.length <= 100
 * 2、1 <= words[i].length <= 5 * 10^3
 * 3、输入确保 sum(words[i].length) <= 10^5。
 * 4、words[i] 只包含小写英文字母。
 * 5、1 <= target.length <= 5 * 10^3 
 * 6、target 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-i/
"""
from functools import cache
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def minValidStrings(self, words: List[str], target: str) -> int:
        tree = {}

        for word in words:
            p = tree
            for c in word:
                if c not in p:
                    p[c] = {}
                p = p[c]
            p['END'] = word

        n = len(target)

        def query(l, r):
            p = tree
            for i in range(l, r):
                if target[i] not in p:
                    return False
                p = p[target[i]]
            return True

        @cache
        def dfs(l, r):
            if l == r: return 0
            if query(l, r): return 1
            ret = INF
            p = tree
            for ii in range(l + 1, r):
                if target[ii - 1] not in p:
                    break
                p = p[target[ii - 1]]
                ret = min(ret, 1 + dfs(ii, r))
            return ret

        ans = dfs(0, n)
        return ans if ans < INF else -1


if __name__ == '__main__':
    # 2
    print(Solution().minValidStrings(["abababab", "ab"], target="ababaababa"))
    # 3
    print(Solution().minValidStrings(["abc", "aaaaa", "bcdef"], target="aabcdabc"))
    # -1
    print(Solution().minValidStrings(["abcdef"], target="xyz"))
