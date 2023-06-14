"""
 * 给你一个长度为 n 、下标从 1 开始的二进制字符串，所有位最开始都是 0 。我们会按步翻转该二进制字符串的所有位（即，将 0 变为 1）。
 * 给你一个下标从 1 开始的整数数组 flips ，其中 flips[i] 表示对应下标 i 的位将会在第 i 步翻转。
 * 二进制字符串 前缀一致 需满足：在第 i 步之后，在 闭 区间 [1, i] 内的所有位都是 1 ，而其他位都是 0 。
 * 返回二进制字符串在翻转过程中 前缀一致 的次数。
 * 提示：
 * 1、n == flips.length
 * 2、1 <= n <= 5 * 10^4
 * 3、flips 是范围 [1, n] 中所有整数构成的一个排列
 * 链接：https://leetcode.cn/problems/number-of-times-binary-string-is-prefix-aligned/
"""
from typing import List


class Solution:

    def numTimesAllBlue(self, flips: List[int]) -> int:
        res = 0
        # 巧妙解法
        cur_max_flip = 0
        for step, flip in enumerate(flips):
            cur_max_flip = max(cur_max_flip, flip)
            if cur_max_flip == step + 1:
                res += 1
        return res


if __name__ == '__main__':
    # 2
    print(Solution().numTimesAllBlue([3, 2, 4, 1, 5]))
    # 1
    print(Solution().numTimesAllBlue([4, 1, 2, 3]))