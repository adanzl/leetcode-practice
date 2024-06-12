"""
 * 给你一个字符串 s，模拟每秒钟的事件 i：
 * 1、如果 s[i] == 'E'，表示有一位顾客进入候诊室并占用一把椅子。
 * 2、如果 s[i] == 'L'，表示有一位顾客离开候诊室，从而释放一把椅子。
 * 返回保证每位进入候诊室的顾客都能有椅子坐的 最少 椅子数，假设候诊室最初是 空的 。
 * 提示：
 * 1、1 <= s.length <= 50
 * 2、s 仅由字母 'E' 和 'L' 组成。
 * 3、s 表示一个有效的进出序列。
 * 链接：https://leetcode.cn/problems/minimum-number-of-chairs-in-a-waiting-room/
"""


class Solution:

    def minimumChairs(self, s: str) -> int:
        ans = 0
        v = 0
        for c in s:
            if c == 'E':
                v += 1
            else:
                v -= 1
            ans = max(ans, v)
        return ans


if __name__ == '__main__':
    # 7
    print(Solution().minimumChairs("EEEEEEE"))
    # 2
    print(Solution().minimumChairs("ELELEEL"))
    # 3
    print(Solution().minimumChairs("ELEELEELLL"))
