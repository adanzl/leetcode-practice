"""
 * 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
 * 注意：给定数字的范围是 [0, 108]
 * 链接：https://leetcode-cn.com/problems/maximum-swap/
"""


class Solution:

    def maximumSwap(self, num: int) -> int:
        n_idx = [-1] * 10
        n_str = list(str(num))
        n = len(n_str)
        ans = [n - 1, n - 1]  # i1 - i2
        for i, c in enumerate(n_str):
            nu = int(c)
            for j in range(nu):
                if n_idx[j] != -1:
                    if ans[0] > n_idx[j]:
                        ans = [n_idx[j], i]
                    elif ans[0] == n_idx[j]:
                        if n_str[i] >= n_str[ans[1]]:
                            ans[1] = i
            if n_idx[nu] == -1: n_idx[nu] = i
        n_str[ans[0]], n_str[ans[1]] = n_str[ans[1]], n_str[ans[0]]
        return int("".join(n_str))


if __name__ == "__main__":
    # 9913
    print(Solution().maximumSwap(1993))
    # 98863
    print(Solution().maximumSwap(98368))
    # 7236
    print(Solution().maximumSwap(2736))
    # 9973
    print(Solution().maximumSwap(9973))