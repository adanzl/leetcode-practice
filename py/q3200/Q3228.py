"""
 * 给你一个 二进制字符串 s。
 * 你可以对这个字符串执行 任意次 下述操作：
 * 1、选择字符串中的任一下标 i（ i + 1 < s.length ），该下标满足 s[i] == '1' 且 s[i + 1] == '0'。
 * 2、将字符 s[i] 向 右移 直到它到达字符串的末端或另一个 '1'。
 *      例如，对于 s = "010010"，如果我们选择 i = 1，结果字符串将会是 s = "000110"。
 * 返回你能执行的 最大 操作次数。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s[i] 为 '0' 或 '1'。
 * 链接：https://leetcode.cn/problems/maximum-number-of-operations-to-move-ones-to-the-end/description/
"""


class Solution:

    def maxOperations(self, s: str) -> int:
        ans = 0
        n = len(s)
        cnt1 = 0
        for i in range(n):
            if s[i] == '1':
                cnt1 += 1
            elif i and s[i - 1] == '1':
                ans += cnt1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().maxOperations("110"))
    # 4
    print(Solution().maxOperations("1001101"))
    # 0
    print(Solution().maxOperations("00111"))
