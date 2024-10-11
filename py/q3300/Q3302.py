"""
 * 给你两个字符串 word1 和 word2 。
 * 如果一个字符串 x 修改 至多 一个字符会变成 y ，那么我们称它与 y 几乎相等 。
 * 如果一个下标序列 seq 满足以下条件，我们称它是 合法的 ：
 * 1、下标序列是 升序 的。
 * 2、将 word1 中这些下标对应的字符 按顺序 连接，得到一个与 word2 几乎相等 的字符串。
 * 请你返回一个长度为 word2.length 的数组，表示一个 字典序最小 的 合法 下标序列。如果不存在这样的序列，请你返回一个 空 数组。
 * 注意 ，答案数组必须是字典序最小的下标数组，而 不是 由这些下标连接形成的字符串。
 * 提示：
 * 1、1 <= word2.length < word1.length <= 3 * 10^5
 * 2、word1 和 word2 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/find-the-lexicographically-smallest-valid-sequence/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def validSequence(self, word1: str, word2: str) -> List[int]:
        m, n = len(word1), len(word2)
        ans = []
        i, j = m - 1, n - 1
        suf = [0] * (m + 1)
        suf[-1] = n
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                j -= 1
            suf[i] = j + 1
            i -= 1
        i, j = 0, 0
        changed = False
        while i < m and j < n:
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            else:
                if suf[i + 1] <= j + 1 and not changed:
                    changed = True
                    j += 1
                    ans.append(i)
            if j == n:
                return ans
            i += 1
        return []


if __name__ == '__main__':
    # [1,2,4]
    print(Solution().validSequence("bacdc", word2="abc"))
    # [0,1,2]
    print(Solution().validSequence("vbcca", word2="abc"))
    # []
    print(Solution().validSequence("aaaaaa", word2="aaabc"))
    # [0,1]
    print(Solution().validSequence("abc", word2="ab"))
