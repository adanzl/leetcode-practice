"""
 * 有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。
 * 假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。
 * 给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。
 * 你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。
 * 请返回待替换子串的最小可能长度。
 * 如果原字符串自身就是一个平衡字符串，则返回 0。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s.length 是 4 的倍数
 * 3、s 中只含有 'Q', 'W', 'E', 'R' 四种字符
 * 链接：https://leetcode.cn/problems/replace-the-substring-for-balanced-string/
"""


class Solution:

    def balancedString(self, s: str) -> int:
        n = len(s)
        sm_q, sm_w, sm_e, sm_r = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
        for i in range(n):
            sm_q[i + 1] = sm_q[i] + (1 if s[i] == 'Q' else 0)
            sm_w[i + 1] = sm_w[i] + (1 if s[i] == 'W' else 0)
            sm_e[i + 1] = sm_e[i] + (1 if s[i] == 'E' else 0)
            sm_r[i + 1] = sm_r[i] + (1 if s[i] == 'R' else 0)
        size = n // 4
        l, r = 0, n - 1
        ans = n - 1
        while l <= r:
            mid = (l + r) // 2
            find = False
            for i in range(-1, n - mid):
                if sm_q[i + 1] + sm_q[-1] - sm_q[i + mid + 1] <= size \
                    and sm_w[i + 1] + sm_w[-1] - sm_w[i + mid + 1] <= size \
                        and sm_e[i + 1] + sm_e[-1] - sm_e[i + mid + 1] <= size \
                            and sm_r[i + 1] + sm_r[-1] - sm_r[i + mid + 1] <= size:
                    find = True
                    ans = mid
                    break
            if find:
                r = mid - 1
            else:
                l = mid + 1
        return ans


if __name__ == '__main__':
    # 5
    print(Solution().balancedString("WWWEQRQEWWQQQWQQQWEWEEWRRRRRWWQE"))
    # 1
    print(Solution().balancedString("QQWE"))
    # 0
    print(Solution().balancedString("QWER"))
    # 2
    print(Solution().balancedString("QQQW"))
    # 3
    print(Solution().balancedString("QQQQ"))