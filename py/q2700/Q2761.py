"""
 * 给你一个整数 n 。如果两个整数 x 和 y 满足下述条件，则认为二者形成一个质数对：
 * 1、1 <= x <= y <= n
 * 2、x + y == n
 * 3、x 和 y 都是质数
 * 请你以二维有序列表的形式返回符合题目要求的所有 [xi, yi] ，列表需要按 xi 的 非递减顺序 排序。如果不存在符合要求的质数对，则返回一个空数组。
 * 注意：质数是大于 1 的自然数，并且只有两个因子，即它本身和 1 。
 * 提示：1 <= n <= 10^6
 * 链接：https://leetcode.cn/problems/prime-pairs-with-target-sum/
"""
from typing import List

MX = 10**6 + 5
b_composite = [False] * (MX + 1)  # 假设都不是合数
prime_list = []
for i in range(2, MX + 1):
    if not b_composite[i]:  # i is prime
        prime_list.append(i)

    for prime in prime_list:
        nx = prime * i
        if nx < MX + 1:
            b_composite[nx] = True
        else:
            break


class Solution:

    def findPrimePairs(self, n: int) -> List[List[int]]:
        ans = []
        for p in prime_list:
            if p > n: break
            r = n - p
            if r > 1 and r <= p and not b_composite[r]:
                ans.append([r, p])
        return sorted(ans)


if __name__ == '__main__':
    # []
    print(Solution().findPrimePairs(902444))
    # [[3,7],[5,5]]
    print(Solution().findPrimePairs(10))
    # []
    print(Solution().findPrimePairs(3))
    # []
    print(Solution().findPrimePairs(2))