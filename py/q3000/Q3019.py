"""
 * 给你一个下标从 0 开始的字符串 s ，该字符串由用户输入。按键变更的定义是：使用与上次使用的按键不同的键。
 * 例如 s = "ab" 表示按键变更一次，而 s = "bBBb" 不存在按键变更。
 * 返回用户输入过程中按键变更的次数。
 * 注意：shift 或 caps lock 等修饰键不计入按键变更，也就是说，如果用户先输入字母 'a' 然后输入字母 'A' ，不算作按键变更。
 * 提示：
 * 1、1 <= s.length <= 100
 * 2、s 仅由英文大写字母和小写字母组成。
 * 链接：https://leetcode.cn/problems/find-the-maximum-number-of-elements-in-subset/
"""


class Solution:

    def countKeyChanges(self, s: str) -> int:
        ans = 0
        s = s.lower()
        pre = s[0]
        for i in range(1, len(s)):
            if s[i] != pre:
                ans += 1
            pre = s[i]
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().countKeyChanges("aAbBcC"))
    # 0
    print(Solution().countKeyChanges("AaAaAaaA"))
