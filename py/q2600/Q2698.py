"""
 * 给你一个正整数 n ，请你返回 n 的 惩罚数 。
 * n 的 惩罚数 定义为所有满足以下条件 i 的数的平方和：
 * 1、1 <= i <= n
 * 2、i * i 的十进制表示的字符串可以分割成若干连续子字符串，且这些子字符串对应的整数值之和等于 i 。
 * 提示：1 <= n <= 1000
 * 链接：https://leetcode.cn/problems/find-the-punishment-number-of-an-integer/
"""

# 预处理
mem = set()


def func(num, v):
    if num == v: return True
    for i in range(1, len(str(num))):
        vv = int(str(num)[:i])
        if vv > v: return False
        if func(int(str(num)[i:]), v - vv):
            return True
    return False


for i in range(1, 1001):
    if func(i * i, i):
        mem.add(i)


class Solution:

    def punishmentNumber(self, n: int) -> int:

        ans = 0
        for i in range(1, n + 1):
            if i in mem:
                ans += i * i
        return ans


if __name__ == '__main__':
    # 182
    print(Solution().punishmentNumber(10))
    # 1478
    print(Solution().punishmentNumber(37))
    #
    # print(Solution().punishmentNumber())