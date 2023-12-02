"""
 * 「HTML 实体解析器」 是一种特殊的解析器，它将 HTML 代码作为输入，并用字符本身替换掉所有这些特殊的字符实体。
 * HTML 里这些特殊字符和它们对应的字符实体包括：
 * 1、双引号：字符实体为 &quot; ，对应的字符是 " 。
 * 2、单引号：字符实体为 &apos; ，对应的字符是 ' 。
 * 3、与符号：字符实体为 &amp; ，对应对的字符是 & 。
 * 4、大于号：字符实体为 &gt; ，对应的字符是 > 。
 * 5、小于号：字符实体为 &lt; ，对应的字符是 < 。
 * 6、斜线号：字符实体为 &frasl; ，对应的字符是 / 。
 * 给你输入字符串 text ，请你实现一个 HTML 实体解析器，返回解析器解析后的结果。
 * 提示：
 * 1 <= text.length <= 10^5
 * 字符串可能包含 256 个ASCII 字符中的任意字符。
 * 链接：https://leetcode.cn/problems/html-entity-parser
"""

from typing import List

#
# @lc app=leetcode.cn id=1410 lang=python3
#
# [1410] HTML 实体解析器
#


# @lc code=start
class Solution:

    def entityParser(self, text: str) -> str:
        ans = []
        n = len(text)

        def check(idx, ss):
            return idx + len(ss) <= n and text[idx:idx + len(ss)] == ss

        def parse(idx):
            for k, v in [['&quot;', '"'], ['&apos;', "'"], ['&amp;', '&'], ['&gt;', '>'], ['&lt;', '<'],
                         ['&frasl;', '/']]:
                if check(idx, k):
                    ans.append(v)
                    return idx + len(k)
            ans.append(text[idx])
            return idx + 1

        i = 0
        while i < n:
            c = text[i]
            if c == '&':
                i = parse(i)
            else:
                ans.append(c)
                i += 1
        return ''.join(ans)


# @lc code=end

if __name__ == '__main__':
    # "& is an HTML entity but &ambassador; is not."
    print(Solution().entityParser("&amp; is an HTML entity but &ambassador; is not."))
    # "and I quote: \"...\""
    print(Solution().entityParser("and I quote: &quot;...&quot;"))
    # "Stay home! Practice on Leetcode :)"
    print(Solution().entityParser("Stay home! Practice on Leetcode :)"))
    # "x > y && x < y is always false"
    print(Solution().entityParser("x &gt; y &amp;&amp; x &lt; y is always false"))
    # "leetcode.com/problemset/all"
    print(Solution().entityParser("leetcode.com&frasl;problemset&frasl;all"))
