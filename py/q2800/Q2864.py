"""
 * 给你一个 二进制 字符串 s ，其中至少包含一个 '1' 。
 * 你必须按某种方式 重新排列 字符串中的位，使得到的二进制数字是可以由该组合生成的 最大二进制奇数 。
 * 以字符串形式，表示并返回可以由给定组合生成的最大二进制奇数。
 * 注意 返回的结果字符串 可以 含前导零。
 * 提示：
 * 1、1 <= s.length <= 100
 * 2、s 仅由 '0' 和 '1' 组成
 * 3、s 中至少包含一个 '1'
 * 链接：https://leetcode.cn/problems/maximum-odd-binary-number/
"""
from collections import Counter


class Solution:

    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = Counter(s)
        return ''.join(['1'] * (cnt['1'] - 1) + ['0'] * cnt['0'] + ['1'])


if __name__ == '__main__':
    # "001"
    print(Solution().maximumOddBinaryNumber('010'))
    # "1001"
    print(Solution().maximumOddBinaryNumber('0101'))