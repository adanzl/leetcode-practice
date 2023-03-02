"""
 * 二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。如果该数字无法精确地用32位以内的二进制表示，则打印“ERROR”。
 * 提示：
 * 1、32位包括输出中的 "0." 这两位。
 * 2、题目保证输入用例的小数位数最多只有 6 位
 * 链接：https://leetcode.cn/problems/bianry-number-to-string-lcci/
"""
from typing import List


class Solution:

    def printBin(self, num: float) -> str:
        num *= 64
        if not num.is_integer():
            return 'ERROR'
        return '0.' + bin(int(num))[2:].zfill(6).rstrip('0')


if __name__ == '__main__':
    # "0.101"
    print(Solution().printBin(0.625))
    # "ERROR"
    print(Solution().printBin(0.1))