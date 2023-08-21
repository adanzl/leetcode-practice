"""
 * 给你两个正整数 low 和 high ，都用字符串表示，请你统计闭区间 [low, high] 内的 步进数字 数目。
 * 如果一个整数相邻数位之间差的绝对值都 恰好 是 1 ，那么这个数字被称为 步进数字 。
 * 请你返回一个整数，表示闭区间 [low, high] 之间步进数字的数目。
 * 由于答案可能很大，请你将它对 10^9 + 7 取余 后返回。
 * 注意：步进数字不能有前导 0 。
 * 提示：
 * 1、1 <= int(low) <= int(high) < 10^100
 * 2、1 <= low.length, high.length <= 100
 * 3、low 和 high 只包含数字。
 * 4、low 和 high 都不含前导 0 。
 * 链接：https://leetcode.cn/problems/count-stepping-numbers-in-range/
"""
from functools import cache


class Solution:

    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10**9 + 7
        h = tuple(map(int, high))
        l = tuple(map(int, str(int(low)-1)))

        @cache
        def dfs(idx, is_limit, is_num, pre, arr):
            if idx == len(arr): return int(is_num)
            ret = 0
            if not is_num:
                ret += dfs(idx + 1, False, False, -1, arr)
            nums = []
            up = arr[idx] if is_limit else 9
            if pre == -1:
                nums = [i for i in range(1, 10 if not is_limit else arr[idx] + 1)]
            else:
                if pre > 0 and pre - 1 <= up: nums.append(pre - 1)
                if pre < up: nums.append(pre + 1)
            for num in nums:
                ret += dfs(idx + 1, is_limit and num == arr[idx], True, num, arr)
            return ret

        return (dfs(0, True, False, -1, h) - dfs(0, True, False, -1, l) + MOD) % MOD


if __name__ == '__main__':
    # 125046265
    print(Solution().countSteppingNumbers("1", "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999"))
    # 2
    print(Solution().countSteppingNumbers("90", high="101"))
    # 10
    print(Solution().countSteppingNumbers("1", high="11"))