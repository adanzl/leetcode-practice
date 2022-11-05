"""
 * 给你一个字符串数组 words ，每一个字符串长度都相同，令所有字符串的长度都为 n 。
 * 每个字符串 words[i] 可以被转化为一个长度为 n - 1 的 差值整数数组 difference[i] ，其中对于 0 <= j <= n - 2 有 difference[i][j] = words[i][j+1] - words[i][j] 。
 * 注意两个字母的差值定义为它们在字母表中 位置 之差，也就是说 'a' 的位置是 0 ，'b' 的位置是 1 ，'z' 的位置是 25 。
 * 比方说，字符串 "acb" 的差值整数数组是 [2 - 0, 1 - 2] = [2, -1] 。
 * words 中所有字符串 除了一个字符串以外 ，其他字符串的差值整数数组都相同。你需要找到那个不同的字符串。
 * 请你返回 words中 差值整数数组 不同的字符串。
 * 提示：
 * 1、3 <= words.length <= 100
 * 2、n == words[i].length
 * 3、2 <= n <= 20
 * 4、words[i] 只含有小写英文字母。
 * 链接：https://leetcode.cn/problems/odd-string-difference/
"""
from typing import List


class Solution:

    def oddString(self, words: List[str]) -> str:
        m = dict()
        exp = ""
        for word in words:
            diff = []
            for i in range(1, len(word)):
                diff.append(ord(word[i]) - ord(word[i - 1]))
            k = ",".join(str(v) for v in diff)
            if k in m: exp = k
            m[k] = word
        for key in m.keys():
            if key != exp: return m[key]
        return ""


if __name__ == '__main__':
    # "abc"
    print(Solution().oddString(["adc", "wzy", "abc"]))
    # "bob"
    print(Solution().oddString(["aaa", "bob", "ccc", "ddd"]))
