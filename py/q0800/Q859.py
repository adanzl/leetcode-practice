"""
 * 给你两个字符串 s 和 goal ，只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果，就返回 true ；否则返回 false 。
 * 交换字母的定义是：取两个下标 i 和 j （下标从 0 开始）且满足 i != j ，接着交换 s[i] 和 s[j] 处的字符。
 * 例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。
 * 提示：
 * 1、1 <= s.length, goal.length <= 2 * 10^4
 * 2、s 和 goal 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/buddy-strings
"""


class Solution:

    def buddyStrings(self, s: str, goal: str) -> bool:
        d = []
        if len(s) != len(goal): return False
        for i, (s1, s2) in enumerate(zip(s, goal)):
            if s1 != s2:
                d.append(i)
        return (len(d) == 2 and s[d[0]] == goal[d[1]] and s[d[1]] == goal[d[0]]) or (len(d) == 0 and len(set(s)) < len(s))


if __name__ == '__main__':
    # True
    print(Solution().buddyStrings("ab", goal="ba"))
    # False
    print(Solution().buddyStrings("ab", goal="ab"))
    # True
    print(Solution().buddyStrings("aa", goal="aa"))
