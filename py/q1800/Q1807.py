"""
 * 给你一个字符串 s ，它包含一些括号对，每个括号中包含一个 非空 的键。
 * 比方说，字符串 "(name)is(age)yearsold" 中，有 两个 括号对，分别包含键 "name" 和 "age" 。
 * 你知道许多键对应的值，这些关系由二维字符串数组 knowledge 表示，其中 knowledge[i] = [key_i, value_i] ，表示键 key_i 对应的值为 value_i 。
 * 你需要替换 所有 的括号对。当你替换一个括号对，且它包含的键为 key_i 时，你需要：
 * 1、将 key_i 和括号用对应的值 value_i 替换。
 * 2、如果从 knowledge 中无法得知某个键对应的值，你需要将 key_i 和括号用问号 "?" 替换（不需要引号）。
 * knowledge 中每个键最多只会出现一次。s 中不会有嵌套的括号。
 * 请你返回替换 所有 括号对后的结果字符串。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、0 <= knowledge.length <= 10^5
 * 3、knowledge[i].length == 2
 * 4、1 <= key_i.length, value_i.length <= 10
 * 5、s 只包含小写英文字母和圆括号 '(' 和 ')' 。
 * 6、s 中每一个左圆括号 '(' 都有对应的右圆括号 ')' 。
 * 7、s 中每对括号内的键都不会为空。
 * 8、s 中不会有嵌套括号对。
 * 9、key_i 和 value_i 只包含小写英文字母。
 * 10、knowledge 中的 key_i 不会重复。
 * 链接：https://leetcode.cn/problems/evaluate-the-bracket-pairs-of-a-string/
"""
from typing import List


class Solution:

    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dic = {}
        for k, v in knowledge:
            dic[k] = v
        ans = []
        l, r, n = 0, 0, len(s)
        while l < n:
            while l < n and s[l] != '(':
                l += 1
            if l >= n: break
            ans.append(s[r:l])
            while r < n and s[r] != ')':
                r += 1
            l += 1
            ans.append(dic.get(s[l:r], '?'))
            r += 1
        if r < n: ans.append(s[r:])
        return "".join(ans)


if __name__ == '__main__':
    # "?tzv?r"
    print(Solution().evaluate("(fy)(kj)(ege)r", [["uxhhkpvp", "h"], ["nriroroa", "m"], ["wvhiycvo", "z"], ["qsmfeing", "s"], ["hbcyqulf", "q"], ["xwgfjnrf", "b"], ["kfipazun", "s"], ["wnkrtxui", "u"],
                                                 ["abwlsese", "e"], ["iimsmftc", "h"], ["pafqkquo", "v"], ["kj", "tzv"], ["fwwxotcd", "t"], ["yzgjjwjr", "l"]]))
    # "bobistwoyearsold"
    print(Solution().evaluate("(name)is(age)yearsold", knowledge=[["name", "bob"], ["age", "two"]]))
    # "hi?"
    print(Solution().evaluate("hi(name)", knowledge=[["a", "b"]]))
    # "yesyesyesaaa"
    print(Solution().evaluate("(a)(a)(a)aaa", knowledge=[["a", "yes"]]))
