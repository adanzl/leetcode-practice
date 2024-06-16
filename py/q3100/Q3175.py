"""
 * 有 n 位玩家在进行比赛，玩家编号依次为 0 到 n - 1 。
 * 给你一个长度为 n 的整数数组 skills 和一个 正 整数 k ，其中 skills[i] 是第 i 位玩家的技能等级。skills 中所有整数 互不相同 。
 * 所有玩家从编号 0 到 n - 1 排成一列。
 * 比赛进行方式如下：
 * 1、队列中最前面两名玩家进行一场比赛，技能等级 更高 的玩家胜出。
 * 2、比赛后，获胜者保持在队列的开头，而失败者排到队列的末尾。
 * 这个比赛的赢家是 第一位连续 赢下 k 场比赛的玩家。
 * 请你返回这个比赛的赢家编号。
 * 提示：
 * 1、n == skills.length
 * 2、2 <= n <= 10^5
 * 3、1 <= k <= 10^9
 * 4、1 <= skills[i] <= 10^6
 * 5、skills 中的整数互不相同。
 * 链接：https://leetcode.cn/problems/find-the-first-player-to-win-k-games-in-a-row/
"""
from typing import List


class Solution:

    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        ans, cnt = 0, 0
        for i in range(1, len(skills)):
            if skills[i] < skills[ans]:
                cnt += 1
            else:
                cnt = 1
                ans = i
            if cnt >= k:
                break
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().findWinningPlayer([4, 2, 6, 3, 9], k=2))
    # 1
    print(Solution().findWinningPlayer([2, 5, 4], k=3))
    # 1
    print(Solution().findWinningPlayer([2, 5, 4], k=73))
    # 1
    print(Solution().findWinningPlayer([1, 6, 17], 1))
