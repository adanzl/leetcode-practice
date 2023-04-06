"""
 * 给你一个整数 n ，以二进制字符串的形式返回该整数的 负二进制（base -2）表示。
 * 注意，除非字符串就是 "0"，否则返回的字符串中不能含有前导零。
 * 提示：0 <= n <= 10^9
 * 链接：https://leetcode.cn/problems/convert-to-base-2/
"""


class Solution:

    def baseNeg2(self, n: int) -> str:
        l = n.bit_length()
        ans = 0

        def func(num, s):
            sm, cnt = 0, s
            while sm < num:
                sm += 1 << cnt
                cnt += 2
            return cnt - 2

        while n:
            sign = 1 if n > 0 else -1
            cnt = func(abs(n), 0 if n > 0 else 1)
            n += -sign * (1 << cnt)
            ans += 1 << cnt

        return bin(ans)[2:]


if __name__ == '__main__':
    # "11010"
    print(Solution().baseNeg2(6))
    # "0"
    print(Solution().baseNeg2(0))
    # "110"
    print(Solution().baseNeg2(2))
    # "111"
    print(Solution().baseNeg2(3))
    # "100"
    print(Solution().baseNeg2(4))