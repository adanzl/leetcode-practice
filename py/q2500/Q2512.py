"""
 * 给你两个字符串数组 positive_feedback 和 negative_feedback ，分别包含表示正面的和负面的词汇。不会 有单词同时是正面的和负面的。
 * 一开始，每位学生分数为 0 。每个正面的单词会给学生的分数 加 3 分，每个负面的词会给学生的分数 减  1 分。
 * 给你 n 个学生的评语，用一个下标从 0 开始的字符串数组 report 和一个下标从 0 开始的整数数组 student_id 表示，其中 student_id[i] 表示这名学生的 ID ，这名学生的评语是 report[i] 。
 * 每名学生的 ID 互不相同。
 * 给你一个整数 k ，请你返回按照得分 从高到低 最顶尖的 k 名学生。如果有多名学生分数相同，ID 越小排名越前。
 * 提示：
 * 1、1 <= positive_feedback.length, negative_feedback.length <= 10^4
 * 2、1 <= positive_feedback[i].length, negative_feedback[j].length <= 100
 * 3、positive_feedback[i] 和 negative_feedback[j] 都只包含小写英文字母。
 * 4、positive_feedback 和 negative_feedback 中不会有相同单词。
 * 5、n == report.length == student_id.length
 * 6、1 <= n <= 10^4
 * 7、report[i] 只包含小写英文字母和空格 ' ' 。
 * 8、report[i] 中连续单词之间有单个空格隔开。
 * 9、1 <= report[i].length <= 100
 * 10、1 <= student_id[i] <= 10^9
 * 11、student_id[i] 的值 互不相同 。
 * 12、1 <= k <= n
 * 链接：https://leetcode.cn/problems/reward-top-k-students
"""
from typing import List


class Solution:

    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        pf, nf = set(positive_feedback), set(negative_feedback)
        a = []
        for r, id in zip(report, student_id):
            score = 0
            for w in r.split():
                if w in pf: score += 3
                elif w in nf: score -= 1
            a.append((score, id))
        ans = []
        for i in sorted(a, key=lambda x: (-x[0], x[1]))[:k]:
            ans.append(i[1])
        return ans


if __name__ == '__main__':
    # [2,1]
    print(Solution().topStudents(["smart", "brilliant", "studious"], negative_feedback=["not"], report=["this student is not studious", "the student is smart"], student_id=[1, 2], k=2))
    # [1,2]
    print(Solution().topStudents(["smart", "brilliant", "studious"], ["not"], ["this student is studious", "the student is smart"], [1, 2], 2))
