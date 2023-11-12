"""
 * 给你两个正整数 n 和 limit 。
 * 请你将 n 颗糖果分给 3 位小朋友，确保没有任何小朋友得到超过 limit 颗糖果，请你返回满足此条件下的 总方案数 。
 * 提示：
 * 1、1 <= n <= 10^6
 * 2、1 <= limit <= 10^
 * 链接：https://leetcode.cn/problems/distribute-candies-among-children-i/
"""


class Solution:

    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for p0 in range(max(0, n - limit * 2), min(limit, n) + 1):
            ans += min(limit, n - p0) - max(0, n - p0 - limit) + 1
        return ans


if __name__ == '__main__':
    # 10
    print(Solution().distributeCandies(3, limit=3))
    # 3
    print(Solution().distributeCandies(5, limit=2))
