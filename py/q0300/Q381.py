"""
 * RandomizedCollection 是一种包含数字集合(可能是重复的)的数据结构。它应该支持插入和删除特定元素，以及删除随机元素。
 * 实现 RandomizedCollection 类:
 * 1、RandomizedCollection()初始化空的 RandomizedCollection 对象。
 * 2、bool insert(int val) 将一个 val 项插入到集合中，即使该项已经存在。如果该项不存在，则返回 true ，否则返回 false 。
 * 3、bool remove(int val) 如果存在，从集合中移除一个 val 项。如果该项存在，则返回 true ，否则返回 false 。注意，如果 val 在集合中出现多次，我们只删除其中一个。
 * 4、int getRandom() 从当前的多个元素集合中返回一个随机元素。每个元素被返回的概率与集合中包含的相同值的数量 线性相关 。
 * 您必须实现类的函数，使每个函数的 平均 时间复杂度为 O(1) 。
 * 注意：生成测试用例时，只有在 RandomizedCollection 中 至少有一项 时，才会调用 getRandom 。
 * 提示:
 * 1、-2^31 <= val <= 2^31 - 1
 * 2、insert, remove 和 getRandom 最多 总共 被调用 2 * 10^5 次
 * 3、当调用 getRandom 时，数据结构中 至少有一个 元素
 * 链接：https://leetcode.cn/problems/insert-delete-getrandom-o1-duplicates-allowed/
"""

from collections import defaultdict
import math
import random

#
# @lc app=leetcode.cn id=381 lang=python3
#
# [381] O(1) 时间插入、删除和获取随机元素 - 允许重复
#

# @lc code=start
data = [0] * (10**5 + 5)


class RandomizedCollection:

    def __init__(self):
        self.ids = defaultdict(set)
        self.end = -1

    def insert(self, val: int) -> bool:
        ret = len(self.ids[val]) == 0  # true if not exist
        self.ids[val].add(self.end + 1)
        data[self.end + 1] = val
        self.end += 1
        return ret

    def remove(self, val: int) -> bool:
        ret = len(self.ids[val]) > 0  # true if exist
        if ret:
            v_end = data[self.end]
            v_i = self.ids[val].pop()
            if self.ids[v_end]:
                self.ids[v_end].discard(self.end)
                data[v_i] = v_end
                self.ids[v_end].add(v_i)
            self.end -= 1
        return ret

    def getRandom(self) -> int:
        return data[random.randint(0, self.end)]


# @lc code=end

if __name__ == '__main__':
    collection = RandomizedCollection()
    print(collection.insert(1))  # True
    print(collection.insert(1))  # False
    print(collection.insert(2))  # True
    print(collection.getRandom())  # 有 2/3 的概率返回 1, 1/3 的概率返回 2。
    print(collection.remove(1))  # True
    print(collection.getRandom())  # 应该返回 1 或 2，两者的可能性相同。

    collection = RandomizedCollection()
    print(collection.insert(1))  # True
    print(collection.remove(1))  # True
    print(collection.insert(1))  # True

    collection = RandomizedCollection()
    print(collection.insert(40))  # True
    print(collection.remove(30))  # False
    print(collection.getRandom())  # 40

    collection = RandomizedCollection()
    print(collection.insert(10))  # True
    print(collection.insert(10))  # False
    print(collection.insert(20))  # True
    print(collection.insert(20))  # False
    print(collection.insert(30))  # True
    print(collection.insert(30))  # False
    print(collection.remove(10))  # True
    print(collection.remove(20))  # True
    print(collection.remove(20))  # True
    print(collection.remove(10))  # True
    print(collection.remove(30))  # True
    print(collection.insert(40))  # True
    print(collection.remove(30))  # True
    print(collection.remove(30))  # False
    print(collection.getRandom())  # 40
