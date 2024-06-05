"""
 * 请你实现三个 API append，addAll 和 multAll 来实现奇妙序列。
 * 请实现 Fancy 类 ：
 * 1、Fancy() 初始化一个空序列对象。
 * 2、void append(val) 将整数 val 添加在序列末尾。
 * 3、void addAll(inc) 将所有序列中的现有数值都增加 inc 。
 * 4、void multAll(m) 将序列中的所有现有数值都乘以整数 m 。
 * 5、int getIndex(idx) 得到下标为 idx 处的数值（下标从 0 开始），并将结果对 10^9 + 7 取余。如果下标大于等于序列的长度，请返回 -1 。
 * 提示：
 * 1、1 <= val, inc, m <= 100
 * 2、0 <= idx <= 10^5
 * 3、总共最多会有 10^5 次对 append，addAll，multAll 和 getIndex 的调用。
 * 链接：https://leetcode.cn/problems/fancy-sequence/
"""

#
# @lc app=leetcode.cn id=1622 lang=python3
#
# [1622] 奇妙序列
#

# @lc code=start
MOD = 10**9 + 7
inv = [0] + [pow(m, -1, MOD) for m in range(1, 101)]


class Fancy:

    def __init__(self):
        self.vals = []
        self.add_base = 0
        self.mul_base = 1
        self.a_mul_base = 1

    def append(self, val: int) -> None:
        self.vals.append((val - self.add_base) * self.a_mul_base)

    def addAll(self, inc: int) -> None:
        self.add_base += inc

    def multAll(self, m: int) -> None:
        self.add_base = self.add_base * m % MOD
        self.mul_base = self.mul_base * m % MOD
        self.a_mul_base = self.a_mul_base * inv[m] % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.vals): return -1
        return (self.mul_base * self.vals[idx] + self.add_base) % MOD


# @lc code=end

if __name__ == '__main__':
    #
    fancy = Fancy()
    fancy.append(2)  # 奇妙序列：[2]
    fancy.addAll(3)  # 奇妙序列：[2+3] -> [5]
    fancy.append(7)  # 奇妙序列：[5, 7]
    fancy.multAll(2)  # 奇妙序列：[5*2, 7*2] -> [10, 14]
    print(fancy.getIndex(0))  # 返回 10
    fancy.addAll(3)  # 奇妙序列：[10+3, 14+3] -> [13, 17]
    fancy.append(10)  # 奇妙序列：[13, 17, 10]
    fancy.multAll(2)  # 奇妙序列：[13*2, 17*2, 10*2] -> [26, 34, 20]
    print(fancy.getIndex(0))  # 返回 26
    print(fancy.getIndex(1))  # 返回 34
    print(fancy.getIndex(2))  # 返回 20
