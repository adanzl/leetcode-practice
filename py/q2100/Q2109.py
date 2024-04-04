"""
 * 给你一个下标从 0 开始的字符串 s ，以及一个下标从 0 开始的整数数组 spaces 。
 * 数组 spaces 描述原字符串中需要添加空格的下标。每个空格都应该插入到给定索引处的字符值 之前 。
 * 例如，s = "EnjoyYourCoffee" 且 spaces = [5, 9] ，那么我们需要在 'Y' 和 'C' 之前添加空格，
 * 这两个字符分别位于下标 5 和下标 9 。因此，最终得到 "Enjoy Your Coffee" 。
 * 请你添加空格，并返回修改后的字符串。
 * 提示：
 * 1、1 <= s.length <= 3 * 10^5
 * 2、s 仅由大小写英文字母组成
 * 3、1 <= spaces.length <= 3 * 10^5
 * 4、0 <= spaces[i] <= s.length - 1
 * 5、spaces 中的所有值 严格递增
 * 链接：https://leetcode.cn/problems/adding-spaces-to-a-string/
"""

from typing import List

#
# @lc app=leetcode.cn id=2109 lang=python3
#
# [2109] 向字符串添加空格
#


# @lc code=start
class Solution:

    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        idx = 0
        for i, c in enumerate(s):
            if idx < len(spaces) and i == spaces[idx]:
                ans.append(' ')
                idx += 1
            ans.append(c)
        return ''.join(ans)


# @lc code=end

if __name__ == '__main__':
    # "Leetcode Helps Me Learn"
    print(Solution().addSpaces("LeetcodeHelpsMeLearn", spaces=[8, 13, 15]))
    # "i code in py thon"
    print(Solution().addSpaces("icodeinpython", spaces=[1, 5, 7, 9]))
    # " s p a c i n g"
    print(Solution().addSpaces("spacing", spaces=[0, 1, 2, 3, 4, 5, 6]))
