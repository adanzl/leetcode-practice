"""
 * 给定两个字符串 s 和 t ，每个字符串代表一个非负有理数，只有当它们表示相同的数字时才返回 true 。字符串中可以使用括号来表示有理数的重复部分。
 * 有理数 最多可以用三个部分来表示：整数部分 <IntegerPart>、小数非重复部分 <NonRepeatingPart> 和小数重复部分 <(><RepeatingPart><)>。
 * 数字可以用以下三种方法之一来表示：
 * 1、<IntegerPart> 例： 0 ,12 和 123 
 * 2、<IntegerPart><.><NonRepeatingPart> 例： 0.5 , 1. , 2.12 和 123.0001
 * 3、<IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)> 例： 0.1(6) ， 1.(9)， 123.00(1212)
 * 十进制展开的重复部分通常在一对圆括号内表示。例如： 1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)
 * 提示：
 * 1、每个部分仅由数字组成。
 * 2、整数部分 <IntegerPart> 不会以零开头。（零本身除外）
 * 3、1 <= <IntegerPart>.length <= 4 
 * 4、0 <= <NonRepeatingPart>.length <= 4 
 * 5、1 <= <RepeatingPart>.length <= 4 
 * 链接：https://leetcode.cn/problems/equal-rational-numbers/
"""

from math import gcd

#
# @lc app=leetcode.cn id=972 lang=python3
#
# [972] 相等的有理数
#


# @lc code=start
class Solution:

    def isRationalEqual(self, s: str, t: str) -> bool:

        def parse(ss):
            i_dot = ss.find('.')
            intPart = ss[:i_dot] if i_dot != -1 else ss
            i_lq, i_rq = ss.find('('), ss.find(')')
            nrPart, rPart = '', ''
            if i_dot != -1:
                if i_lq != -1 and i_rq != -1:
                    rPart = ss[i_lq + 1:i_rq]
                    nrPart = ss[i_dot + 1:i_lq]
                else:
                    nrPart = ss[i_dot + 1:]
            lnr = len(nrPart)
            a = b = 0
            if nrPart:
                a, b = int(nrPart), 10**lnr
            if rPart:
                lr = len(rPart)
                a, b = int(rPart), 10**lr - 1
                a += int(nrPart) * b if nrPart else 0
                b *= 10**lnr
                a, b = a // gcd(a, b), b // gcd(a, b)
            return int(intPart), a, b

        def calc(num, a, b):
            if a == 0 or b == 0: return num
            return num + a / b

        # print(parse(s), parse(t))
        return calc(*parse(s)) == calc(*parse(t))


# @lc code=end

if __name__ == '__main__':
    # true
    print(Solution().isRationalEqual("0.08(9)", t="0.09"))
    # true
    print(Solution().isRationalEqual("0.(52)", t="0.5(25)"))
    # true
    print(Solution().isRationalEqual("0.1666(6)", t="0.166(66)"))
    # true
    print(Solution().isRationalEqual("0.9(9)", t="1."))
