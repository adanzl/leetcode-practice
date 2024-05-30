"""
 * 给你一个以二进制形式表示的数字 s 。请你返回按下述规则将其减少到 1 所需要的步骤数：
 * 1、如果当前数字为偶数，则将其除以 2 。
 * 2、如果当前数字为奇数，则将其加上 1 。
 * 题目保证你总是可以按上述规则将测试用例变为 1 。
 * 提示：
 * 1、1 <= s.length <= 500
 * 2、s 由字符 '0' 或 '1' 组成。
 * 3、s[0] == '1'
 * 链接：https://leetcode.cn/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one
"""

from typing import List

#
# @lc app=leetcode.cn id=1404 lang=python3
#
# [1404] 将二进制表示减到 1 的步骤数
#


# @lc code=start
class Solution:

    def numSteps(self, s: str) -> int:
        ans, n = 0, len(s)
        v = 0
        for i in range(n - 1, 0, -1):
            v += int(s[i])
            if v & 1 == 0:
                v >>= 1
            else:
                ans += 1
                v = (v + 1) >> 1
            ans += 1
        return ans + v


# @lc code=end

if __name__ == '__main__':
    # 6
    print(Solution().numSteps("1101"))
    # 0
    print(Solution().numSteps("1"))
    # 1
    print(Solution().numSteps("10"))
