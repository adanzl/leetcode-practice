"""
 * 行程长度编码 是一种常用的字符串压缩方法，它将连续的相同字符（重复 2 次或更多次）替换为字符和表示字符计数的数字（行程长度）。
 * 例如，用此方法压缩字符串 "aabccc" ，将 "aa" 替换为 "a2" ，"ccc" 替换为` "c3" 。因此压缩后的字符串变为 "a2bc3" 。
 * 注意，本问题中，压缩时没有在单个字符后附加计数 '1' 。
 * 给你一个字符串 s 和一个整数 k 。你需要从字符串 s 中删除最多 k 个字符，以使 s 的行程长度编码长度最小。
 * 请你返回删除最多 k 个字符后，s 行程长度编码的最小长度 。
 * 提示：
 * 1、1 <= s.length <= 100
 * 2、0 <= k <= s.length
 * 3、s 仅包含小写英文字母
 * 链接：https://leetcode.cn/problems/string-compression-ii/
"""


class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        calc = lambda x: 1 if x == 1 else (2 if x < 10 else (3 if x < 100 else 4))
        min = lambda a, b: a if a < b else b
        n = len(s)
        dp = [[0] * (k + 1) for _ in range(n + 1)]  # cnt-del k
        for i in range(n):
            for p in range(i, -1, -1):
                if s[p] != s[i]: break
                dp[i + 1][0] = dp[p][0] + calc(i - p + 1)
            for j in range(1, k + 1):
                # del s[i]: dp[i][j] = dp[i-1][j-1]
                dp[i + 1][j] = dp[i][j - 1]
                # keep: same=same_s[i], cnt=len_other, score=len(str(same)) -> dp[i][j] = min(dp[i-same-cnt][j-cnt]+score)
                same, cnt = 0, 0
                for p in range(i, -1, -1):
                    if s[p] == s[i]:
                        same += 1
                    else:
                        cnt += 1
                    if cnt > j: break
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i + 1 - same - cnt][j - cnt] + calc(same))
        return dp[n][k]


if __name__ == '__main__':
    # 5
    print(Solution().getLengthOfOptimalCompression("aaaaabaaaaafffwfff", 2))
    # 3
    print(Solution().getLengthOfOptimalCompression("aaaaaaaaaaa", 0))
    # 4
    print(Solution().getLengthOfOptimalCompression("aaabcccd", 2))
    # 2
    print(Solution().getLengthOfOptimalCompression("aabbaa", 2))