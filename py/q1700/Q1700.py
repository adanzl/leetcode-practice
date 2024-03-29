"""
 * 学校的自助午餐提供圆形和方形的三明治，分别用数字 0 和 1 表示。所有学生站在一个队列里，每个学生要么喜欢圆形的要么喜欢方形的。
 * 餐厅里三明治的数量与学生的数量相同。所有三明治都放在一个 栈 里，每一轮：
 * 1、如果队列最前面的学生 喜欢 栈顶的三明治，那么会 拿走它 并离开队列。
 * 2、否则，这名学生会 放弃这个三明治 并回到队列的尾部。
 * 这个过程会一直持续到队列里所有学生都不喜欢栈顶的三明治为止。
 * 给你两个整数数组 students 和 sandwiches ，其中 sandwiches[i] 是栈里面第 i​​​​​​ 个三明治的类型（i = 0 是栈的顶部）， 
 * students[j] 是初始队列里第 j​​​​​​ 名学生对三明治的喜好（j = 0 是队列的最开始位置）。请你返回无法吃午餐的学生数量。
 * 提示：
 * 1、1 <= students.length, sandwiches.length <= 100
 * 2、students.length == sandwiches.length
 * 3、sandwiches[i] 要么是 0 ，要么是 1 。
 * 4、students[i] 要么是 0 ，要么是 1 。
 * 链接：https://leetcode.cn/problems/number-of-students-unable-to-eat-lunch/
"""
from typing import List, Deque


class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        qst, qsa = Deque(students), Deque(sandwiches)
        idx = 0
        while idx < len(qst):
            while qsa and qst[0] == qsa[0]:
                idx = 0
                qst.popleft()
                qsa.popleft()
            if qst:
                qst.append(qst.popleft())
                idx += 1
        return len(qst)


if __name__ == '__main__':
    # 0
    print(Solution().countStudents([1, 1, 0, 0], [0, 1, 0, 1]))
    # 3
    print(Solution().countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
