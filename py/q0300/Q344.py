"""
 * 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
 * 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s[i] 都是 ASCII 码表中的可打印字符
 * 链接：https://leetcode.cn/problems/reverse-string/
"""
from typing import List


class Solution:

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


if __name__ == '__main__':
    # ["o","l","l","e","h"]
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    print(s)
    # ["h","a","n","n","a","H"]
    s = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(s)
    print(s)