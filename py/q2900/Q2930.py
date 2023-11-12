"""
 * 给你一个整数 n 。
 * 如果一个字符串 s 只包含小写英文字母，且 将 s 的字符重新排列后，新字符串包含 子字符串 "leet" ，那么我们称字符串 s 是一个 好 字符串。
 * 比方说：
 * 1、字符串 "lteer" 是好字符串，因为重新排列后可以得到 "leetr" 。
 * 2、"letl" 不是好字符串，因为无法重新排列并得到子字符串 "leet" 。
 * 请你返回长度为 n 的好字符串 总 数目。
 * 由于答案可能很大，将答案对 10^9 + 7 取余 后返回。
 * 子字符串 是一个字符串中一段连续的字符序列。
 * 提示：1 <= n <= 10^5
 * 链接：https://leetcode.cn/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/description/
"""


class Solution:

    def stringCount(self, n: int) -> int:
        # 1、不包含l的字符串
        # 2、不包含t的字符串
        # 3、不包含e或者只包含一个e的字符串
        # 全集减去 1、2、3，补上1&2、1&3、2&3，减去1&2&3
        MOD = 10**9 + 7
        return (pow(26, n, MOD) - pow(25, n - 1, MOD) * (75 + n) + pow(24, n - 1, MOD) * (72 + n * 2) - pow(23, n - 1, MOD) * (23 + n)) % MOD


if __name__ == '__main__':
    # 12
    print(Solution().stringCount(4))
    # 83943898
    print(Solution().stringCount(10))
    #
    print(Solution().stringCount(10**5))
