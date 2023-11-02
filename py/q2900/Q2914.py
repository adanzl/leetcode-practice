"""
 * 给你一个长度为偶数下标从 0 开始的二进制字符串 s 。
 * 如果可以将一个字符串分割成一个或者更多满足以下条件的子字符串，那么我们称这个字符串是 美丽的 ：
 * 1、每个子字符串的长度都是 偶数 。
 * 2、每个子字符串都 只 包含 1 或 只 包含 0 。
 * 你可以将 s 中任一字符改成 0 或者 1 。
 * 请你返回让字符串 s 美丽的 最少 字符修改次数。
 * 提示：
 * 1、2 <= s.length <= 10^5
 * 2、s 的长度为偶数。
 * 3、s[i] 要么是 '0' ，要么是 '1' 。
 * 链接：https://leetcode.cn/problems/minimum-number-of-changes-to-make-binary-string-beautiful/
"""


class Solution:

    def minChanges(self, s: str) -> int:
        n = len(s)
        dp = [[0, 0]]
        for i in range(0, n, 2):
            ss = s[i:i + 2]
            if ss == '00' or ss == '11':
                dp.append([min(dp[-1][0], dp[-1][1]), min(dp[-1][0] + 2, dp[-1][1] + 2)])
            elif ss == '01':
                dp.append([min(dp[-1][0], dp[-1][1]) + 1, min(dp[-1][0], dp[-1][1]) + 1])
            elif ss == '10':
                dp.append([min(dp[-1][0], dp[-1][1]) + 1, min(dp[-1][0], dp[-1][1]) + 1])
        return min(dp[-1])


if __name__ == '__main__':
    # 2
    print(Solution().minChanges("1001"))
    # 1
    print(Solution().minChanges("10"))
    # 0
    print(Solution().minChanges("0000"))
