"""
 * 你打算构建一些障碍赛跑路线。给你一个 下标从 0 开始 的整数数组 obstacles ，数组长度为 n ，其中 obstacles[i] 表示第 i 个障碍的高度。
 * 对于每个介于 0 和 n - 1 之间（包含 0 和 n - 1）的下标  i ，在满足下述条件的前提下，请你找出 obstacles 能构成的最长障碍路线的长度：
 * 1、你可以选择下标介于 0 到 i 之间（包含 0 和 i）的任意个障碍。
 * 2、在这条路线中，必须包含第 i 个障碍。
 * 3、你必须按障碍在 obstacles 中的 出现顺序 布置这些障碍。
 * 4、除第一个障碍外，路线中每个障碍的高度都必须和前一个障碍 相同 或者 更高 。
 * 返回长度为 n 的答案数组 ans ，其中 ans[i] 是上面所述的下标 i 对应的最长障碍赛跑路线的长度。
 * 提示：
 * 1、n == obstacles.length
 * 2、1 <= n <= 10^5
 * 3、1 <= obstacles[i] <= 10^7
 * 链接：https://leetcode.cn/problems/find-the-longest-valid-obstacle-course-at-each-position/
"""
from bisect import bisect_right
from typing import List


# 树状数组 下标从 1 开始，求max
class BIT:

    def __init__(self, n):
        self.tree = [0] * n

    def add(self, i, val):
        while i < len(self.tree):
            self.tree[i] = max(self.tree[i], val)
            i += i & -i  # low_bit

    def query(self, i):
        res = 0
        while i > 0:
            res = max(self.tree[i], res)
            i &= i - 1
        return res


class Solution:

    def longestObstacleCourseAtEachPosition1(self, obstacles: List[int]) -> List[int]:
        t = BIT(max(obstacles) + 1)
        n = len(obstacles)
        ans = [0] * n
        for i, o in enumerate(obstacles):
            v = t.query(o) + 1
            ans[i] = v
            t.add(o, v)
        return ans

    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        d = list()
        ans = list()
        for ob in obstacles:
            # 这里需要改成 >=
            if not d or ob >= d[-1]:
                d.append(ob)
                ans.append(len(d))
            else:
                # 将 300 题解中的二分查找改为 API 调用使得代码更加直观
                # 如果是最长严格递增子序列，这里是 bisect_left
                # 如果是最长递增子序列，这里是 bisect_right
                loc = bisect_right(d, ob)
                ans.append(loc + 1)
                d[loc] = ob

        return ans


if __name__ == '__main__':
    # [1,1,2,3,2,2]
    print(Solution().longestObstacleCourseAtEachPosition([3, 1, 5, 6, 4, 2]))
    # [1,2,3,3]
    print(Solution().longestObstacleCourseAtEachPosition([1, 2, 3, 2]))
    # [1,2,1]
    print(Solution().longestObstacleCourseAtEachPosition([2, 2, 1]))
