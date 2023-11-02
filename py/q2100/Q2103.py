"""
 * 总计有 n 个环，环的颜色可以是红、绿、蓝中的一种。这些环分别穿在 10 根编号为 0 到 9 的杆上。
 * 给你一个长度为 2n 的字符串 rings ，表示这 n 个环在杆上的分布。rings 中每两个字符形成一个 颜色位置对 ，用于描述每个环：
 * 1、第 i 对中的 第一个 字符表示第 i 个环的 颜色（'R'、'G'、'B'）。
 * 2、第 i 对中的 第二个 字符表示第 i 个环的 位置，也就是位于哪根杆上（'0' 到 '9'）。
 * 例如，"R3G2B1" 表示：共有 n == 3 个环，红色的环在编号为 3 的杆上，绿色的环在编号为 2 的杆上，蓝色的环在编号为 1 的杆上。
 * 找出所有集齐 全部三种颜色 环的杆，并返回这种杆的数量。
 * 提示：
 * 1、rings.length == 2 * n
 * 2、1 <= n <= 100
 * 3、如 i 是 偶数 ，则 rings[i] 的值可以取 'R'、'G' 或 'B'（下标从 0 开始计数）
 * 4、如 i 是 奇数 ，则 rings[i] 的值可以取 '0' 到 '9' 中的一个数字（下标从 0 开始计数）
 * 链接：https://leetcode.cn/problems/rings-and-rods
"""

#
# @lc app=leetcode.cn id=2103 lang=python3
#
# [2103] 环和杆
#


# @lc code=start
class Solution:

    def countPoints(self, rings: str) -> int:
        flags = [0] * 10
        d = {"B": 0, "G": 1, "R": 2}
        for i in range(0, len(rings), 2):
            flags[int(rings[i + 1])] |= (1 << d[rings[i]])
        return sum([1 for v in flags if v == 7])


# @lc code=end

if __name__ == '__main__':
    # 1
    print(Solution().countPoints('B0R0G0R9R0B0G0'))
    # 0
    print(Solution().countPoints('G4'))
