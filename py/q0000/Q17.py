"""
 * 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
 * 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
 * 提示：
 * 1、0 <= digits.length <= 4
 * 2、digits[i] 是范围 ['2', '9'] 的一个数字。
 * 链接：https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
"""
from typing import List


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = ['']
        for d in digits:
            na = []
            for s in ans:
                for c in dic[d]:
                    na.append(s + c)
            ans = na
        return ans if len(ans) > 1 else []


if __name__ == '__main__':
    # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(Solution().letterCombinations('23'))
    # []
    print(Solution().letterCombinations(''))
    # ["a","b","c"]
    print(Solution().letterCombinations('2'))