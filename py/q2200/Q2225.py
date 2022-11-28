"""
 * 给你一个整数数组 matches 其中 matches[i] = [winner_i, loser_i] 表示在一场比赛中 winner_i 击败了 loser_i 。
 * 返回一个长度为 2 的列表 answer ：
 * 1、answer[0] 是所有 没有 输掉任何比赛的玩家列表。
 * 2、answer[1] 是所有恰好输掉 一场 比赛的玩家列表。
 * 两个列表中的值都应该按 递增 顺序返回。
 * 注意：
 * 1、只考虑那些参与 至少一场 比赛的玩家。
 * 2、生成的测试用例保证 不存在 两场比赛结果 相同 。
 * 提示：
 * 1、1 <= matches.length <= 10^5
 * 2、matches[i].length == 2
 * 3、1 <= winner_i, loser_i <= 10^5
 * 4、winner_i != loser_i
 * 5、所有 matches[i] 互不相同
 * 链接：https://leetcode-cn.com/problems/find-players-with-zero-or-one-losses
"""
from typing import Counter, List


class Solution:

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        cnt = Counter()
        for w, l in matches:
            cnt[w] += 0
            cnt[l] += 1
        ans = [[], []]
        for u, c in cnt.items():
            if c == 0: ans[0].append(u)
            if c == 1: ans[1].append(u)
        ans[0].sort()
        ans[1].sort()
        return ans


if __name__ == '__main__':
    # [[1,2,10],[4,5,7,8]]
    print(Solution().findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
    # [[1,2,5,6],[]]
    print(Solution().findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]))
    # [[1,2,10],[4,5,7,8]]
    print(Solution().findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
