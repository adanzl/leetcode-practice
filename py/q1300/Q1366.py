"""
 * 现在有一个特殊的排名系统，依据参赛团队在投票人心中的次序进行排名，
 * 每个投票者都需要按从高到低的顺序对参与排名的所有团队进行排位。
 * 排名规则如下：
 * 1、参赛团队的排名次序依照其所获「排位第一」的票的多少决定。
 *    如果存在多个团队并列的情况，将继续考虑其「排位第二」的票的数量。以此类推，直到不再存在并列的情况。
 * 2、如果在考虑完所有投票情况后仍然出现并列现象，则根据团队字母的字母顺序进行排名。
 * 给你一个字符串数组 votes 代表全体投票者给出的排位情况，请你根据上述排名规则对所有参赛团队进行排名。
 * 请你返回能表示按排名系统 排序后 的所有团队排名的字符串。
 * 提示：
 * 1、1 <= votes.length <= 1000
 * 2、1 <= votes[i].length <= 26
 * 3、votes[i].length == votes[j].length for 0 <= i, j < votes.length
 * 4、votes[i][j] 是英文 大写 字母
 * 5、votes[i] 中的所有字母都是唯一的
 * 6、votes[0] 中出现的所有字母 同样也 出现在 votes[j] 中，其中 1 <= j < votes.length
 * 链接：https://leetcode.cn/problems/rank-teams-by-votes
"""

from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=1366 lang=python3
# @lcpr version=20004
#
# [1366] 通过投票对团队排名
#


# @lc code=start
class Solution:

    def rankTeams(self, votes: List[str]) -> str:
        d = {}
        for vote in votes:
            for i, c in enumerate(vote):
                if c not in d:
                    d[c] = [0] * 26
                d[c][i] += 1
        ans = sorted(d.keys(), key=lambda x: (d[x], -ord(x)), reverse=True)
        return "".join(ans)


# @lc code=end
#

if __name__ == '__main__':
    # "ABC"
    print(Solution().rankTeams(["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]))
    # "ACB"
    print(Solution().rankTeams(["ABC", "ACB", "ABC", "ACB", "ACB"]))
    # "XWYZ"
    print(Solution().rankTeams(["WXYZ", "XYZW"]))
    # "ZMNAGUEDSJYLBOPHRQICWFXTVK"
    print(Solution().rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))
