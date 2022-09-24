"""
 * 你有一个炸弹需要拆除，时间紧迫！你的情报员会给你一个长度为 n 的 循环 数组 code 以及一个密钥 k 。
 * 为了获得正确的密码，你需要替换掉每一个数字。所有数字会 同时 被替换。
 * 1、如果 k > 0 ，将第 i 个数字用 接下来 k 个数字之和替换。
 * 2、如果 k < 0 ，将第 i 个数字用 之前 k 个数字之和替换。
 * 3、如果 k == 0 ，将第 i 个数字用 0 替换。
 * 由于 code 是循环的， code[n-1] 下一个元素是 code[0] ，且 code[0] 前一个元素是 code[n-1] 。
 * 给你 循环 数组 code 和整数密钥 k ，请你返回解密后的结果来拆除炸弹！
 * 提示：
 * 1、n == code.length
 * 2、1 <= n <= 100
 * 3、1 <= code[i] <= 100
 * 4、-(n - 1) <= k <= n - 1
 * 链接：https://leetcode.cn/problems/defuse-the-bomb/
"""

from typing import *


class Solution:

    def decrypt(self, code: List[int], k: int) -> List[int]:
        sm, n = 0, len(code)
        ans = [0] * len(code)
        if k != 0:
            sign = 1 if k > 0 else -1
            for i in range(k * sign):
                sm += code[(n + sign * (1 + i)) % n]
            ans[0] = sm
            for i in range(1, n):
                if sign == 1:
                    ans[i] = ans[i - 1] + code[(i + k) % n] - code[i]
                else:
                    ans[i] = ans[i - 1] + code[i - 1] - code[(i + k - 1 + n) % n]
        return ans


if __name__ == "__main__":
    # [22,26,22,28,29,22,19,22,18,21,28,19]
    print(Solution().decrypt([10, 5, 7, 7, 3, 2, 10, 3, 6, 9, 1, 6], -4))
    # [12,5,6,13]
    print(Solution().decrypt([2, 4, 9, 3], -2))
    # [12,10,16,13]
    print(Solution().decrypt([5, 7, 1, 4], 3))
    # [0,0,0,0]
    print(Solution().decrypt([1, 2, 3, 4], 0))
