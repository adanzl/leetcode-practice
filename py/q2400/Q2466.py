"""
 * 给你整数 zero ，one ，low 和 high ，我们从空字符串开始构造一个字符串，每一步执行下面操作中的一种：
 * 1、将 '0' 在字符串末尾添加 zero  次。
 * 2、将 '1' 在字符串末尾添加 one 次。
 * 以上操作可以执行任意次。
 * 如果通过以上过程得到一个 长度 在 low 和 high 之间（包含上下边界）的字符串，那么这个字符串我们称为 好 字符串。
 * 请你返回满足以上要求的 不同 好字符串数目。由于答案可能很大，请将结果对 109 + 7 取余 后返回。
 * 提示：
 * 1 <= low <= high <= 10^5
 * 1 <= zero, one <= low
 * 链接：https://leetcode.cn/problems/count-ways-to-build-good-strings/
"""


class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        ans = [1] + [0] * high
        for i in range(high + 1):
            if i + zero <= high:
                ans[i + zero] += ans[i]
            if i + one <= high:
                ans[i + one] += ans[i]
        return sum(ans[low:high + 1]) % MOD


if __name__ == '__main__':
    # 5
    print(Solution().countGoodStrings(2, 3, 1, 2))
    #
    print(Solution().countGoodStrings(200, 200, 10, 1))
    # 8
    print(Solution().countGoodStrings(3, 3, 1, 1))
