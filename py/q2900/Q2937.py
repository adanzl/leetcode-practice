"""
 * 给你三个字符串 s1、s2 和 s3。 你可以根据需要对这三个字符串执行以下操作 任意次数 。
 * 在每次操作中，你可以选择其中一个长度至少为 2 的字符串 并删除其 最右位置上 的字符。
 * 如果存在某种方法能够使这三个字符串相等，请返回使它们相等所需的 最小 操作次数；否则，返回 -1。
 * 提示：
 * 1、1 <= s1.length, s2.length, s3.length <= 100
 * 2、s1、s2 和 s3 仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/make-three-strings-equal/
"""


class Solution:

    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if not (s1[0] == s2[0] == s3[0]):
            return -1
        ans = 0
        n1, n2, n3 = len(s1), len(s2), len(s3)
        for c1, c2, c3 in zip(s1, s2, s3):
            if c1 == c2 == c3:
                ans += 1
            else:
                break
        return n1 - ans + n2 - ans + n3 - ans


if __name__ == '__main__':
    # 10
    print(Solution().findMinimumOperations("bcbb", "bccbabb", "bcabb"))
    # 9
    print(Solution().findMinimumOperations("aca", "abcc", "accba"))
    # 2
    print(Solution().findMinimumOperations("abc", s2="abb", s3="ab"))
    # -1
    print(Solution().findMinimumOperations("dac", s2="bac", s3="cac"))
