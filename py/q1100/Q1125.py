"""
 * 作为项目经理，你规划了一份需求的技能清单 req_skills，并打算从备选人员名单 people 中选出些人组成一个「必要团队」（ 编号为 i 的备选人员 people[i] 含有一份该备选人员掌握的技能列表）。
 * 所谓「必要团队」，就是在这个团队中，对于所需求的技能列表 req_skills 中列出的每项技能，团队中至少有一名成员已经掌握。可以用每个人的编号来表示团队中的成员：
 * 例如，团队 team = [0, 1, 3] 表示掌握技能分别为 people[0]，people[1]，和 people[3] 的备选人员。
 * 请你返回 任一 规模最小的必要团队，团队成员用人员编号表示。你可以按 任意顺序 返回答案，题目数据保证答案存在。
 * 提示：
 * 1、1 <= req_skills.length <= 16
 * 2、1 <= req_skills[i].length <= 16
 * 3、req_skills[i] 由小写英文字母组成
 * 4、req_skills 中的所有字符串 互不相同
 * 5、1 <= people.length <= 60
 * 6、0 <= people[i].length <= 16
 * 7、1 <= people[i][j].length <= 16
 * 8、people[i][j] 由小写英文字母组成
 * 9、people[i] 中的所有字符串 互不相同
 * 10、people[i] 中的每个技能是 req_skills 中的技能
 * 11、题目数据保证「必要团队」一定存在
 * 链接：https://leetcode.cn/problems/smallest-sufficient-team/
"""
from typing import List


class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skills = dict({k: v for k, v in zip(req_skills, range(len(req_skills)))})
        n = len(skills)
        inf = 0x3c3c3c3c
        dp = [inf] * (1 << n)
        ans = [[] for _ in range(1 << n)]
        dp[0] = 0
        for idx, p in enumerate(people):
            m = 0
            for s in p:
                m |= 1 << skills[s]
            for i in range(len(dp)):
                if dp[i | m] > dp[i] + 1:
                    dp[i | m] = dp[i] + 1
                    ans[i | m] = ans[i] + [idx]
        return ans[-1]


if __name__ == '__main__':
    # [0,2]
    print(Solution().smallestSufficientTeam(["java", "nodejs", "reactjs"], [["java"], ["nodejs"], ["nodejs", "reactjs"]]))
    # [1,2]
    print(Solution().smallestSufficientTeam(["algorithms", "math", "java", "reactjs", "csharp", "aws"],
                                            [["algorithms", "math", "java"], ["algorithms", "math", "reactjs"], ["java", "csharp", "aws"], ["reactjs", "csharp"], ["csharp", "math"], ["aws", "java"]]))
