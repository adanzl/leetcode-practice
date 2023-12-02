"""
 * 车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）
 * 给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengers_i, from_i, to_i] 表示第 i 次旅行有 numPassengers_i 乘客，
 * 接他们和放他们的位置分别是 from_i 和 to_i 。这些位置是从汽车的初始位置向东的公里数。
 * 当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。
 * 提示：
 * 1、1 <= trips.length <= 1000
 * 2、trips[i].length == 3
 * 3、1 <= numPassengers_i <= 100
 * 4、0 <= from_i < to_i <= 1000
 * 5、1 <= capacity <= 10^5
 * 链接：https://leetcode.cn/problems/car-pooling
"""
from typing import List


class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cnt = [0] * 1001
        for num, f, t in trips:
            for i in range(f, t):
                cnt[i] += num
                if cnt[i] > capacity:
                    return False
        return True


if __name__ == '__main__':
    # False
    print(Solution().carPooling([[2, 1, 5], [3, 3, 7]], capacity=4))
    # True
    print(Solution().carPooling([[2, 1, 5], [3, 3, 7]], capacity=5))
