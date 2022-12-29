"""
 * 给你一个整数 n，请返回长度为 n 、仅由元音 (a, e, i, o, u) 组成且按 字典序排列 的字符串数量。
 * 字符串 s 按 字典序排列 需要满足：对于所有有效的 i，s[i] 在字母表中的位置总是与 s[i+1] 相同或在 s[i+1] 之前。
 * 提示：1 <= n <= 50 
 * 链接：https://leetcode.cn/problems/count-sorted-vowel-strings/
"""


class Solution:

    def countVowelStrings(self, n: int) -> int:
        # 这个神奇的优化，一点都不快
        dp = [0] + [1] * 5
        for _ in range(n - 1):
            for i in range(5):
                dp[i + 1] += dp[i]
        return sum(dp)

    def countVowelStrings1(self, n: int) -> int:
        dp = [1] + [0] * 5
        for _ in range(n):
            ndp = [0] + [0] * 5
            sm = dp[0]
            for i in range(5):
                sm += dp[i + 1]
                ndp[i + 1] += sm
            dp = ndp
        return sum(dp)


if __name__ == '__main__':
    # 15
    print(Solution().countVowelStrings(2))
    # 5
    print(Solution().countVowelStrings(1))
    # 66045
    print(Solution().countVowelStrings(33))