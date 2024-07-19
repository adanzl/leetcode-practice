"""
 * 给你一个正整数 n。
 * 如果一个二进制字符串 x 的所有长度为 2 的 子字符串 中包含 至少 一个 "1"，则称 x 是一个 有效 字符串。
 * 返回所有长度为 n 的 有效 字符串，可以以任意顺序排列。
 * 提示：1 <= n <= 18
 * 链接：https://leetcode.cn/problems/generate-binary-strings-without-adjacent-zeros/
"""
from typing import List


class Solution:

    def validStrings(self, n: int) -> List[str]:
        ans = set()
        for num in range(1 << n):
            v = num & 3
            ss = bin(num)[2:].zfill(n)
            num >>= 2
            for _ in range(n - 1):
                if v == 0: break
                v = (v >> 1) + (num & 1) * 2
                num >>= 1
            else:
                ans.add(ss)
        return list(ans)


if __name__ == '__main__':
    # ["010","011","101","110","111"]
    print(Solution().validStrings(3))
    # ["0","1"]
    print(Solution().validStrings(1))
