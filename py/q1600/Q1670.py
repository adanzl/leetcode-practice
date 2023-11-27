"""
 * 请你设计一个队列，支持在前，中，后三个位置的 push 和 pop 操作。
 * 请你完成 FrontMiddleBack 类：
 * 1、FrontMiddleBack() 初始化队列。
 * 2、void pushFront(int val) 将 val 添加到队列的 最前面 。
 * 3、void pushMiddle(int val) 将 val 添加到队列的 正中间 。
 * 4、void pushBack(int val) 将 val 添加到队里的 最后面 。
 * 5、int popFront() 将 最前面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。
 * 6、int popMiddle() 将 正中间 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。
 * 7、int popBack() 将 最后面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。
 * 请注意当有 两个 中间位置的时候，选择靠前面的位置进行操作。比方说：
 * 将 6 添加到 [1, 2, 3, 4, 5] 的中间位置，结果数组为 [1, 2, 6, 3, 4, 5] 。
 * 从 [1, 2, 3, 4, 5, 6] 的中间位置弹出元素，返回 3 ，数组变为 [1, 2, 4, 5, 6] 。
 * 提示：
 * 1、1 <= val <= 10^9
 * 2、最多调用 1000 次 pushFront， pushMiddle， pushBack， popFront， popMiddle 和 popBack 。
 * 链接：https://leetcode.cn/problems/design-front-middle-back-queue
"""


class FrontMiddleBackQueue:

    def __init__(self):
        self.arr = []

    def pushFront(self, val: int) -> None:
        self.arr.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        self.arr.insert(len(self.arr) // 2, val)

    def pushBack(self, val: int) -> None:
        self.arr.append(val)

    def popFront(self) -> int:
        return self.arr.pop(0) if self.arr else -1

    def popMiddle(self) -> int:
        l = len(self.arr)
        if l == 0: return -1
        return self.arr.pop(l // 2) if l & 1 else self.arr.pop(l // 2 - 1)

    def popBack(self) -> int:
        return self.arr.pop() if self.arr else -1


if __name__ == '__main__':
    #
    q = FrontMiddleBackQueue()
    q.pushFront(1)  # [1]
    q.pushBack(2)  # [1, 2]
    q.pushMiddle(3)  # [1, 3, 2]
    q.pushMiddle(4)  # [1, 4, 3, 2]
    print(q.popFront())  # 返回 1 -> [4, 3, 2]
    print(q.popMiddle())  # 返回 3 -> [4, 2]
    print(q.popMiddle())  # 返回 4 -> [2]
    print(q.popBack())  # 返回 2 -> []
    print(q.popFront())  # 返回 -1 -> [] （队列为空）
