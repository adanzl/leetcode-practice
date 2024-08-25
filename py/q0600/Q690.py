"""
 * 你有一个保存员工信息的数据结构，它包含了员工唯一的 id ，重要度和直系下属的 id 。
 * 给定一个员工数组 employees，其中：
 * 1、employees[i].id 是第 i 个员工的 ID。
 * 2、employees[i].importance 是第 i 个员工的重要度。
 * 3、employees[i].subordinates 是第 i 名员工的直接下属的 ID 列表。
 * 给定一个整数 id 表示一个员工的 ID，返回这个员工和他所有下属的重要度的 总和。
 * 提示：
 * 1、1 <= employees.length <= 2000
 * 2、1 <= employees[i].id <= 2000
 * 3、所有的 employees[i].id 互不相同。
 * 4、-100 <= employees[i].importance <= 100
 * 5、一名员工最多有一名直接领导，并可能有多名下属。
 * 6、employees[i].subordinates 中的 ID 都有效。
 * 链接：https://leetcode.cn/problems/employee-importance/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Employee:

    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ans, n = 0, len(employees)
        g = [[] for _ in range(2001)]
        score = [0] * 2001
        for e in employees:
            score[e.id - 1] = e.importance
            for sub in e.subordinates:
                g[e.id - 1].append(sub - 1)

        def dfs(idx):
            nonlocal ans
            ans += score[idx]
            for sub in g[idx]:
                dfs(sub)

        dfs(id - 1)
        return ans
