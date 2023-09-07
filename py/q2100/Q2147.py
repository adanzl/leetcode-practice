"""
 * 在一个图书馆的长廊里，有一些座位和装饰植物排成一列。给你一个下标从 0 开始，长度为 n 的字符串 corridor ，
 * 它包含字母 'S' 和 'P' ，其中每个 'S' 表示一个座位，每个 'P' 表示一株植物。
 * 在下标 0 的左边和下标 n - 1 的右边 已经 分别各放了一个屏风。
 * 你还需要额外放置一些屏风。每一个位置 i - 1 和 i 之间（1 <= i <= n - 1），至多能放一个屏风。
 * 请你将走廊用屏风划分为若干段，且每一段内都 恰好有两个座位 ，而每一段内植物的数目没有要求。
 * 可能有多种划分方案，如果两个方案中有任何一个屏风的位置不同，那么它们被视为 不同 方案。
 * 请你返回划分走廊的方案数。由于答案可能很大，请你返回它对 10^9 + 7 取余 的结果。如果没有任何方案，请返回 0 。
 * 提示：
 * 1、n == corridor.length
 * 2、1 <= n <= 10^5
 * 3、corridor[i] 要么是 'S' ，要么是 'P' 。
 * 链接：https://leetcode.cn/problems/number-of-ways-to-divide-a-long-corridor/
"""

#
# @lc app=leetcode.cn id=2147 lang=python3
#
# [2147] 分隔长廊的方案数
#


# @lc code=start
class Solution:

    def numberOfWays(self, corridor: str) -> int:
        ans = 0
        cnt_s, cnt_p = 0, 1
        for c in corridor:
            if c == 'P':
                if cnt_s == 2:
                    cnt_p += 1
            else:
                if cnt_s == 2:
                    ans = max(1, ans)
                    ans *= cnt_p
                    cnt_s = 0
                    cnt_p = 1
                cnt_s += 1
        if cnt_s == 2:
            ans = max(1, ans)
            cnt_s = 0
        if cnt_s: return 0
        return ans % (10**9 + 7)


# @lc code=end

if __name__ == '__main__':
    # 1
    print(Solution().numberOfWays('PPSPSP'))
    # 3
    print(Solution().numberOfWays('SSPPSPS'))
    # 0
    print(Solution().numberOfWays('S'))