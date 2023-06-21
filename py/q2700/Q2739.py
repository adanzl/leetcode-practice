"""
 * 卡车有两个油箱。给你两个整数，mainTank 表示主油箱中的燃料（以升为单位），additionalTank 表示副油箱中的燃料（以升为单位）。
 * 该卡车每耗费 1 升燃料都可以行驶 10 km。每当主油箱使用了 5 升燃料时，如果副油箱至少有 1 升燃料，则会将 1 升燃料从副油箱转移到主油箱。
 * 返回卡车可以行驶的最大距离。
 * 注意：从副油箱向主油箱注入燃料不是连续行为。这一事件会在每消耗 5 升燃料时突然且立即发生。
 * 提示：1 <= mainTank, additionalTank <= 100
 * 链接：https://leetcode.cn/problems/total-distance-traveled/
"""


class Solution:

    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank >= 5:
            a = mainTank // 5
            ans += a * 5 * 10
            mainTank = mainTank - a * 5 + min(a, additionalTank)
            additionalTank -= min(a, additionalTank)
        return ans + mainTank * 10


if __name__ == '__main__':
    # 70
    print(Solution().distanceTraveled(6, 1))
    # 60
    print(Solution().distanceTraveled(5, additionalTank=10))
    # 10
    print(Solution().distanceTraveled(1, additionalTank=2))
