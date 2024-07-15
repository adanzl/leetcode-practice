"""
 * 给出一个字符串 s（仅含有小写英文字母和括号）。
 * 请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
 * 注意，您的结果中 不应 包含任何括号。
 * 提示：
 * 1、1 <= s.length <= 2000
 * 2、s 中只有小写英文字母和括号
 * 3、题目测试用例确保所有括号都是成对出现的
 * 链接：https://leetcode.cn/problems/reverse-substrings-between-each-pair-of-parentheses
"""

#
# @lc app=leetcode.cn id=1190 lang=python3
#
# [1190] 反转每对括号间的子串
#


# @lc code=start
class Solution:

    def reverseParentheses(self, s: str) -> str:
        ans, idx = [], []
        for c in s:
            if c == '(':
                idx.append(len(ans))
            elif c == ')':
                ii = idx.pop()
                ans = ans[:ii] + list(reversed(ans[ii:]))
            else:
                ans.append(c)
        return ''.join(ans)


# @lc code=end

if __name__ == '__main__':
    # "dcba"
    print(Solution().reverseParentheses("(abcd)"))
    # "iloveu"
    print(Solution().reverseParentheses("(u(love)i)"))
    # "leetcode"
    print(Solution().reverseParentheses("(ed(et(oc))el)"))
    # "apmnolkjihgfedcbq"
    print(Solution().reverseParentheses("a(bcdefghijkl(mno)p)q"))
