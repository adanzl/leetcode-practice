"""
 * 请你设计一个支持对其元素进行增量操作的栈。
 * 实现自定义栈类 CustomStack ：
 * 1、CustomStack(int maxSize)：用 maxSize 初始化对象，maxSize 是栈中最多能容纳的元素数量。
 * 2、void push(int x)：如果栈还未增长到 maxSize ，就将 x 添加到栈顶。
 * 3、int pop()：弹出栈顶元素，并返回栈顶的值，或栈为空时返回 -1 。
 * 4、void inc(int k, int val)：栈底的 k 个元素的值都增加 val 。如果栈中元素总数小于 k ，则栈中的所有元素都增加 val 。
 * 提示：
 * 1、1 <= maxSize, x, k <= 1000
 * 2、0 <= val <= 100
 * 3、每种方法 increment，push 以及 pop 分别最多调用 1000 次
 * 链接：https://leetcode.cn/problems/design-a-stack-with-increment-operation
"""

from sys import maxsize
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=1381 lang=python3
#
# [1381] 设计一个支持增量操作的栈
#


# @lc code=start
class CustomStack:

    def __init__(self, maxSize: int):
        self.s = []
        self.mx = maxSize

    def push(self, x: int) -> None:
        if len(self.s) < self.mx:
            self.s.append(x)

    def pop(self) -> int:
        if not self.s:
            return -1
        return self.s.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.s))):
            self.s[i] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end

if __name__ == '__main__':
    #
    stk = CustomStack(3)  # 栈是空的 []
    stk.push(1)  # 栈变为 [1]
    stk.push(2)  # 栈变为 [1, 2]
    print(stk.pop())  # 返回 2 --> 返回栈顶值 2，栈变为 [1]
    stk.push(2)  # 栈变为 [1, 2]
    stk.push(3)  # 栈变为 [1, 2, 3]
    stk.push(4)  # 栈仍然是 [1, 2, 3]，不能添加其他元素使栈大小变为 4
    stk.increment(5, 100)  # 栈变为 [101, 102, 103]
    stk.increment(2, 100)  # 栈变为 [201, 202, 103]
    print(stk.pop())  # 返回 103 --> 返回栈顶值 103，栈变为 [201, 202]
    print(stk.pop())  # 返回 202 --> 返回栈顶值 202，栈变为 [201]
    print(stk.pop())  # 返回 201 --> 返回栈顶值 201，栈变为 []
    print(stk.pop())  # 返回 -1 --> 栈为空，返回 -1
