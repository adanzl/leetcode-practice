"""
 * 给你一个字符串数组 words 和一个字符 separator ，请你按 separator 拆分 words 中的每个字符串。
 * 返回一个由拆分后的新字符串组成的字符串数组，不包括空字符串 。
 * 注意
 * 1、separator 用于决定拆分发生的位置，但它不包含在结果字符串中。
 * 2、拆分可能形成两个以上的字符串。
 * 3、结果字符串必须保持初始相同的先后顺序。
 * 提示：
 * 1、1 <= words.length <= 100
 * 2、1 <= words[i].length <= 20
 * 3、words[i] 中的字符要么是小写英文字母，要么就是字符串 ".,|$#@" 中的字符（不包括引号）
 * 4、separator 是字符串 ".,|$#@" 中的某个字符（不包括引号）
 * 链接：https://leetcode.cn/problems/split-strings-by-separator/
"""
from typing import List


class Solution:

    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            for w in word.split(separator):
                if w:
                    ans.append(w)
        return ans


if __name__ == '__main__':
    # ["one","two","three","four","five","six"]
    print(Solution().splitWordsBySeparator(["one.two.three", "four.five", "six"], separator="."))
    # ["easy","problem"]
    print(Solution().splitWordsBySeparator(["$easy$", "$problem$"], separator="$"))
    # []
    print(Solution().splitWordsBySeparator(["|||"], separator="|"))
