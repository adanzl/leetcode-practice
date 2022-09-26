"""
 * 给你一个字符串数组 names ，和一个由 互不相同 的正整数组成的数组 heights 。两个数组的长度均为 n 。
 * 对于每个下标 i，names[i] 和 heights[i] 表示第 i 个人的名字和身高。
 * 请按身高 降序 顺序返回对应的名字数组 names 。
 * 提示：
 * 1、n == names.length == heights.length
 * 2、1 <= n <= 10^3
 * 3、1 <= names[i].length <= 20
 * 4、1 <= heights[i] <= 10^5
 * 5、names[i] 由大小写英文字母组成
 * 6、heights 中的所有值互不相同
 * 链接：https://leetcode.cn/problems/sort-the-people/
"""

from typing import *


class Solution:

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [x[1] for x in sorted(zip(heights, names), reverse=True)]


if __name__ == '__main__':
    # ['Mary', 'Emma', 'John']
    print(Solution().sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))
    # ['Bob', 'Alice', 'Bob']
    print(Solution().sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]))
