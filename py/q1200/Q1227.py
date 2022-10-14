"""
 * 有 n 位乘客即将登机，飞机正好有 n 个座位。第一位乘客的票丢了，他随便选了一个座位坐下。
 * 剩下的乘客将会：
 * 1、如果他们自己的座位还空着，就坐到自己的座位上，
 * 2、当他们自己的座位被占用时，随机选择其他座位
 * 第 n 位乘客坐在自己的座位上的概率是多少？
 * 提示：1 <= n <= 10^5
 * 链接：https://leetcode.cn/problems/airplane-seat-assignment-probability/
"""
from typing import List


class Solution:

    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1 if n == 1 else 0.5


if __name__ == '__main__':
    # 1.00
    print(Solution().nthPersonGetsNthSeat(1))
    # 0.50
    print(Solution().nthPersonGetsNthSeat(2))
    #
    print(Solution().nthPersonGetsNthSeat(100000))