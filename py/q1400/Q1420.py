"""
 * 给你三个整数 n、m 和 k 。下图描述的算法用于找出正整数数组中最大的元素。
 *  maximum_value = -1
 *  maximum_index = -1
 *  search_cost = 0
 *  n = arr.length
 *  for (i = 0; i < n; i++) {
 *      if (maximum_value < arr[i]) {
 *          maximum_value = arr[i]
 *          maximum_index = i
 *          search_cost = search_cost + 1
 *      }
 *  }
 *  return maximum_index
 * 请你生成一个具有下述属性的数组 arr ：
 * 1、arr 中有 n 个整数。
 * 2、1 <= arr[i] <= m 其中 (0 <= i < n) 。
 * 3、将上面提到的算法应用于 arr ，search_cost 的值等于 k 。
 * 返回上述条件下生成数组 arr 的 方法数 ，由于答案可能会很大，所以 必须 对 10^9 + 7 取余。
 * 提示：
 * 1、1 <= n <= 50
 * 2、1 <= m <= 100
 * 3、0 <= k <= n
 * 链接：https://leetcode.cn/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/
"""
from functools import cache


class Solution:

    def numOfArrays(self, n: int, m: int, k: int) -> int:

        MOD = 10**9 + 7

        @cache
        def dfs(idx, mx, cost):
            if idx == n: return 1 if cost == k else 0
            # 增加一个不超过mx的数字
            ans = mx * dfs(idx + 1, mx, cost)
            # 增加一个超过mx的数字
            for i in range(mx + 1, m + 1):
                ans += dfs(idx + 1, i, cost + 1)
            return ans % MOD

        return dfs(0, 0, 0)


if __name__ == '__main__':
    # 6
    print(Solution().numOfArrays(2, 3, 1))
    # 0
    print(Solution().numOfArrays(5, 2, 3))
    # 1
    print(Solution().numOfArrays(9, 1, 1))
    # 34549172
    print(Solution().numOfArrays(50, 100, 25))
    # 418930126
    print(Solution().numOfArrays(37, 17, 7))
