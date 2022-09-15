"""
 * 房间中有 n 只已经打开的灯泡，编号从 1 到 n 。墙上挂着 4 个开关 。
 * 这 4 个开关各自都具有不同的功能，其中：
 * 1、开关 1 ：反转当前所有灯的状态（即开变为关，关变为开）
 * 2、开关 2 ：反转编号为偶数的灯的状态（即 2, 4, ...）
 * 3、开关 3 ：反转编号为奇数的灯的状态（即 1, 3, ...）
 * 4、开关 4 ：反转编号为 j = 3k + 1 的灯的状态，其中 k = 0, 1, 2, ...（即 1, 4, 7, 10, ...）
 * 你必须 恰好 按压开关 presses 次。每次按压，你都需要从 4 个开关中选出一个来执行按压操作。
 * 给你两个整数 n 和 presses ，执行完所有按压之后，返回 不同可能状态 的数量。
 * 提示：
 * 1、1 <= n <= 1000
 * 2、0 <= presses <= 1000
 * 链接：https://leetcode.cn/problems/bulb-switcher-ii
"""


class Solution:

    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0: return 1
        if n <= 2: return 2 if n == 1 else (3 if presses == 1 else 4)
        return (4 if presses == 1 else 7) if presses <= 2 else 8


if __name__ == '__main__':
    # 2
    print(Solution().flipLights(1, 1))
    # 3
    print(Solution().flipLights(2, 1))
    # 4
    print(Solution().flipLights(3, 1))
