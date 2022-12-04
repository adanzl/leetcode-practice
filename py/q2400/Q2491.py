"""
 * 给你一个正整数数组 skill ，数组长度为 偶数 n ，其中 skill[i] 表示第 i 个玩家的技能点。将所有玩家分成 n / 2 个 2 人团队，使每一个团队的技能点之和 相等 。
 * 团队的 化学反应 等于团队中玩家的技能点 乘积 。
 * 返回所有团队的 化学反应 之和，如果无法使每个团队的技能点之和相等，则返回 -1 。
 * 提示：
 * 1、2 <= skill.length <= 10^5
 * 2、skill.length 是偶数
 * 3、1 <= skill[i] <= 1000
 * 链接：https://leetcode.cn/problems/divide-players-into-teams-of-equal-skill/
"""
from collections import Counter
from typing import List


class Solution:

    def dividePlayers(self, skill: List[int]) -> int:
        sm = sum(skill)
        n = len(skill)
        val, r = divmod(sm, n // 2)
        if r != 0: return -1
        cnt = Counter(skill)
        ans = 0
        while cnt:
            num = list(cnt.keys())[0]
            if cnt[num] == 0:
                return -1
            cnt[num] -= 1
            if cnt[num] == 0: del cnt[num]
            if cnt[val - num] == 0:
                return -1
            cnt[val - num] -= 1
            if cnt[val - num] == 0: del cnt[val - num]
            ans += num * (val - num)

        return ans


if __name__ == '__main__':
    # 22
    print(Solution().dividePlayers([3, 2, 5, 1, 3, 4]))
    # 12
    print(Solution().dividePlayers([3, 4]))
    # -1
    print(Solution().dividePlayers([1, 1, 2, 3]))
