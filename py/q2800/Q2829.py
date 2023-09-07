"""
 * 给你两个整数 n 和 k 。
 * 对于一个由 不同 正整数组成的数组，如果其中不存在任何求和等于 k 的不同元素对，则称其为 k-avoiding 数组。
 * 返回长度为 n 的 k-avoiding 数组的可能的最小总和。
 * 提示：1 <= n, k <= 50
 * 链接：https://leetcode.cn/problems/determine-the-minimum-sum-of-a-k-avoiding-array/
"""


class Solution:

    def minimumSum(self, n: int, k: int) -> int:
        ans = 0
        avoid = set()
        num = 1
        for _ in range(n):
            while num in avoid:
                num += 1
            ans += num
            avoid.add(k - num)
            num += 1
        return ans


if __name__ == '__main__':
    # 18
    print(Solution().minimumSum(5, k=4))
    # 3
    print(Solution().minimumSum(2, k=6))