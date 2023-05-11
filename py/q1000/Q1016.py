"""
 * 给定一个二进制字符串 s 和一个正整数 n，如果对于 [1, n] 范围内的每个整数，其二进制表示都是 s 的 子字符串 ，就返回 true，否则返回 false 。
 * 子字符串 是字符串中连续的字符序列。
 * 提示：
 * 1、1 <= s.length <= 1000
 * 2、s[i] 不是 '0' 就是 '1'
 * 3、1 <= n <= 10^9
 * 链接：https://leetcode.cn/problems/binary-string-with-substrings-representing-1-to-n/
"""


class Solution:

    def queryString(self, s: str, n: int) -> bool:
        ss = set()
        for i in range(1, len(s) + 1):
            for j in range(len(s) - i + 1):
                ss.add(int(s[j:j + i], 2))
        a = sorted(list(ss))
        return len(a) >= n and (a[n] == n if n > 1 else a[n - 1] == n)


if __name__ == '__main__':
    # True
    print(Solution().queryString("1", n=1))
    # True
    print(Solution().queryString("0110", n=3))
    # False
    print(Solution().queryString("0110", n=4))