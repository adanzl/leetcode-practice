"""
 * 给你一个整数 limit 和一个大小为 n x 2 的二维数组 queries 。
 * 总共有 limit + 1 个球，每个球的编号为 [0, limit] 中一个 互不相同 的数字。
 * 一开始，所有球都没有颜色。queries 中每次操作的格式为 [x, y] ，你需要将球 x 染上颜色 y 。
 * 每次操作之后，你需要求出所有球中 不同 颜色的数目。
 * 请你返回一个长度为 n 的数组 result ，其中 result[i] 是第 i 次操作以后不同颜色的数目。
 * 注意 ，没有染色的球不算作一种颜色。
 * 提示：
 * 1、1 <= limit <= 10^9
 * 2、1 <= n == queries.length <= 10^5
 * 3、queries[i].length == 2
 * 4、0 <= queries[i][0] <= limit
 * 5、1 <= queries[i][1] <= 10^9
 * 链接：https://leetcode.cn/problems/find-the-number-of-distinct-colors-among-the-balls/description/
"""
from typing import Counter, List


class Solution:

    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = []
        color = Counter()
        cnt = Counter()
        for x, y in queries:
            if color[x]:
                cnt[color[x]] -= 1
                if cnt[color[x]] == 0:
                    del cnt[color[x]]
            color[x] = y
            cnt[y] += 1
            ans.append(len(cnt))
        return ans


if __name__ == '__main__':
    # [1,2,2,3]
    print(Solution().queryResults(4, queries=[[1, 4], [2, 5], [1, 3], [3, 4]]))
    # [1,2,2,3,4]
    print(Solution().queryResults(4, queries=[[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]))
