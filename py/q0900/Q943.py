"""
 * 给定一个字符串数组 words，找到以 words 中每个字符串作为子字符串的最短字符串。如果有多个有效最短字符串满足题目条件，返回其中 任意一个 即可。
 * 我们可以假设 words 中没有字符串是 words 中另一个字符串的子字符串。
 * 提示：
 * 1、1 <= words.length <= 12
 * 2、1 <= words[i].length <= 20
 * 3、words[i] 由小写英文字母组成
 * 4、words 中的所有字符串 互不相同
 * 链接：https://leetcode.cn/problems/find-the-shortest-superstring/
"""
from typing import *


class Solution:

    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        dp = [[""] * n for _ in range(1 << n)]  # mask-end

        def merge_str(s1, s2) -> str:
            l = 0
            ans = 0
            while l < len(s1) and l < len(s2):
                if s1[-l:] == s2[:l]:
                    ans = l
                l += 1
            return s1 + s2[ans:]

        def func(mask, idx) -> str:
            if dp[mask][idx] != "":
                return dp[mask][idx]
            if mask & (1 << idx) == 0: return None
            val = None
            for i in range(n):
                prev = func(mask & ~(1 << idx), i)
                if prev is None: continue
                nv = dp[(1 << i) | (1 << idx)][idx]
                if val is None or len(val) > len(prev) - len(words[i]) + len(nv):
                    val = prev[:-len(words[i])] + nv
            dp[mask][idx] = val
            return val

        for i in range(n):
            dp[1 << i][i] = words[i]
            for j in range(i):
                dp[(1 << i) | (1 << j)][i] = merge_str(words[j], words[i])
                dp[(1 << i) | (1 << j)][j] = merge_str(words[i], words[j])
        ans = None
        for i in range(n):
            ret = func((1 << n) - 1, i)
            if ans is None or (ret is not None and len(ret) < len(ans)):
                ans = ret
        return ans


if __name__ == '__main__':
    # "gctaagttcatgcatc"
    print(Solution().shortestSuperstring(["catg", "ctaagt", "gcta", "ttca", "atgcatc"]))
    # "alexlovesleetcode"
    print(Solution().shortestSuperstring(["alex", "loves", "leetcode"]))
