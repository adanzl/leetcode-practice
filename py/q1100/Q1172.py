"""
 * 我们把无限数量 ∞ 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量 capacity 都相同。
 * 实现一个叫「餐盘」的类 DinnerPlates：
 * 1、DinnerPlates(int capacity) - 给出栈的最大容量 capacity。
 * 2、void push(int val) - 将给出的正整数 val 推入 从左往右第一个 没有满的栈。
 * 3、int pop() - 返回 从右往左第一个 非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回 -1。
 * 4、int popAtStack(int index) - 返回编号 index 的栈顶部的值，并将其从栈中删除；如果编号 index 的栈是空的，请返回 -1。
 * 提示：
 * 1、1 <= capacity <= 20000
 * 2、1 <= val <= 20000
 * 3、0 <= index <= 100000
 * 4、最多会对 push，pop，和 popAtStack 进行 200000 次调用。
 * 链接：https:# leetcode.cn/problems/dinner-plate-stacks/
"""

from heapq import heappop, heappush


class DinnerPlates:

    def __init__(self, capacity: int):
        self.s = []
        self.capacity = capacity
        self.q = []

    def push(self, val: int) -> None:
        while self.q and self.q[0] >= len(self.s):
            heappop(self.q)
        if len(self.q) == 0:
            idx = len(self.s)
            self.s.append([val])
            if self.capacity > 1:
                heappush(self.q, idx)
        else:
            idx = self.q[0]
            self.s[idx].append(val)
            if len(self.s[idx]) == self.capacity:
                heappop(self.q)

    def pop(self) -> int:
        if len(self.s) == 0: return -1
        if len(self.s[-1]) == self.capacity and self.capacity > 1:
            heappush(self.q, len(self.s) - 1)
        ret = self.s[-1].pop()
        while self.s and len(self.s[-1]) == 0:
            self.s.pop()
        return ret

    def popAtStack(self, index: int) -> int:
        if index >= len(self.s): return -1
        if len(self.s[index]) == 0: return -1
        if len(self.s[index]) == self.capacity:
            heappush(self.q, index)
        ret = self.s[index].pop()
        while self.s and len(self.s[-1]) == 0:
            self.s.pop()
        return ret


if __name__ == '__main__':
    D = DinnerPlates(2)  #  初始化，栈最大容量 capacity = 2
    D.push(1)
    D.push(2)
    D.push(3)
    D.push(4)
    D.push(5)
    print(D.popAtStack(0))  # 2
    D.push(20)
    D.push(21)
    print(D.popAtStack(0))  # 20
    print(D.popAtStack(2))  # 21
    print(D.pop())  # 5
    print(D.pop())  # 4
    print(D.pop())  # 3
    print(D.pop())  # 1。现在没有栈。
    print(D.pop())  # -1。仍然没有栈。
