"""
 * 给你一个 二进制字符串 s 和一个整数数组 queries ，其中 queries[i] = [first_i, second_i] 。
 * 对于第 i 个查询，找到 s 的 最短子字符串 ，它对应的 十进制值 val 与 first_i 按位异或 得到 second_i ，换言之，val ^ first_i == second_i 。
 * 第 i 个查询的答案是子字符串 [left_i, right_i] 的两个端点（下标从 0 开始），如果不存在这样的子字符串，则答案为 [-1, -1] 。如果有多个答案，请你选择 left_i 最小的一个。
 * 请你返回一个数组 ans ，其中 ans[i] = [left_i, right_i] 是第 i 个查询的答案。
 * 子字符串 是一个字符串中一段连续非空的字符序列。
 * 提示：
 * 1、1 <= s.length <= 10^4
 * 2、s[i] 要么是 '0' ，要么是 '1' 。
 * 3、1 <= queries.length <= 10^5
 * 4、0 <= first_i, second_i <= 10^9
 * 链接：https://leetcode.cn/problems/substring-xor-queries/
"""
from typing import List


class Solution:

    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        ans = []
        pos = {}
        for i in range(len(s)):
            for j in range(min(30, i + 1)):
                k = str(int(s[i - j:i + 1]))
                if not k in pos:
                    pos[k] = [i - j, i]
        for v1, v2 in queries:
            k = bin(v1 ^ v2)[2:]
            ans.append(pos[k] if k in pos else [-1, -1])
        return ans


if __name__ == '__main__':
    # [[0,2],[2,3]]
    print(Solution().substringXorQueries("101101", queries=[[0, 5], [1, 2]]))
    # [[-1,-1]]
    print(Solution().substringXorQueries("0101", queries=[[12, 8]]))
    # [[0,0]]
    print(Solution().substringXorQueries("1", queries=[[4, 5]]))
