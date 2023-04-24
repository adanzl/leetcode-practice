"""
 * 远征队即将开启未知的冒险之旅，不过在此之前，将对补给车队进行最后的检查。supplies[i] 表示编号为 i 的补给马车装载的物资数量。
 * 考虑到车队过长容易被野兽偷袭，他们决定将车队的长度变为原来的一半（向下取整），计划为：
 * 1、找出车队中 物资之和最小 两辆 相邻 马车，将它们车辆的物资整合为一辆。若存在多组物资之和相同的马车，则取编号最小的两辆马车进行整合；
 * 2、重复上述操作直到车队长度符合要求。
 * 请返回车队长度符合要求后，物资的分布情况。
 * 解释：
 * 1、2 <= supplies.length <= 1000
 * 2、1 <= supplies[i] <= 1000
 * 链接：https://leetcode.cn/problems/hqCnmP/
"""
from itertools import pairwise
from typing import List


class Solution:

    def supplyWagon(self, supplies: List[int]) -> List[int]:
        ans = supplies
        n = len(supplies)
        for _ in range(n - n // 2):
            mnv, idx = min([[v1 + v2, i] for i, (v1, v2) in enumerate(pairwise(ans))])
            ans = ans[:idx] + [mnv] + ans[idx + 2:]
        return ans


if __name__ == '__main__':
    #
    # print(Solution().supplyWagon())
    # [10,15]
    print(Solution().supplyWagon([7, 3, 6, 1, 8]))
    # [5,5]
    print(Solution().supplyWagon([1, 3, 1, 5]))