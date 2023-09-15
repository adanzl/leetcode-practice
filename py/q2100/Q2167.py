"""
 * 给你一个下标从 0 开始的二进制字符串 s ，表示一个列车车厢序列。s[i] = '0' 表示第 i 节车厢 不 含违禁货物，而 s[i] = '1' 表示第 i 节车厢含违禁货物。
 * 作为列车长，你需要清理掉所有载有违禁货物的车厢。你可以不限次数执行下述三种操作中的任意一个：
 * 1、从列车 左 端移除一节车厢（即移除 s[0]），用去 1 单位时间。
 * 2、从列车 右 端移除一节车厢（即移除 s[s.length - 1]），用去 1 单位时间。
 * 3、从列车车厢序列的 任意位置 移除一节车厢，用去 2 单位时间。
 * 返回移除所有载有违禁货物车厢所需要的 最少 单位时间数。
 * 注意，空的列车车厢序列视为没有车厢含违禁货物。
 * 提示：
 * 1、1 <= s.length <= 2 * 10^5
 * 2、s[i] 为 '0' 或 '1'
 * 链接：https://leetcode.cn/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/
"""

#
# @lc app=leetcode.cn id=2167 lang=python3
#
# [2167] 移除所有载有违禁货物车厢所需的最少时间
#


# @lc code=start
class Solution:

    def minimumTime(self, s: str) -> int:
        n = len(s)
        lf = [[0 for _ in range(2)] for __ in range(n)]
        lf[0] = [1, 1] if s[0] == '1' else [0, 0]
        for i in range(1, n):
            if s[i] == '1':
                lf[i][0] = i + 1
                lf[i][1] = min(lf[i - 1][0], lf[i - 1][1]) + 2
            else:
                lf[i] = lf[i - 1]
        rf = [1, 1] if s[-1] == '1' else [0, 0]
        ans = min(n, lf[-1][1] + rf[1], lf[-1][0] + rf[0], lf[-1][1] + rf[0], lf[-1][0] + rf[1])
        for i in range(n - 2, -1, -1):
            if s[i] == '1':
                rf = [n - i, min(rf[0], rf[1]) + 2]
            ans = min(ans, lf[i][1] + rf[1], lf[i][0] + rf[0], lf[i][1] + rf[0], lf[i][0] + rf[1])
        return ans


# @lc code=end

if __name__ == '__main__':
    # 0
    print(Solution().minimumTime("0"))
    # 5
    print(Solution().minimumTime("1100101"))
    # 2
    print(Solution().minimumTime("0010"))
