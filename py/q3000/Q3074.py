"""
 * 给你一个长度为 n 的数组 apple 和另一个长度为 m 的数组 capacity 。
 * 一共有 n 个包裹，其中第 i 个包裹中装着 apple[i] 个苹果。同时，还有 m 个箱子，第 i 个箱子的容量为 capacity[i] 个苹果。
 * 请你选择一些箱子来将这 n 个包裹中的苹果重新分装到箱子中，返回你需要选择的箱子的 最小 数量。
 * 注意，同一个包裹中的苹果可以分装到不同的箱子中。
 * 提示：
 * 1、1 <= n == apple.length <= 50
 * 2、1 <= m == capacity.length <= 50
 * 3、1 <= apple[i], capacity[i] <= 50
 * 4、输入数据保证可以将包裹中的苹果重新分装到箱子中。
 * 链接：https://leetcode.cn/problems/apple-redistribution-into-boxes/
"""
from typing import List


class Solution:

    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sm = 0
        ans = 0
        for num in sorted(capacity, reverse=True):
            if sm >= sum(apple):
                break
            sm += num
            ans += 1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().minimumBoxes([1, 3, 2], capacity=[4, 3, 1, 5, 2]))
    # 4
    print(Solution().minimumBoxes([5, 5, 5], capacity=[2, 4, 2, 7]))
    #
    # print(Solution().minimumBoxes())
