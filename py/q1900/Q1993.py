"""
 * 给你一棵 n 个节点的树，编号从 0 到 n - 1 ，以父节点数组 parent 的形式给出，其中 parent[i] 是第 i 个节点的父节点。
 * 树的根节点为 0 号节点，所以 parent[0] = -1 ，因为它没有父节点。你想要设计一个数据结构实现树里面对节点的加锁，解锁和升级操作。
 * 数据结构需要支持如下函数：
 * 1、Lock：指定用户给指定节点 上锁 ，上锁后其他用户将无法给同一节点上锁。只有当节点处于未上锁的状态下，才能进行上锁操作。
 * 2、Unlock：指定用户给指定节点 解锁 ，只有当指定节点当前正被指定用户锁住时，才能执行该解锁操作。
 * 3、Upgrade：指定用户给指定节点 上锁 ，并且将该节点的所有子孙节点 解锁 。只有如下 3 个条件 全部 满足时才能执行升级操作：
 *      (1) 指定节点当前状态为未上锁。
 *      (2) 指定节点至少有一个上锁状态的子孙节点（可以是 任意 用户上锁的）。
 *      (3) 指定节点没有任何上锁的祖先节点。
 * 请你实现 LockingTree 类：
 * 1、LockingTree(int[] parent) 用父节点数组初始化数据结构。
 * 2、lock(int num, int user) 如果 id 为 user 的用户可以给节点 num 上锁，那么返回 true ，否则返回 false 。
 *      如果可以执行此操作，节点 num 会被 id 为 user 的用户 上锁 。
 * 3、unlock(int num, int user) 如果 id 为 user 的用户可以给节点 num 解锁，那么返回 true ，否则返回 false 。
 *      如果可以执行此操作，节点 num 变为 未上锁 状态。
 * 4、upgrade(int num, int user) 如果 id 为 user 的用户可以给节点 num 升级，那么返回 true ，否则返回 false 。
 *      如果可以执行此操作，节点 num 会被 升级 。
 * 提示：
 * 1、n == parent.length
 * 2、2 <= n <= 2000
 * 3、对于 i != 0 ，满足 0 <= parent[i] <= n - 1
 * 4、parent[0] == -1
 * 5、0 <= num <= n - 1
 * 6、1 <= user <= 10^4
 * 7、parent 表示一棵合法的树。
 * 8、lock ，unlock 和 upgrade 的调用 总共 不超过 2000 次。
 * 链接：https://leetcode.cn/problems/operations-on-tree
"""

from collections import Counter, defaultdict
from typing import List

#
# @lc app=leetcode.cn id=1993 lang=python3
#
# [1993] 树上的操作
#


# @lc code=start
class LockingTree:

    def __init__(self, parent: List[int]):
        self.locker = defaultdict(lambda: -1)
        self.parent = parent
        self.lock_sub = Counter()
        self.g = defaultdict(list)
        for i, p in enumerate(parent):
            self.g[p].append(i)

    def lock(self, num: int, user: int) -> bool:
        ret = self.locker[num] == -1
        if ret:
            self.locker[num] = user
            v = num
            while v != -1:
                self.lock_sub[v] += 1
                v = self.parent[v]
        return ret

    def unlock(self, num: int, user: int) -> bool:
        ret = self.locker[num] == user
        if ret:
            self.locker[num] = -1
            v = num
            while v != -1:
                self.lock_sub[v] -= 1
                v = self.parent[v]
        return ret

    def upgrade(self, num: int, user: int) -> bool:
        ret = self.locker[num] == -1
        ret &= self.lock_sub[num] != 0
        v = num
        while v != -1 and ret:
            ret &= self.locker[v] == -1
            v = self.parent[v]
        if ret:
            q = [num]
            while q:
                v = q.pop(0)
                self.locker[v] = -1
                self.lock_sub[v] = 0
                for nx in self.g[v]:
                    q.append(nx)
            self.locker[num] = user
        return ret


# @lc code=end

if __name__ == '__main__':
    obj = LockingTree([-1, 0, 0, 1, 1, 2, 2])
    print(obj.lock(2, 2))  # True
    print(obj.unlock(2, 3))  # False
    print(obj.unlock(2, 2))  # True
    print(obj.lock(4, 5))  # True
    print(obj.upgrade(0, 1))  # True
    print(obj.lock(0, 1))  # False
