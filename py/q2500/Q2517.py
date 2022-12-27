"""
 * 给你一个正整数数组 price ，其中 price[i] 表示第 i 类糖果的价格，另给你一个正整数 k 。
 * 商店组合 k 类 不同 糖果打包成礼盒出售。礼盒的 甜蜜度 是礼盒中任意两种糖果 价格 绝对差的最小值。
 * 返回礼盒的 最大 甜蜜度。
 * 提示：
 * 1、1 <= price.length <= 10^5
 * 2、1 <= price[i] <= 10^9
 * 3、2 <= k <= price.length
 * 链接：https://leetcode.cn/problems/maximum-tastiness-of-candy-basket/
"""
from typing import List


class Solution:

    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        l, r = 0, price[-1] * 2
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            cnt = 1
            idx = 0
            for i in range(1, len(price)):
                if price[i] - price[idx] >= mid:
                    cnt += 1
                    idx = i
            if cnt >= k:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


if __name__ == '__main__':
    # 0
    print(Solution().maximumTastiness([7, 7, 7, 7], 2))
    # 19
    print(Solution().maximumTastiness([34, 116, 83, 15, 150, 56, 69, 42, 26], 6))
    # 2
    print(Solution().maximumTastiness([1, 3, 1], 2))
    # 8
    print(Solution().maximumTastiness([13, 5, 1, 8, 21, 2], 3))
