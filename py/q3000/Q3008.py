"""
 * 给你一个下标从 0 开始的字符串 s 、字符串 a 、字符串 b 和一个整数 k 。
 * 如果下标 i 满足以下条件，则认为它是一个 美丽下标：
 * 1、0 <= i <= s.length - a.length
 * 2、s[i..(i + a.length - 1)] == a
 * 3、存在下标 j 使得：
 *      0 <= j <= s.length - b.length
 *      s[j..(j + b.length - 1)] == b
 *      |j - i| <= k
 * 以数组形式按 从小到大排序 返回美丽下标。
 * 提示：
 * 1、1 <= k <= s.length <= 5*10^5
 * 2、1 <= a.length, b.length <= 5*10^5
 * 3、s、a、和 b 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/find-beautiful-indices-in-the-given-array-ii/
"""
import bisect
from typing import List


class Solution:

    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        pos_a = self.kmp(s, a)
        pos_b = self.kmp(s, b)

        ans = []
        for i in pos_a:
            bi = bisect.bisect_left(pos_b, i)
            if bi < len(pos_b) and pos_b[bi] - i <= k or \
               bi > 0 and i - pos_b[bi - 1] <= k:
                ans.append(i)
        return ans

    def kmp(self, text: str, pattern: str) -> List[int]:
        m = len(pattern)
        pi = [0] * m
        c = 0
        for i in range(1, m):
            v = pattern[i]
            while c and pattern[c] != v:
                c = pi[c - 1]
            if pattern[c] == v:
                c += 1
            pi[i] = c

        res = []
        c = 0
        for i, v in enumerate(text):
            v = text[i]
            while c and pattern[c] != v:
                c = pi[c - 1]
            if pattern[c] == v:
                c += 1
            if c == len(pattern):
                res.append(i - m + 1)
                c = pi[c - 1]
        return res


if __name__ == '__main__':
    # [16, 33]
    print(Solution().beautifulIndices("isawsquirrelnearmysquirrelhouseohmy", a="my", b="squirrel", k=15))
    # []
    print(Solution().beautifulIndices("opzufozzl", "opz", "foz", 3))
    # [0]
    print(Solution().beautifulIndices("abcd", a="a", b="a", k=4))
