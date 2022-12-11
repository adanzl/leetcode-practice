"""
 * 一个由字母和数字组成的字符串的 值 定义如下：
 * 如果字符串 只 包含数字，那么值为该字符串在 10 进制下的所表示的数字。
 * 否则，值为字符串的 长度 。
 * 给你一个字符串数组 strs ，每个字符串都只由字母和数字组成，请你返回 strs 中字符串的 最大值 。
 * 提示：
 * 1、1 <= strs.length <= 100
 * 2、1 <= strs[i].length <= 9
 * 3、strs[i] 只包含小写英文字母和数字。
 * 链接：https://leetcode.cn/problems/maximum-value-of-a-string-in-an-array
"""
from typing import List


class Solution:

    def maximumValue(self, strs: List[str]) -> int:
        ans, arr = 0, []
        for s in strs:
            if s.isdigit():
                ans = max(ans, int(s))
            else:
                ans = max(ans, len(s))
        return ans


if __name__ == '__main__':
    # 5
    print(Solution().maximumValue(["alic3", "bob", "3", "4", "00000"]))
    # 1
    print(Solution().maximumValue(["1", "01", "001", "0001"]))
