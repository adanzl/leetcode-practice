"""
 * 设计一个类似堆栈的数据结构，将元素推入堆栈，并从堆栈中弹出出现频率最高的元素。
 * 实现 FreqStack 类:
 * 1、FreqStack() 构造一个空的堆栈。
 * 2、void push(int val) 将一个整数 val 压入栈顶。
 * 3、int pop() 删除并返回堆栈中出现频率最高的元素。
 * 4、如果出现频率最高的元素不只一个，则移除并返回最接近栈顶的元素。
 * 提示：
 * 1、0 <= val <= 10^9
 * 2、push 和 pop 的操作数不大于 2 * 10^4。
 * 3、输入保证在调用 pop 之前堆栈中至少有一个元素。
 * 链接：https://leetcode.cn/problems/maximum-frequency-stack/
"""
from collections import Counter, defaultdict


class FreqStack:

    def __init__(self):
        self.data = []
        self.ids = defaultdict(list)
        self.cnt = Counter()
        self.top = -1

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        self.ids[self.cnt[val]].append(len(self.data))
        self.data.append(val)
        self.top = max(self.top, self.cnt[val])

    def pop(self) -> int:
        id = self.ids[self.top].pop()
        self.cnt[self.data[id]] -= 1
        while self.top >= 0 and len(self.ids[self.top]) == 0:
            self.top -= 1
        return self.data[id]


if __name__ == '__main__':
    freqStack = FreqStack()
    freqStack.push(5)  # 堆栈为 [5]
    freqStack.push(7)  # 堆栈是 [5,7]
    freqStack.push(5)  # 堆栈是 [5,7,5]
    freqStack.push(7)  # 堆栈是 [5,7,5,7]
    freqStack.push(4)  # 堆栈是 [5,7,5,7,4]
    freqStack.push(5)  # 堆栈是 [5,7,5,7,4,5]
    print(freqStack.pop())  # 返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,5,7,4]。
    print(freqStack.pop())  # 返回 7 ，因为 5 和 7 出现频率最高，但7最接近顶部。堆栈变成 [5,7,5,4]。
    print(freqStack.pop())  # 返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,4]。
    print(freqStack.pop())  # 返回 4 ，因为 4, 5 和 7 出现频率最高，但 4 是最接近顶部的。堆栈变成 [5,7]。
