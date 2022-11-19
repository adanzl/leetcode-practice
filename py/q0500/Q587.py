"""
 * 在一个二维的花园中，有一些用 (x, y) 坐标表示的树。由于安装费用十分昂贵，你的任务是先用最短的绳子围起所有的树。
 * 只有当所有的树都被绳子包围时，花园才能围好栅栏。你需要找到正好位于栅栏边界上的树的坐标。
 * 注意:
 * 1、所有的树应当被围在一起。你不能剪断绳子来包围树或者把树分成一组以上。
 * 2、输入的整数在 0 到 100 之间。
 * 3、花园至少有一棵树。
 * 4、所有树的坐标都是不同的。
 * 5、输入的点没有顺序。输出顺序也没有要求。
 * 链接：https://leetcode-cn.com/problems/erect-the-fence
"""
from functools import cmp_to_key
from typing import List


class Solution:

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:

        # Graham 算法
        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        def distance(p: List[int], q: List[int]) -> int:
            return (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])

        n = len(trees)
        if n < 4:
            return trees

        # 找到 y 最小的点 bottom
        bottom = 0
        for i, tree in enumerate(trees):
            if tree[1] < trees[bottom][1]:
                bottom = i
        trees[bottom], trees[0] = trees[0], trees[bottom]

        # 以 bottom 原点，按照极坐标的角度大小进行排序
        def cmp(a: List[int], b: List[int]) -> int:
            diff = -cross(trees[0], a, b)
            return diff if diff else distance(trees[0], a) - distance(trees[0], b)

        trees[1:] = sorted(trees[1:], key=cmp_to_key(cmp))

        # 对于凸包最后且在同一条直线的元素按照距离从大到小进行排序
        r = n - 1
        while r >= 0 and cross(trees[0], trees[n - 1], trees[r]) == 0:
            r -= 1
        l, h = r + 1, n - 1
        while l < h:
            trees[l], trees[h] = trees[h], trees[l]
            l += 1
            h -= 1

        stack = [0, 1]
        for i in range(2, n):
            # 如果当前元素与栈顶的两个元素构成的向量顺时针旋转，则弹出栈顶元素
            while len(stack) > 1 and cross(trees[stack[-2]], trees[stack[-1]], trees[i]) < 0:
                stack.pop()
            stack.append(i)
        return [trees[i] for i in stack]


if __name__ == '__main__':
    # [[1,1],[2,0],[4,2],[3,3],[2,4]]
    print(Solution().outerTrees([[1, 1], [2, 2], [4, 2], [2, 0], [2, 4], [3, 3]]))
    # [[1,2],[2,2],[4,2]]
    print(Solution().outerTrees([[1, 2], [2, 2], [4, 2]]))
