"""
 * 给你一个字符串 s 和两个整数 x 和 y 。你可以执行下面两种操作任意次。
 * 1、删除子字符串 "ab" 并得到 x 分。比方说，从 "cabxbae" 删除 ab ，得到 "cxbae" 。
 * 2、删除子字符串"ba" 并得到 y 分。比方说，从 "cabxbae" 删除 ba ，得到 "cabxe" 。
 * 请返回对 s 字符串执行上面操作若干次能得到的最大得分。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、1 <= x, y <= 10^4
 * 3、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/maximum-score-from-removing-substrings
"""

#
# @lc app=leetcode.cn id=1717 lang=python3
#
# [1717] 删除子字符串的最大得分
#


# @lc code=start
class Solution:

    def maximumGain(self, s: str, x: int, y: int) -> int:
        s += 'c'
        ans = 0
        # 默认 ab 得分多于 ba，否则交换x、y
        # 使用变量名a、b来表示'a'、'b'（x > y时）
        # 使用变量名a、b来表示'b'、'a'（x < y时）
        # 保证 变量名ab得分为x，且x>y
        a, b = 'a', 'b'
        if x < y:
            a, b = b, a
            x, y = y, x
        count = {a: 0, b: 0}  # 统计之前有多少个a、b未配对
        for i in range(len(s)):
            if s[i] == b:
                # 有未配对的a则与当前的b配对（因此count中所有的b只可能在a的前面）
                if count[a]:
                    ans += x
                    count[a] -= 1
                # b存起来
                else:
                    count[b] += 1
            elif s[i] == a:
                # a存起来
                count[a] += 1
            else:
                # count中有count[b]个b，count[a]个a，且b在a前面，能够凑成min(count[a],count[b])个ba
                ans += min(count[a], count[b]) * y
                count[a] = count[b] = 0
        return ans


# @lc code=end

if __name__ == '__main__':
    # 19
    print(Solution().maximumGain("cdbcbbaaabab", x=4, y=5))
    # 20
    print(Solution().maximumGain("aabbaaxybbaabb", x=5, y=4))
