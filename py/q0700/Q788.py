"""
 * 我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。
 * 如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；
 * 2 和 5 可以互相旋转成对方（在这种情况下，它们以不同的方向旋转，换句话说，2 和 5 互为镜像）；
 * 6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。
 * 现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？
 * 提示：N 的取值范围是 [1, 10000]。
 * 链接：https://leetcode.cn/problems/rotated-digits/
"""


class Solution:

    def rotatedDigits(self, n: int) -> int:
        ans = 0
        ex = ['3', '4', '7']
        include = ['2', '5', '6', '9']
        for i in range(n):
            b_skip, b_in = False, False
            for n in str(i + 1):
                if n in ex:
                    b_skip = True
                    break
                if n in include:
                    b_in = True
            if not b_skip and b_in:
                ans += 1
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().rotatedDigits(10))
    # 0
    print(Solution().rotatedDigits(1))
    # 1
    print(Solution().rotatedDigits(2))