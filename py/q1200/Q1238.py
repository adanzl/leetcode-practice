"""
 * 给你两个整数 n 和 start。你的任务是返回任意 (0,1,2,,...,2^n-1) 的排列 p，并且满足：
 * 1、p[0] = start
 * 2、p[i] 和 p[i+1] 的二进制表示形式只有一位不同
 * 3、p[0] 和 p[2^n -1] 的二进制表示形式也只有一位不同
 * 提示：
 * 1、1 <= n <= 16
 * 2、0 <= start < 2^n
 * 链接：https://leetcode.cn/problems/circular-permutation-in-binary-representation/
"""
from typing import List


class Solution:

    def circularPermutation(self, n: int, start: int) -> List[int]:
        # 格雷码 x ^ (x >> 1) ， 再与首元素异或
        return [i ^ (i >> 1) ^ start for i in range(1 << n)]


if __name__ == '__main__':
    #
    print(Solution().circularPermutation(2, start=3))
    #
    print(Solution().circularPermutation(3, start=2))