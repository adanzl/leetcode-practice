"""
 * 给你一个用字符串表示的正整数 num ，请你以字符串形式返回不含尾随零的整数 num 。
 * 提示：
 * 1、1 <= num.length <= 1000
 * 2、num 仅由数字 0 到 9 组成
 * 3、num 不含前导零
 * 链接：https://leetcode.cn/problems/remove-trailing-zeros-from-a-string/
"""


class Solution:

    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')


if __name__ == '__main__':
    # "512301"
    print(Solution().removeTrailingZeros("51230100"))
    # "123"
    print(Solution().removeTrailingZeros("123"))