"""
 * 给你三个 正整数 n 、x 和 y 。
 * 在城市中，存在编号从 1 到 n 的房屋，由 n 条街道相连。
 * 对所有 1 <= i < n ，都存在一条街道连接编号为 i 的房屋与编号为 i + 1 的房屋。
 * 另存在一条街道连接编号为 x 的房屋与编号为 y 的房屋。
 * 对于每个 k（1 <= k <= n），你需要找出所有满足要求的 房屋对 [house1, house2] ，
 * 即从 house1 到 house2 需要经过的 最少 街道数为 k 。
 * 返回一个下标从 1 开始且长度为 n 的数组 result ，其中 result[k] 表示所有满足要求的房屋对的数量，  
 * 即从一个房屋到另一个房屋需要经过的 最少 街道数为 k 。
 * 注意，x 与 y 可以 相等 。
 * 提示：
 * 1、2 <= n <= 100
 * 2、1 <= x, y <= n
 * 链接：https://leetcode.cn/problems/count-the-number-of-houses-at-a-certain-distance-i
"""

from typing import List

#
# @lc app=leetcode.cn id=3015 lang=python3
#
# [3015] 按距离统计房屋对数目 I
#


# @lc code=start
class Solution:

    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y:
            x, y =  y, x
        ans = [(n - i - 1) * 2 for i in range(n)]
        # n^2
        for v0 in range(n):
            for v1 in range(v0 + 1, n):
                d = abs(v0 - x + 1) + abs(v1 - y + 1) + 1
                if v1 - v0 > d:
                    ans[v1 - v0 - 1] -= 2
                    ans[d - 1] += 2
        return ans


# @lc code=end

if __name__ == '__main__':
    # [6,0,0]
    print(Solution().countOfPairs(3, x=3, y=1))
    # [6,0,0]
    print(Solution().countOfPairs(3, x=1, y=3))
    # [10,8,2,0,0]
    print(Solution().countOfPairs(5, x=2, y=4))
    # [6,4,2,0]
    print(Solution().countOfPairs(4, x=1, y=1))
    # [6,0,0]
    print(Solution().countOfPairs(3, 1, 3))
