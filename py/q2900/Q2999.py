"""
 * 给你三个整数 start ，finish 和 limit 。同时给你一个下标从 0 开始的字符串 s ，表示一个 正 整数。
 * 如果一个 正 整数 x 末尾部分是 s （换句话说，s 是 x 的 后缀），且 x 中的每个数位至多是 limit ，那么我们称 x 是 强大的 。
 * 请你返回区间 [start..finish] 内强大整数的 总数目 。
 * 如果一个字符串 x 是 y 中某个下标开始（包括 0 ），到下标为 y.length - 1 结束的子字符串，那么我们称 x 是 y 的一个后缀。
 * 比方说，25 是 5125 的一个后缀，但不是 512 的后缀。
 * 提示：
 * 1、1 <= start <= finish <= 10^15
 * 2、1 <= limit <= 9
 * 3、1 <= s.length <= floor(log10(finish)) + 1
 * 4、s 数位中每个数字都小于等于 limit 。
 * 5、s 不包含任何前导 0 。
 * 链接：https://leetcode.cn/problems/count-the-number-of-powerful-integers/
"""
from functools import cache


class Solution:

    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        if int(s) > finish:
            return 0
        suf = int(s)

        def calc(high: int) -> int:
            if high < suf:
                return 0
            s_high = str(high)
            r = high % (10**len(s))
            if r < suf:
                high -= suf
                s_high = str(high)

            ss = len(s_high) - len(s)
            # 第 i 位开始填充数字，返回合法数字个数
            # is_limit 当前位置是否受到num限制，首次调用要True
            # is_num 是否已经是一个数了，区分是否可以前导0
            @cache
            def f(i: int, is_limit: bool, is_num: bool) -> int:
                if i == ss: return 1
                ret = 0
                if not is_num:
                    ret += f(i + 1, False, False)
                up = int(s_high[i]) if is_limit else 9
                up = min(limit, up)
                down = 0 if is_num else 1
                for num in range(down, up + 1):
                    ret += f(i + 1, num == int(s_high[i]) and is_limit, True)
                return ret

            return f(0, True, False)

        return calc(finish) - calc(start - 1)


if __name__ == '__main__':
    # 5
    print(Solution().numberOfPowerfulInt(1, finish=6000, limit=4, s="124"))
    # 2
    print(Solution().numberOfPowerfulInt(15, finish=215, limit=6, s="10"))
    # 0
    print(Solution().numberOfPowerfulInt(1000, finish=2000, limit=4, s="3000"))
