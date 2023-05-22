"""
 * 我们有一个 n 项的集合。给出两个整数数组 values 和 labels ，第 i 个元素的值和标签分别是 values[i] 和 labels[i]。还会给出两个整数 numWanted 和 useLimit 。
 * 从 n 个元素中选择一个子集 s :
 * 1、子集 s 的大小 小于或等于 numWanted 。
 * 2、s 中 最多 有相同标签的 useLimit 项。
 * 一个子集的 分数 是该子集的值之和。
 * 返回子集 s 的最大 分数 。
 * 提示：
 * 1、n == values.length == labels.length
 * 2、1 <= n <= 2 * 10^4
 * 3、0 <= values[i], labels[i] <= 2 * 10^4
 * 4、1 <= numWanted, useLimit <= n
 * 链接：https://leetcode.cn/problems/largest-values-from-labels/
"""
from collections import Counter
from typing import List


class Solution:

    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        arr = sorted([[values[i], labels[i]] for i in range(len(values))], reverse=True)
        idx, ans, cnt = 0, 0, Counter()
        for v, l in arr:
            if idx >= numWanted:
                break
            if cnt[l] >= useLimit:
                continue
            ans += v
            cnt[l] += 1
            idx += 1
        return ans


if __name__ == '__main__':
    # 9
    print(Solution().largestValsFromLabels([5, 4, 3, 2, 1], labels=[1, 1, 2, 2, 3], numWanted=3, useLimit=1))
    # 12
    print(Solution().largestValsFromLabels([5, 4, 3, 2, 1], labels=[1, 3, 3, 3, 2], numWanted=3, useLimit=2))
    # 16
    print(Solution().largestValsFromLabels([9, 8, 8, 7, 6], labels=[0, 0, 0, 1, 1], numWanted=3, useLimit=1))
