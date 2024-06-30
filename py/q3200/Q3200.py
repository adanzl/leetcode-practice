"""
 * 给你两个整数 red 和 blue，分别表示红色球和蓝色球的数量。
 * 你需要使用这些球来组成一个三角形，满足第 1 行有 1 个球，第 2 行有 2 个球，第 3 行有 3 个球，依此类推。
 * 每一行的球必须是 相同 颜色，且相邻行的颜色必须 不同。
 * 返回可以实现的三角形的 最大 高度。
 * 提示：1 <= red, blue <= 100
 * 链接：https://leetcode.cn/problems/maximum-height-of-a-triangle/
"""
from itertools import count


class Solution:

    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        ans = 0
        v1, v2, f = 0, 0, 0
        for i in count():
            if f:
                v1 += ans + 1
            else:
                v2 += ans + 1
            if (v1 > red or v2 > blue) and (v2 > red or v1 > blue):
                break
            ans += 1
            f ^= 1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().maxHeightOfTriangle(2, blue=4))
    # 2
    print(Solution().maxHeightOfTriangle(2, blue=1))
    # 1
    print(Solution().maxHeightOfTriangle(1, blue=1))
    # 2
    print(Solution().maxHeightOfTriangle(10, blue=1))
