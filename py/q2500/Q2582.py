"""
 * n 个人站成一排，按从 1 到 n 编号。
 * 最初，排在队首的第一个人拿着一个枕头。每秒钟，拿着枕头的人会将枕头传递给队伍中的下一个人。一旦枕头到达队首或队尾，传递方向就会改变，队伍会继续沿相反方向传递枕头。
 * 例如，当枕头到达第 n 个人时，TA 会将枕头传递给第 n - 1 个人，然后传递给第 n - 2 个人，依此类推。
 * 给你两个正整数 n 和 time ，返回 time 秒后拿着枕头的人的编号。
 * 提示：
 * 1、2 <= n <= 1000
 * 2、1 <= time <= 1000
 * 链接：https://leetcode.cn/problems/pass-the-pillow/
"""


class Solution:

    def passThePillow(self, n: int, time: int) -> int:
        a, r = divmod(time, n - 1)
        return n - r if a & 1 else (r + 1)


if __name__ == '__main__':
    # 5
    print(Solution().passThePillow(9, 4))
    # 2
    print(Solution().passThePillow(4, 5))
    # 3
    print(Solution().passThePillow(3, 2))
    # 6
    print(Solution().passThePillow(8, 9))
