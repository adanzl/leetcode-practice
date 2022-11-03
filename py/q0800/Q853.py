"""
 * 在一条单行道上，有 n 辆车开往同一目的地。目的地是几英里以外的 target 。
 * 给定两个整数数组 position 和 speed ，长度都是 n ，其中 position[i] 是第 i 辆车的位置， speed[i] 是第 i 辆车的速度(单位是英里/小时)。
 * 一辆车永远不会超过前面的另一辆车，但它可以追上去，并与前车 以相同的速度 紧接着行驶。此时，我们会忽略这两辆车之间的距离，也就是说，它们被假定处于相同的位置。
 * 车队 是一些由行驶在相同位置、具有相同速度的车组成的非空集合。注意，一辆车也可以是一个车队。
 * 即便一辆车在目的地才赶上了一个车队，它们仍然会被视作是同一个车队。
 * 返回到达目的地的 车队数量 。
 * 提示：
 * 1、n == position.length == speed.length
 * 2、1 <= n <= 10^5
 * 3、0 < target <= 10^6
 * 4、0 <= position[i] < target
 * 5、position 中每个值都 不同
 * 6、0 < speed[i] <= 10^6
 * 链接：https://leetcode.cn/problems/car-fleet/
"""
from typing import List


class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # i < j and time[i]<time[j] 会被合并
        times = sorted([[(target - p) / v, p] for p, v in zip(position, speed)], key=lambda x: x[1])
        s = []
        ans = len(times)
        for time in times:
            while s and s[-1] <= time[0]:
                s.pop()
                ans -= 1
            s.append(time[0])
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().carFleet(10, [0, 4, 2], [2, 1, 3]))
    # 1
    print(Solution().carFleet(100, [0, 2, 4], [4, 2, 1]))
    # 3
    print(Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    # 1
    print(Solution().carFleet(10, [3], [3]))
