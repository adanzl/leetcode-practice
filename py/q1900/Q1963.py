"""
 * 给你一个字符串 s ，下标从 0 开始 ，且长度为偶数 n 。字符串 恰好 由 n / 2 个开括号 '[' 和 n / 2 个闭括号 ']' 组成。
 * 只有能满足下述所有条件的字符串才能称为 平衡字符串 ：
 * 字符串是一个空字符串，或者
 * 字符串可以记作 AB ，其中 A 和 B 都是 平衡字符串 ，或者
 * 字符串可以写成 [C] ，其中 C 是一个 平衡字符串 。
 * 你可以交换 任意 两个下标所对应的括号 任意 次数。
 * 返回使 s 变成 平衡字符串 所需要的 最小 交换次数。
 * 提示：
 * 1、n == s.length
 * 2、2 <= n <= 10^6
 * 3、n 为偶数
 * 4、s[i] 为'[' 或 ']'
 * 5、开括号 '[' 的数目为 n / 2 ，闭括号 ']' 的数目也是 n / 2
 * 链接：https://leetcode.cn/problems/minimum-number-of-swaps-to-make-the-string-balanced
"""


INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=1963 lang=python3
#
# [1963] 使字符串平衡的最小交换次数
#


# @lc code=start
class Solution:

    def minSwaps(self, s: str) -> int:
        cnt = 0
        for c in s:
            if c == '[':
                cnt += 1
            elif cnt:
                cnt -= 1
        return (cnt + 1) // 2


# @lc code=end

if __name__ == '__main__':
    # 4
    print(Solution().minSwaps("]]]][[]]][]][[][][[]][][[]]]][[[[[[["))
    # 4
    print(Solution().minSwaps("]]]][[][[][[[]]][[]][[[[][]]][[]]]]]][]][[][][[]][][[]]]][[[[[[["))
    # 1
    print(Solution().minSwaps("][]["))
    # 2
    print(Solution().minSwaps("]]][[["))
    # 0
    print(Solution().minSwaps("[]"))
