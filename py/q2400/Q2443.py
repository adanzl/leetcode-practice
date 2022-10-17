"""
 * 给你一个 非负 整数 num 。如果存在某个 非负 整数 k 满足 k + reverse(k) = num  ，则返回 true ；否则，返回 false 。
 * reverse(k) 表示 k 反转每个数位后得到的数字。
 * 提示：0 <= num <= 10^5
 * 链接：https://leetcode.cn/problems/sum-of-number-and-its-reverse/
"""


class Solution:

    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num + 1):
            if int(str(i)[::-1]) + i == num: return True
        return False


if __name__ == '__main__':
    # True
    print(Solution().sumOfNumberAndReverse(443))
    # False
    print(Solution().sumOfNumberAndReverse(63))
    # True
    print(Solution().sumOfNumberAndReverse(181))