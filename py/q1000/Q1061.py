"""
 * 给出长度相同的两个字符串s1 和 s2 ，还有一个字符串 baseStr 。
 * 其中  s1[i] 和 s2[i]  是一组等价字符。
 * 举个例子，如果 s1 = "abc" 且 s2 = "cde"，那么就有 'a' == 'c', 'b' == 'd', 'c' == 'e'。
 * 等价字符遵循任何等价关系的一般规则：
 *  1、自反性 ：'a' == 'a'
 *  2、对称性 ：'a' == 'b' 则必定有 'b' == 'a'
 *  3、传递性 ：'a' == 'b' 且 'b' == 'c' 就表明 'a' == 'c'
 * 例如， s1 = "abc" 和 s2 = "cde" 的等价信息和之前的例子一样，那么 baseStr = "eed" , "acd" 或 "aab"，这三个字符串都是等价的，而 "aab" 是 baseStr 的按字典序最小的等价字符串
 * 利用 s1 和 s2 的等价信息，找出并返回 baseStr 的按字典序排列最小的等价字符串。
 * 提示：
 * 1、1 <= s1.length, s2.length, baseStr <= 1000
 * 2、s1.length == s2.length
 * 3、字符串s1, s2, and baseStr 仅由从 'a' 到 'z' 的小写英文字母组成。
 * 链接：https://leetcode.cn/problems/lexicographically-smallest-equivalent-string/
"""


class Solution:

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        for c in 'abcdefghijklmnopqrstuvwxyz':
            parent[c] = c

        def find(v):
            if parent[v] == v: return v
            parent[v] = find(parent[v])
            return parent[v]

        for k1, k2 in zip(s1, s2):
            r1, r2 = find(k1), find(k2)
            if r1 < r2: parent[r2] = r1
            else: parent[r1] = r2
        ans = list(baseStr)
        for i in range(len(ans)):
            ans[i] = find(ans[i])
        return ''.join(ans)


if __name__ == '__main__':
    # "makkek"
    print(Solution().smallestEquivalentString("parker", s2="morris", baseStr="parser"))
    # "hdld"
    print(Solution().smallestEquivalentString("hello", s2="world", baseStr="hold"))
    # "aauaaaaada"
    print(Solution().smallestEquivalentString("leetcode", s2="programs", baseStr="sourcecode"))
