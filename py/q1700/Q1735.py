"""
 * 给你一个二维整数数组 queries ，其中 queries[i] = [ni, ki] 。
 * 第 i 个查询 queries[i] 要求构造长度为 ni 、每个元素都是正整数的数组，且满足所有元素的乘积为 ki ，请你找出有多少种可行的方案。
 * 由于答案可能会很大，方案数需要对 10^9 + 7 取余 。
 * 请你返回一个整数数组 answer，满足 answer.length == queries.length ，其中 answer[i]是第 i 个查询的结果。
 * 提示：
 * 1、1 <= queries.length <= 10^4 
 * 2、1 <= ni, ki <= 10^4
 * 链接：https://leetcode.cn/problems/count-ways-to-make-array-with-product/
"""
from collections import Counter
from math import comb
from typing import List

#
# @lc app=leetcode.cn id=1735 lang=python3
#
# [1735] 生成乘积数组的方案数
#

# @lc code=start

# 约数 预处理
divisors = [[], []]
for i in range(2, 10**4 + 1):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            divisors.append(divisors[i // j] + [j])
            break
    else:
        divisors.append([i])


class Solution:

    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        res = []
        for i, j in queries:
            c = Counter(divisors[j])
            x = 1
            for k in c.values():
                x *= comb(i + k - 1, k)
                x %= 10**9 + 7
            res.append(x % (10**9 + 7))
        return res


# @lc code=end
if __name__ == '__main__':
    # [4,1,50734910]
    print(Solution().waysToFillArray([[2, 6], [5, 1], [73, 660]]))
    # [1,2,3,10,5]
    print(Solution().waysToFillArray([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))
    # [4, 1, 418224726]
    print(Solution().waysToFillArray([[2, 6], [5, 1], [10000, 10000]]))