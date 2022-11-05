"""
 * 给你两个正整数 n 和 target 。
 * 如果某个整数每一位上的数字相加小于或等于 target ，则认为这个整数是一个 美丽整数 。
 * 找出并返回满足 n + x 是 美丽整数 的最小非负整数 x 。生成的输入保证总可以使 n 变成一个美丽整数。
 * 提示：
 * 1、1 <= n <= 10^12
 * 2、1 <= target <= 150
 * 3、生成的输入保证总可以使 n 变成一个美丽整数。
 * 链接：https://leetcode.cn/problems/minimum-addition-to-make-integer-beautiful/
"""


class Solution:

    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        num = n

        def sm(num):
            ret = 0
            while num:
                ret += num % 10
                num //= 10
            return ret

        for i in range(len(str(n)) + 2):
            if sm(num) <= target: break
            num -= num % (10**(i + 1))
            num += 10**(i + 1)
        return num - n


if __name__ == '__main__':
    # 4
    print(Solution().makeIntegerBeautiful(16, 6))
    # 33
    print(Solution().makeIntegerBeautiful(467, 6))
    # 0
    print(Solution().makeIntegerBeautiful(1, 1))
