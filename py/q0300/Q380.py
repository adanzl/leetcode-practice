"""
 * 设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。
 * 1、insert(val)：当元素 val 不存在时，向集合中插入该项。
 * 2、remove(val)：元素 val 存在时，从集合中移除该项。
 * 3、getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
 * 链接：https://leetcode-cn.com/problems/insert-delete-getrandom-o1
"""


import random


class RandomizedSet:

    def __init__(self):
        self.d_i = {}
        self.i_d = {}

    def insert(self, val: int) -> bool:
        if val in self.d_i: return False
        self.d_i[val] = len(self.d_i)
        self.i_d[len(self.i_d)] = val
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d_i: return False
        i = self.d_i[val]
        self.d_i[self.i_d[len(self.i_d) - 1]] = i
        self.i_d[i] = self.i_d[len(self.i_d) - 1]
        del self.i_d[len(self.i_d) - 1]
        del self.d_i[val]
        return True

    def getRandom(self) -> int:
        return self.i_d[random.randint(0, len(self.i_d) - 1)]


if __name__ == '__main__':
    obj = RandomizedSet()
    print(obj.insert(0))  # true
    print(obj.insert(1))  # true
    print(obj.remove(0))  # true
    print(obj.insert(2))  # true
    print(obj.remove(1))  # true
    print(obj.getRandom())  # 2