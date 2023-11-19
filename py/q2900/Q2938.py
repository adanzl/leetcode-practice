"""
 * 桌子上有 n 个球，每个球的颜色不是黑色，就是白色。
 * 给你一个长度为 n 、下标从 0 开始的二进制字符串 s，其中 1 和 0 分别代表黑色和白色的球。
 * 在每一步中，你可以选择两个相邻的球并交换它们。
 * 返回「将所有黑色球都移到右侧，所有白色球都移到左侧所需的 最小步数」。
 * 提示：
 * 1、1 <= n == s.length <= 10^5
 * 2、s[i] 不是 '0'，就是 '1'。
 * 链接：https://leetcode.cn/problems/separate-black-and-white-balls/description/
"""


class Solution:

    def minimumSteps(self, s: str) -> int:
        ans, cnt = 0, 0
        for c in s:
            if c == '1':
                cnt += 1
            else:
                ans += cnt
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().minimumSteps("101"))
    # 2
    print(Solution().minimumSteps("100"))
    # 0
    print(Solution().minimumSteps("0111"))
