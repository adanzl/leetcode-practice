"""
 * 给你一个下标从 0 开始的字符串 str1 和 str2 。
 * 一次操作中，你选择 str1 中的若干下标。对于选中的每一个下标 i ，你将 str1[i] 循环 递增，变成下一个字符。也就是说 'a' 变成 'b' ，'b' 变成 'c' ，以此类推，'z' 变成 'a' 。
 * 如果执行以上操作 至多一次 ，可以让 str2 成为 str1 的子序列，请你返回 true ，否则返回 false 。
 * 注意：一个字符串的子序列指的是从原字符串中删除一些（可以一个字符也不删）字符后，剩下字符按照原本先后顺序组成的新字符串。
 * 提示：
 * 1、1 <= str1.length <= 10^5
 * 2、1 <= str2.length <= 10^5
 * 3、str1 和 str2 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/make-string-a-subsequence-using-cyclic-increments/
"""


class Solution:

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i0, i1 = 0, 0
        n0, n1 = len(str1), len(str2)

        while i0 < n0 and i1 < n1:
            nx = chr((ord(str1[i0]) - ord('a') + 1) % 26 + ord('a'))
            if str1[i0] == str2[i1] or nx == str2[i1]:
                i0 += 1
                i1 += 1
            else:
                i0 += 1
        return i1 == n1


if __name__ == '__main__':
    # True
    print(Solution().canMakeSubsequence("abc", str2="ad"))
    # False
    print(Solution().canMakeSubsequence("ab", str2="d"))
    # True
    print(Solution().canMakeSubsequence("zc", str2="ad"))
