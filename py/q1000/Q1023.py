"""
 * 如果我们可以将小写字母插入模式串 pattern 得到待查询项 query，那么待查询项与给定模式串匹配。（我们可以在任何位置插入每个字符，也可以插入 0 个字符。）
 * 给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。只有在待查项 queries[i] 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。
 * 提示：
 * 1、1 <= queries.length <= 100
 * 2、1 <= queries[i].length <= 100
 * 3、1 <= pattern.length <= 100
 * 4、所有字符串都仅由大写和小写英文字母组成。
 * 链接：https://leetcode.cn/problems/camelcase-matching/
"""
from typing import List


class Solution:

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        n = len(pattern)
        ans = []
        for q in queries:
            i = 0
            abort = False
            for c in q:
                if i < n and pattern[i] == c:
                    i += 1
                elif c.isupper():
                    ans.append(False)
                    break
            else:
                ans.append(i == n)
        return ans


if __name__ == '__main__':
    # [true,false,true,false,false]
    print(Solution().camelMatch(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FoBa"))
    # [true,false,true,true,false]
    print(Solution().camelMatch(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FB"))
    # [false,true,false,false,false]
    print(Solution().camelMatch(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FoBaT"))
