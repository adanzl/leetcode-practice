"""
 * 给你两个整数 num 和 t 。
 * 如果整数 x 可以在执行下述操作不超过 t 次的情况下变为与 num 相等，则称其为 可达成数字 ：
 * 每次操作将 x 的值增加或减少 1 ，同时可以选择将 num 的值增加或减少 1 。
 * 返回所有可达成数字中的最大值。可以证明至少存在一个可达成数字。
 * 提示：1 <= num, t <= 50
 * 链接：https://leetcode.cn/problems/find-the-maximum-achievable-number/
"""


class Solution:

    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t * 2


if __name__ == '__main__':
    # 6
    print(Solution().theMaximumAchievableX(4, t=1))
    # 7
    print(Solution().theMaximumAchievableX(3, t=2))
