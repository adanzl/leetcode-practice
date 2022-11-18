"""
 * 给你一个整数数组 digits，你可以通过按任意顺序连接其中某些数字来形成 3 的倍数，请你返回所能得到的最大的 3 的倍数。
 * 由于答案可能不在整数数据类型范围内，请以字符串形式返回答案。
 * 如果无法得到答案，请返回一个空字符串。
 * 提示：
 * 1、1 <= digits.length <= 10^4
 * 2、0 <= digits[i] <= 9
 * 3、返回的结果不应包含不必要的前导零。
 * 链接：https://leetcode.cn/problems/largest-multiple-of-three/
"""
from typing import List


class Solution:

    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse=True)
        dp = ["", None, None]  # remain 0,1,2
        cmp = lambda a, b: max(a, b) if len(a) == len(b) else (a if len(a) > len(b) else b)
        for num in digits:
            ndp = dp.copy()
            for i in range(3):
                if dp[i] is None: continue
                idx = (num + i) % 3
                ndp[idx] = (dp[i] + str(num)) if ndp[idx] is None else cmp(ndp[idx], dp[i] + str(num))
            dp = ndp
        if dp[0] is None: return ""
        if len(dp[0]) == 1: return dp[0]
        idx = 0
        while idx < len(dp[0]) and dp[0][idx] == '0':
            idx += 1
        return dp[0][min(idx, len(dp[0]) - 1):]


if __name__ == '__main__':
    # "111"
    print(Solution().largestMultipleOfThree([1, 1, 1, 2]))
    # ""
    print(Solution().largestMultipleOfThree([1]))
    # 8760
    print(Solution().largestMultipleOfThree([8, 6, 7, 1, 0]))
    # 981
    print(Solution().largestMultipleOfThree([8, 1, 9]))
    # "0"
    print(Solution().largestMultipleOfThree([0, 0, 0, 0, 0, 0]))
