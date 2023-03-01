"""
 * 给你一个整数数组 banned 和两个整数 n 和 maxSum 。你需要按照以下规则选择一些整数：
 * 1、被选择整数的范围是 [1, n] 。
 * 2、每个整数 至多 选择 一次 。
 * 3、被选择整数不能在数组 banned 中。
 * 4、被选择整数的和不超过 maxSum 。
 * 请你返回按照上述规则 最多 可以选择的整数数目。
 * 提示：
 * 1、1 <= banned.length <= 10^4
 * 2、1 <= banned[i], n <= 10^4
 * 3、1 <= maxSum <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-number-of-integers-to-choose-from-a-range-i/
"""
from typing import List


class Solution:

    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        sm, ans = 0, 0
        ban = set(banned)
        for i in range(1, n + 1):
            if i in ban: continue
            if sm + i > maxSum: break
            sm += i
            ans += 1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().maxCount([1, 6, 5], n=5, maxSum=6))
    # 0
    print(Solution().maxCount([1, 2, 3, 4, 5, 6, 7], n=8, maxSum=1))
    # 7
    print(Solution().maxCount([11], n=7, maxSum=50))
