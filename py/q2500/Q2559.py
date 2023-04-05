"""
 * 给你一个下标从 0 开始的字符串数组 words 以及一个二维整数数组 queries 。
 * 每个查询 queries[i] = [li, ri] 会要求我们统计在 words 中下标在 li 到 ri 范围内（包含 这两个值）并且以元音开头和结尾的字符串的数目。
 * 返回一个整数数组，其中数组的第 i 个元素对应第 i 个查询的答案。
 * 注意：元音字母是 'a'、'e'、'i'、'o' 和 'u' 。
 * 提示：
 * 1、1 <= words.length <= 10^5
 * 2、1 <= words[i].length <= 40
 * 3、words[i] 仅由小写英文字母组成
 * 4、sum(words[i].length) <= 3 * 10^5
 * 5、1 <= queries.length <= 10^5
 * 6、0 <= queries[j][0] <= queries[j][1] < words.length
 * 链接：https://leetcode.cn/problems/count-vowel-strings-in-ranges/
"""
from typing import List


class Solution:

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        pre_sum = [0] * (len(words) + 1)
        for i, w in enumerate(words):
            if w[0] in "aeiou" and w[-1] in "aeiou":
                pre_sum[i + 1] = pre_sum[i] + 1
            else:
                pre_sum[i + 1] = pre_sum[i]
        for l, r in queries:
            ans.append(pre_sum[r + 1] - pre_sum[l])
        return ans


if __name__ == '__main__':
    # [2,3,0]
    print(Solution().vowelStrings(["aba", "bcb", "ece", "aa", "e"], queries=[[0, 2], [1, 4], [1, 1]]))
    # [3,2,1]
    print(Solution().vowelStrings(["a", "e", "i"], queries=[[0, 2], [0, 1], [2, 2]]))