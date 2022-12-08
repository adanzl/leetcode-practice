"""
 * 给你一个整数 n ，如果你可以将 n 表示成若干个不同的三的幂之和，请你返回 true ，否则请返回 false 。
 * 对于一个整数 y ，如果存在整数 x 满足 y == 3x ，我们称这个整数 y 是三的幂。
 * 提示：1 <= n <= 10^7
 * 链接：https://leetcode.cn/problems/check-if-number-is-a-sum-of-powers-of-three/submissions/
"""


class Solution:

    def checkPowersOfThree(self, n: int) -> bool:
        arr = [0]
        num = 1
        while num <= n:
            for i in range(len(arr)):
                arr.append(arr[i] + num)
            num *= 3
        return n in arr


if __name__ == '__main__':
    # False
    print(Solution().checkPowersOfThree(11))
    # True
    print(Solution().checkPowersOfThree(12))
    # True
    print(Solution().checkPowersOfThree(91))
    # False
    print(Solution().checkPowersOfThree(21))