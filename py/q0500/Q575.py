"""
 * Alice 有 n 枚糖，其中第 i 枚糖的类型为 candyType[i] 。Alice 注意到她的体重正在增长，所以前去拜访了一位医生。
 * 医生建议 Alice 要少摄入糖分，只吃掉她所有糖的 n / 2 即可（n 是一个偶数）。
 * Alice 非常喜欢这些糖，她想要在遵循医生建议的情况下，尽可能吃到最多不同种类的糖。
 * 给你一个长度为 n 的整数数组 candyType ，返回： Alice 在仅吃掉 n / 2 枚糖的情况下，可以吃到糖的 最多 种类数。
 * 提示：
 * 1、n == candyType.length
 * 2、2 <= n <= 10^4
 * 3、n 是一个偶数
 * 4、-10^5 <= candyType[i] <= 10^5
 * 链接：https://leetcode.cn/problems/distribute-candies/
"""
from typing import Counter, List


class Solution:

    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(Counter(candyType)))


if __name__ == '__main__':
    # 3
    print(Solution().distributeCandies([1, 1, 2, 2, 3, 3]))
    # 2
    print(Solution().distributeCandies([1, 1, 2, 3]))
    # 1
    print(Solution().distributeCandies([6, 6, 6, 6]))
