"""
 * 给你一个字符串 s 以及两个整数 a 和 b 。其中，字符串 s 的长度为偶数，且仅由数字 0 到 9 组成。
 * 你可以在 s 上按任意顺序多次执行下面两个操作之一：
 * 1、累加：将  a 加到 s 中所有下标为奇数的元素上（下标从 0 开始）。数字一旦超过 9 就会变成 0，如此循环往复。例如，s = "3456" 且 a = 5，则执行此操作后 s 变成 "3951"。
 * 2、轮转：将 s 向右轮转 b 位。例如，s = "3456" 且 b = 1，则执行此操作后 s 变成 "6345"。
 * 请你返回在 s 上执行上述操作任意次后可以得到的 字典序最小 的字符串。
 * 如果两个字符串长度相同，那么字符串 a 字典序比字符串 b 小可以这样定义：在 a 和 b 出现不同的第一个位置上，字符串 a 中的字符出现在字母表中的时间早于 b 中的对应字符。
 * 例如，"0158” 字典序比 "0190" 小，因为不同的第一个位置是在第三个字符，显然 '5' 出现在 '9' 之前。
 * 提示：
 * 1、2 <= s.length <= 100
 * 2、s.length 是偶数
 * 3、s 仅由数字 0 到 9 组成
 * 4、1 <= a <= 9
 * 5、1 <= b <= s.length - 1
 * 链接：https://leetcode.cn/problems/lexicographically-smallest-string-after-applying-operations/
"""

class Solution:

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        ans = s
        n = len(s)
        ss = list(s)
        for _ in range(n):
            ss = ss[-b:] + ss[:-b]
            for j in range(10):
                for k in range(1, n, 2):
                    ss[k] = str((int(ss[k]) + a) % 10)
                if b & 1:
                    for p in range(10):
                        for k in range(0, n, 2):
                            ss[k] = str((int(ss[k]) + a) % 10)
                        t = ''.join(ss)
                        if ans > t:
                            ans = t
                else:
                    t = ''.join(ss)
                    if ans > t:
                        ans = t
        return ans


if __name__ == '__main__':
    # "2050"
    print(Solution().findLexSmallestString("5525", a=9, b=2))
    # "24"
    print(Solution().findLexSmallestString("74", a=5, b=1))
    # "0011"
    print(Solution().findLexSmallestString("0011", a=4, b=2))
    # "00553311"
    print(Solution().findLexSmallestString("43987654", a=7, b=3))
