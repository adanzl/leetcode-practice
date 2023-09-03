"""
 * 给你两个字符串 s1 和 s2 ，两个字符串长度都为 n ，且只包含 小写 英文字母。
 * 你可以对两个字符串中的 任意一个 执行以下操作 任意 次：
 * 选择两个下标 i 和 j ，满足 i < j 且 j - i 是 偶数，然后 交换 这个字符串中两个下标对应的字符。
 * 如果你可以让字符串 s1 和 s2 相等，那么返回 true ，否则返回 false 。
 * 提示：
 * 1、n == s1.length == s2.length
 * 2、1 <= n <= 10^5
 * 3、s1 和 s2 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/check-if-strings-can-be-made-equal-with-operations-ii/
"""
from typing import List


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        a10, a11, a20, a21 = [],[],[],[]
        for i in range(len(s1)):
            if i & 1:
                a11.append(s1[i])
                a21.append(s2[i])
            else:
                a10.append(s1[i])
                a20.append(s2[i])
        return sorted(a10) == sorted(a20) and sorted(a11) == sorted(a21)

if __name__ == '__main__':
    # true
    print(Solution().checkStrings("abcdba", s2 = "cabdab"))
    # false
    print(Solution().checkStrings("abe", s2 = "bea"))