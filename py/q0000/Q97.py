"""
 * 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
 * 两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：
 * s = s1 + s2 + ... + sn
 * t = t1 + t2 + ... + tm
 * |n - m| <= 1
 * 交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
 * 注意：a + b 意味着字符串 a 和 b 连接。
 * 提示：
 * 1、0 <= s1.length, s2.length <= 100
 * 2、0 <= s3.length <= 200
 * 3、s1、s2、和 s3 都由小写英文字母组成
 * 进阶：您能否仅使用 O(s2.length) 额外的内存空间来解决它?
 * 链接：https://leetcode-cn.com/problems/interleaving-string/
"""
from functools import cache


class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp 解决，dp[i][j] 表示 s1[:i] 和 s2[:j] 能否交错组成 s3[:i+j]
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l3 != l1 + l2:
            return False

        dp = [True] + [False] * (l2)
        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if i:
                    dp[j] &= s1[i - 1] == s3[i + j - 1]
                if j and s2[j - 1] == s3[i + j - 1]:
                    dp[j] |= dp[j - 1]
        return dp[-1]

    def isInterleave1(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        @cache
        def dfs(idx, i1, i2):
            if idx == len(s3):
                return True
            ret = False
            if i1 < len(s1) and s3[idx] == s1[i1]:
                ret |= dfs(idx + 1, i1 + 1, i2)
            if i2 < len(s2) and s3[idx] == s2[i2]:
                ret |= dfs(idx + 1, i1, i2 + 1)
            return ret

        return dfs(0, 0, 0)


if __name__ == '__main__':
    # True
    print(Solution().isInterleave("aabcc", s2="dbbca", s3="aadbbcbcac"))
    # False
    print(Solution().isInterleave("aabcc", s2="dbbca", s3="aadbbbaccc"))
    # True
    print(Solution().isInterleave("", s2="", s3=""))
