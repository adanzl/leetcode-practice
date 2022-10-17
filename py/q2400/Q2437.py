"""
 * 给你一个长度为 5 的字符串 time ，表示一个电子时钟当前的时间，格式为 "hh:mm" 。最早 可能的时间是 "00:00" ，最晚 可能的时间是 "23:59" 。
 * 在字符串 time 中，被字符 ? 替换掉的数位是 未知的 ，被替换的数字可能是 0 到 9 中的任何一个。
 * 请你返回一个整数 answer ，将每一个 ? 都用 0 到 9 中一个数字替换后，可以得到的有效时间的数目。
 * 提示：
 * 1、time 是一个长度为 5 的有效字符串，格式为 "hh:mm" 。
 * 2、"00" <= hh <= "23"
 * 3、"00" <= mm <= "59"
 * 4、字符串中有的数位是 '?' ，需要用 0 到 9 之间的数字替换。
 * 链接：https://leetcode.cn/problems/number-of-valid-clock-times/
"""


class Solution:

    def countTime(self, time: str) -> int:
        ans = 0
        v1 = [int(time[0])] if time[0] != '?' else list(range(10))
        v2 = [int(time[1])] if time[1] != '?' else list(range(10))
        v3 = [int(time[3])] if time[3] != '?' else list(range(10))
        v4 = [int(time[4])] if time[4] != '?' else list(range(10))
        for i in v1:
            for j in v2:
                v = i * 10 + j
                for k in v3:
                    for l in v4:
                        vv = k * 10 + l
                        if v < 24 and vv < 60:
                            ans += 1

        return ans


if __name__ == '__main__':
    # 2
    print(Solution().countTime("?5:00"))
    # 100
    print(Solution().countTime("0?:0?"))
    # 1440
    print(Solution().countTime("??:??"))