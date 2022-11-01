"""
 * 给你一个以字符串表示的非负整数 num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。
 * 提示：
 * 1、1 <= k <= num.length <= 10^5
 * 2、num 仅由若干位数字（0 - 9）组成
 * 3、除了 0 本身之外，num 不含任何前导零
 * 链接：https://leetcode.cn/problems/remove-k-digits/
"""


class Solution:

    def removeKDigits(self, num: str, k: int) -> str:
        s = []
        for d in num:
            while k and s and s[-1] > d:
                s.pop()
                k -= 1
            s.append(d)
        if k: s = s[:-k]
        return "".join(s).lstrip('0') or '0'


if __name__ == '__main__':
    # "1219"
    print(Solution().removeKDigits("1432219", 3))
    # "200"
    print(Solution().removeKDigits("10200", 1))
    # "0"
    print(Solution().removeKDigits("10", 2))