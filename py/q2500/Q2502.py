"""
 * 给你一个整数 n ，表示下标从 0 开始的内存数组的大小。所有内存单元开始都是空闲的。
 * 请你设计一个具备以下功能的内存分配器：
 * 1、分配 一块大小为 size 的连续空闲内存单元并赋 id mID 。
 * 2、释放 给定 id mID 对应的所有内存单元。
 * 注意：
 * 1、多个块可以被分配到同一个 mID 。
 * 2、你必须释放 mID 对应的所有内存单元，即便这些内存单元被分配在不同的块中。
 * 实现 Allocator 类：
 * 1、Allocator(int n) 使用一个大小为 n 的内存数组初始化 Allocator 对象。
 * 2、int allocate(int size, int mID) 找出大小为 size 个连续空闲内存单元且位于  最左侧 的块，分配并赋 id mID 。返回块的第一个下标。如果不存在这样的块，返回 -1 。
 * 3、int free(int mID) 释放 id mID 对应的所有内存单元。返回释放的内存单元数目。
 * 提示：
 * 1、1 <= n, size, mID <= 1000
 * 2、最多调用 allocate 和 free 方法 1000 次
 * 链接：https://leetcode.cn/problems/design-memory-allocator/
"""


class Allocator:

    def __init__(self, n: int):
        self.mem = [0 for i in range(n)]
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        s, e = -1, -1
        for i in range(self.n):
            if self.mem[i] != 0:
                s = i
            else:
                if i - s == size:
                    e = i
                    break
        for i in range(s + 1, e + 1):
            self.mem[i] = mID
        return (s + 1) if e != -1 else -1

    def free(self, mID: int) -> int:
        ret = 0
        for i in range(self.n):
            if self.mem[i] == mID:
                ret += 1
                self.mem[i] = 0
        return ret


if __name__ == '__main__':
    #
    loc = Allocator(10)  #  Initialize a memory array of size 10. All memory units are initially free.
    print(loc.allocate(1, 1))  #  The leftmost block's first index is 0. The memory array becomes [1,_,_,_,_,_,_,_,_,_]. We return 0.
    print(loc.allocate(1, 2))  #  The leftmost block's first index is 1. The memory array becomes [1,2,_,_,_,_,_,_,_,_]. We return 1.
    print(loc.allocate(1, 3))  #  The leftmost block's first index is 2. The memory array becomes [1,2,3,_,_,_,_,_,_,_]. We return 2.
    print(loc.free(2))  #  Free all memory units with mID 2. The memory array becomes [1,_, 3,_,_,_,_,_,_,_]. We return 1 since there is only 1 unit with mID 2.
    print(loc.allocate(3, 4))  #  The leftmost block's first index is 3. The memory array becomes [1,_,3,4,4,4,_,_,_,_]. We return 3.
    print(loc.allocate(1, 1))  #  The leftmost block's first index is 1. The memory array becomes [1,1,3,4,4,4,_,_,_,_]. We return 1.
    print(loc.allocate(1, 1))  #  The leftmost block's first index is 6. The memory array becomes [1,1,3,4,4,4,1,_,_,_]. We return 6.
    print(loc.free(1))  #  Free all memory units with mID 1. The memory array becomes [_,_,3,4,4,4,_,_,_,_]. We return 3 since there are 3 units with mID 1.
    print(loc.allocate(10, 2))  #  We can not find any free block with 10 consecutive free memory units, so we return -1.
    print(loc.free(7))  #  Free all memory units with mID 7. The memory array remains the same since there is no memory unit with mID 7. We return 0.