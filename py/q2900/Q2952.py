"""
 * 给你一个下标从 0 开始的整数数组 coins，表示可用的硬币的面值，以及一个整数 target 。
 * 如果存在某个 coins 的子序列总和为 x，那么整数 x 就是一个 可取得的金额 。
 * 返回需要添加到数组中的 任意面值 硬币的 最小数量 ，使范围 [1, target] 内的每个整数都属于 可取得的金额 。
 * 数组的 子序列 是通过删除原始数组的一些（可能不删除）元素而形成的新的 非空 数组，删除过程不会改变剩余元素的相对位置。
 * 提示：
 * 1、1 <= target <= 10^5
 * 2、1<= coins.length <= 10^5
 * 3、1 <= coins[i] <= target
 * 链接：https://leetcode.com/problems/minimum-number-of-coins-to-be-added/
"""
from typing import List


class Solution:

    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        ans = 0
        idx = 0
        num = 1
        while num <= target:
            if idx >= len(coins):
                num += num 
                ans += 1
            elif num == coins[idx]:
                idx += 1
                num += num
            elif num < coins[idx]:
                ans += 1
                num += num
            else:
                num += coins[idx]
                idx += 1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().minimumAddedCoins([1, 4, 10], target=19))
    # 1
    print(Solution().minimumAddedCoins([1, 4, 10, 5, 7, 19], target=19))
    # 3
    print(Solution().minimumAddedCoins([1, 1, 1], target=20))
