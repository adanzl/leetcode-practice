"""
 * 你有 n 枚花的种子。每枚种子必须先种下，才能开始生长、开花。播种需要时间，种子的生长也是如此。给你两个下标从 0 开始的整数数组 plantTime 和 growTime ，每个数组的长度都是 n ：
 * 1、plantTime[i] 是 播种 第 i 枚种子所需的 完整天数 。每天，你只能为播种某一枚种子而劳作。无须 连续几天都在种同一枚种子，但是种子播种必须在你工作的天数达到 plantTime[i] 之后才算完成。
 * 2、growTime[i] 是第 i 枚种子完全种下后生长所需的 完整天数 。在它生长的最后一天 之后 ，将会开花并且永远 绽放 。
 * 从第 0 开始，你可以按 任意 顺序播种种子。
 * 返回所有种子都开花的 最早 一天是第几天。
 * 提示：
 * 1、n == plantTime.length == growTime.length
 * 2、1 <= n <= 10^5
 * 3、1 <= plantTime[i], growTime[i] <= 10^4
 * 链接：https://leetcode.cn/problems/earliest-possible-day-of-full-bloom/
"""
from typing import List


class Solution:

    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        arr = sorted(list(zip(plantTime, growTime)), key=lambda x: (-x[1], x[0]))
        ans, pre = 0, 0
        for p, g in arr:
            pre += p
            ans = max(ans, pre + g)
        return ans


if __name__ == '__main__':
    # 9
    print(Solution().earliestFullBloom([1, 4, 3], [2, 3, 1]))
    # 9
    print(Solution().earliestFullBloom([1, 2, 3, 2], [2, 1, 2, 1]))
    # 2
    print(Solution().earliestFullBloom([1], [1]))
