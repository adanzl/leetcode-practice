"""
 * 给你一个下标从 0 开始的二维整数数组 questions ，其中 questions[i] = [points_i, brainpower_i] 。
 * 这个数组表示一场考试里的一系列题目，你需要 按顺序 （也就是从问题 0 开始依次解决），针对每个问题选择 解决 或者 跳过 操作。
 * 解决问题 i 将让你 获得  points_i 的分数，但是你将 无法 解决接下来的 brainpower_i 个问题（即只能跳过接下来的 brainpower_i 个问题）。
 * 如果你跳过问题 i ，你可以对下一个问题决定使用哪种操作。
 * 比方说，给你 questions = [[3, 2], [4, 3], [4, 4], [2, 5]] ：
 * 1、如果问题 0 被解决了， 那么你可以获得 3 分，但你不能解决问题 1 和 2 。
 * 2、如果你跳过问题 0 ，且解决问题 1 ，你将获得 4 分但是不能解决问题 2 和 3 。
 * 请你返回这场考试里你能获得的 最高 分数。
 * 提示：
 * 1、1 <= questions.length <= 10^5
 * 2、questions[i].length == 2
 * 3、1 <= points_i, brainpower_i <= 10^5
 * 链接：https://leetcode.cn/problems/solving-questions-with-brainpower/
"""
from typing import List


class Solution:

    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i, (p, b) in enumerate(questions):
            if i > 0:
                dp[i] = max(dp[i], dp[i - 1])
            idx = min(i + b + 1, n)
            dp[idx] = max(dp[idx], dp[i] + p)
        return dp[-1]


if __name__ == '__main__':
    # 5
    print(Solution().mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]))
    # 7
    print(Solution().mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))