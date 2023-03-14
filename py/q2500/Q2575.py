"""
 * 给你一个下标从 0 开始的字符串 word ，长度为 n ，由从 0 到 9 的数字组成。另给你一个正整数 m 。
 * word 的 可整除数组 div 是一个长度为 n 的整数数组，并满足：
 * 1、如果 word[0,...,i] 所表示的 数值 能被 m 整除，div[i] = 1
 * 2、否则，div[i] = 0
 * 返回 word 的可整除数组。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、word.length == n
 * 3、word 由数字 0 到 9 组成
 * 4、1 <= m <= 10^9
 * 链接：https://leetcode.cn/problems/find-the-divisibility-array-of-a-string/
"""
from typing import List


class Solution:

    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        ans = [0] * n
        r = 0
        for i in range(n):
            r = (r * 10 + int(word[i])) % m
            if r == 0:
                ans[i] = 1
        return ans


if __name__ == '__main__':
    # [1,1,0,0,0,1,1,0,0]
    print(Solution().divisibilityArray("998244353", m=3))
    # [0,1,0,1]
    print(Solution().divisibilityArray("1010", m=10))
