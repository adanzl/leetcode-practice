"""
 * 给你两个字符串 a 和 b ，它们长度相同。请你选择一个下标，将两个字符串都在 相同的下标 分割开。
 * 由 a 可以得到两个字符串： a_prefix 和 a_suffix ，满足 a = a_prefix + a_suffix ，同理，由 b 可以得到两个字符串 b_prefix 和 b_suffix ，满足 b = b_prefix + b_suffix 。
 * 请你判断 a_prefix + b_suffix 或者 b_prefix + a_suffix 能否构成回文串。
 * 当你将一个字符串 s 分割成 s_prefix 和 s_suffix 时， s_suffix 或者 s_prefix 可以为空。
 * 比方说， s = "abc" 那么 "" + "abc" ， "a" + "bc" ， "ab" + "c" 和 "abc" + "" 都是合法分割。
 * 如果 能构成回文字符串 ，那么请返回 true，否则返回 false 。
 * 注意， x + y 表示连接字符串 x 和 y 。
 * 提示：
 * 1、1 <= a.length, b.length <= 10^5
 * 2、a.length == b.length
 * 3、a 和 b 都只包含小写英文字母
 * 链接：https://leetcode.cn/problems/split-two-strings-to-make-palindrome/
"""


class Solution:

    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)

        def f(arr):
            mark_p = [False] * (n)
            if n & 1: mark_p[n // 2] = True
            for i in range(n // 2 - 1, -1, -1):
                if arr[i] == arr[n - 1 - i]:
                    mark_p[i] = True
                else:
                    break
            return mark_p

        mark_a = f(a)
        mark_b = f(b)
        if mark_a[0] or mark_b[0]:
            return True
        ans = True
        for i in range(n // 2):
            if a[i] == b[n - 1 - i]:
                if mark_a[i + 1] or mark_b[i + 1]:
                    return True
            else:
                ans = False
                break
        if ans: return True
        ans = True
        for i in range(n // 2):
            if b[i] == a[n - 1 - i]:
                if mark_a[i + 1] or mark_b[i + 1]:
                    return True
            else:
                ans = False
                break
        return ans


if __name__ == '__main__':
    # True
    print(Solution().checkPalindromeFormation("pvhmupgqeltozftlmfjjde", "yjgpzbezspnnpszebzmhvp"))
    # False
    print(Solution().checkPalindromeFormation("pvhmupgqeltozftlmfjjde", "yjgpzbezspnnpszebzmcvp"))
    # True
    print(Solution().checkPalindromeFormation("ulacfd", b="jizalu"))
    # True
    print(Solution().checkPalindromeFormation("abdef", b="fecab"))
    # True
    print(Solution().checkPalindromeFormation("x", b="y"))
