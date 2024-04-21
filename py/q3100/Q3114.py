"""
 * 给你一个字符串 s，表示一个 12 小时制的时间格式，其中一些数字（可能没有）被 "?" 替换。
 * 12 小时制时间格式为 "HH:MM" ，其中 HH 的取值范围为 00 至 11，MM 的取值范围为 00 至 59。最早的时间为 00:00，最晚的时间为 11:59。
 * 你需要将 s 中的 所有 "?" 字符替换为数字，使得结果字符串代表的时间是一个 有效 的 12 小时制时间，并且是可能的 最晚 时间。
 * 返回结果字符串。
 * 提示：
 * 1、s.length == 5
 * 2、s[2] 是字符 ":"
 * 3、除 s[2] 外，其他字符都是数字或 "?"
 * 4、输入保证在替换 "?" 字符后至少存在一个介于 "00:00" 和 "11:59" 之间的时间。
 * 链接：https://leetcode.cn/problems/latest-time-you-can-obtain-after-replacing-characters/
"""


class Solution:

    def findLatestTime(self, s: str) -> str:
        ans = list(s)
        for i, c in enumerate(s):
            if c == '?':
                if i == 0:
                    ans[i] = '1' if s[i + 1] == '?' or int(s[i + 1]) < 2 else '0'
                elif i == 1:
                    ans[i] = '1' if ans[i - 1] == '1' else '9'
                elif i == 3:
                    ans[i] = '5'
                else:
                    ans[i] = '9'
        return ''.join(ans)


if __name__ == '__main__':
    # "11:59"
    print(Solution().findLatestTime("1?:??"))
    # "03:12"
    print(Solution().findLatestTime("?3:12"))
    # "11:54"
    print(Solution().findLatestTime("1?:?4"))
    # "09:59"
    print(Solution().findLatestTime("0?:5?"))
    # "09:59"
    print(Solution().findLatestTime("0?:5?"))
    # "11:19"
    print(Solution().findLatestTime("??:1?"))
