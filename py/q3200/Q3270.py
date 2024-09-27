"""
 * 给你三个 正 整数 num1 ，num2 和 num3 。
 * 数字 num1 ，num2 和 num3 的数字答案 key 是一个四位数，定义如下：
 * 1、一开始，如果有数字 少于 四位数，给它补 前导 0 。
 * 2、答案 key 的第 i 个数位（1 <= i <= 4）为 num1 ，num2 和 num3 第 i 个数位中的 最小 值。
 * 请你返回三个数字 没有 前导 0 的数字答案。
 * 提示：1 <= num1, num2, num3 <= 9999
 * 链接：https://leetcode.cn/problems/find-the-key-of-the-numbers/
"""

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        s1, s2, s3 = str(num1).rjust(4, '0'), str(num2).rjust(4, '0'), str(num3).rjust(4, '0')
        ans = [''] * 4
        for i in range(4):
            ans[i] = min(s1[i], s2[i], s3[i])
        return int(''.join(ans))


if __name__ == '__main__':
    # 0
    print(Solution().generateKey(1, num2=10, num3=1000))
    # 777
    print(Solution().generateKey(987, num2=879, num3=798))
    # 1
    print(Solution().generateKey(1, num2=2, num3=3))
