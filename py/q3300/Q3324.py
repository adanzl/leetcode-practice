"""
 * 给你一个字符串 target。
 * Alice 将会使用一种特殊的键盘在她的电脑上输入 target，这个键盘 只有两个 按键：
 * 1、按键 1：在屏幕上的字符串后追加字符 'a'。
 * 2、按键 2：将屏幕上字符串的 最后一个 字符更改为英文字母表中的 下一个 字符。例如，'c' 变为 'd'，'z' 变为 'a'。
 * 注意，最初屏幕上是一个空字符串 ""，所以她 只能 按按键 1。
 * 请你考虑按键次数 最少 的情况，按字符串出现顺序，返回 Alice 输入 target 时屏幕上出现的所有字符串列表。
 * 提示：
 * 1、1 <= target.length <= 400
 * 2、target 仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/find-the-sequence-of-strings-appeared-on-the-screen/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def stringSequence(self, target: str) -> List[str]:
        ans = []
        for c in target:
            if not ans:
                ans.append('a')
            while ans[-1][-1] != c:
                ans.append(ans[-1][:-1] + chr(ord(ans[-1][-1]) + 1))
            ans.append(ans[-1] + 'a')
        return ans[:-1]




if __name__ == '__main__':
    # ["a","aa","ab","aba","abb","abc"]
    print(Solution().stringSequence("abc"))
    # ["a","b","c","d","e","f","g","h","ha","hb","hc","hd","he"]
    print(Solution().stringSequence("he"))
    #
    # print(Solution().stringSequence())
