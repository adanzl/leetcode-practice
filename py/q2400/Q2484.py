"""
 * 给你数字字符串 s ，请你返回 s 中长度为 5 的 回文子序列 数目。由于答案可能很大，请你将答案对 10^9 + 7 取余 后返回。
 * 提示：
 * 1、如果一个字符串从前往后和从后往前读相同，那么它是 回文字符串 。
 * 2、子序列是一个字符串中删除若干个字符后，不改变字符顺序，剩余字符构成的字符串。
 * 提示：
 * 1、1 <= s.length <= 10^4
 * 2、s 只包含数字字符。
 * 链接：https://leetcode.cn/problems/count-palindromic-subsequences/
"""


class Solution:

    def countPalindromes(self, s: str) -> int:
        # 因为要求长度是5, 所以不用考虑偶数回文的情况
        # 以任意元素为中心，左右各为长度是2的字符串相乘即可
        MOD = 10**9 + 7
        n = len(s)
        ans = 0
        cnt_l_1, cnt_l_2 = [0] * 10, [0] * 100
        cnt_r_1, cnt_r_2 = [0] * 10, [0] * 100
        for i in range(n):
            num = int(s[i])
            for j in range(10):
                cnt_l_2[j * 10 + num] += cnt_l_1[j]
            cnt_l_1[num] += 1
        for i in range(n - 1, -1, -1):  # 遍历中心点
            num = int(s[i])
            cnt_l_1[num] -= 1
            for j in range(10):
                cnt_l_2[j * 10 + num] -= cnt_l_1[j]
            # 中心点左右，乘法原则
            for j in range(100):
                ans += cnt_l_2[j] * cnt_r_2[j]

            for j in range(10):
                cnt_r_2[j * 10 + num] += cnt_r_1[j]
            cnt_r_1[num] += 1
        return ans % MOD


if __name__ == '__main__':
    # 2
    print(Solution().countPalindromes("103301"))
    # 21
    print(Solution().countPalindromes("0000000"))
    # 2
    print(Solution().countPalindromes("9999900000"))