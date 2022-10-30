"""
 * 神奇字符串 s 仅由 '1' 和 '2' 组成，并需要遵守下面的规则：
 * 神奇字符串 s 的神奇之处在于，串联字符串中 '1' 和 '2' 的连续出现次数可以生成该字符串。
 * s 的前几个元素是 s = "1221121221221121122……" 。如果将 s 中连续的若干 1 和 2 进行分组，可以得到 "1 22 11 2 1 22 1 22 11 2 11 22 ......" 。
 * 每组中 1 或者 2 的出现次数分别是 "1 2 2 1 1 2 1 2 2 1 2 2 ......" 。上面的出现次数正是 s 自身。
 * 给你一个整数 n ，返回在神奇字符串 s 的前 n 个数字中 1 的数目。
 * 提示：1 <= n <= 10^5
 * 链接：https://leetcode.cn/problems/magical-string/submissions/
"""
from typing import Counter, List


class Solution:

    def magicalString(self, n: int) -> int:
        arr = [1, 2, 2] + [0] * (n)
        l, r = 1, 1
        pre = 1
        while r < n:
            nv = 1 if pre == 2 else 2
            for _ in range(arr[l]):
                arr[r] = nv
                r += 1
            pre = nv
            l += 1
        c = Counter(arr[:n])
        return c[1]


if __name__ == '__main__':
    # 3  122112
    print(Solution().magicalString(6))
    # 1
    print(Solution().magicalString(1))
    # 49972
    print(Solution().magicalString(10**5))