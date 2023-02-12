"""
 * 在一条单车道上有 n 辆车，它们朝着同样的方向行驶。给你一个长度为 n 的数组 cars ，其中 cars[i] = [position_i, speed_i] ，它表示：
 * 1、position_i 是第 i 辆车和道路起点之间的距离（单位：米）。题目保证 position_i < position_i+1 。
 * 2、speed_i 是第 i 辆车的初始速度（单位：米/秒）。
 * 简单起见，所有车子可以视为在数轴上移动的点。当两辆车占据同一个位置时，我们称它们相遇了。
 * 一旦两辆车相遇，它们会合并成一个车队，这个车队里的车有着同样的位置和相同的速度，速度为这个车队里 最慢 一辆车的速度。
 * 请你返回一个数组 answer ，其中 answer[i] 是第 i 辆车与下一辆车相遇的时间（单位：秒），如果这辆车不会与下一辆车相遇，则 answer[i] 为 -1 。
 * 答案精度误差需在 10^-5 以内。
 * 提示：
 * 1、1 <= cars.length <= 10^5
 * 2、1 <= position_i, speed_i <= 10^6
 * 3、position_i < position_i+1
 * 链接：https://leetcode.cn/problems/car-fleet-ii/
"""
from typing import List


class Solution:

    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        # 只和右侧值有关，所以要从右侧遍历。核心是计算每个car与车队头的车从原始位置开始运行之后的碰撞点
        # 将car[i+1]入栈，每次判断（1）【car[i]与s[-1]合并】、（2）【s[-1]与s[-2]合并】哪个时间更短
        # 如果（1）更短则break；如果（2）更短则s[-1]出栈，栈顶元素对于后续计算不再需要
        # car[i]与栈顶元素的碰撞时间为ans[i]对应的值
        n = len(cars)  # position-speed
        ans = [-1.0] * n
        inf = 0x3c3c3c3c
        s = [cars[-1]]  # time-speed-position
        for i in range(n - 2, -1, -1):
            s.append(cars[i + 1])
            p, v = cars[i]
            dt1 = inf
            while len(s) > 1:
                ds1 = v - s[-1][1]
                dt1 = inf if ds1 <= 0 else (s[-1][0] - p) / ds1
                ds2 = s[-1][1] - s[-2][1]
                dt2 = inf if ds2 <= 0 else (s[-2][0] - s[-1][0]) / ds2
                if dt1 < dt2: break
                s.pop()
            if dt1 != inf: ans[i] = dt1
        return ans


if __name__ == '__main__':
    # [2.00000,1.00000,1.50000,-1.00000]
    print(Solution().getCollisionTimes([[3, 4], [5, 4], [6, 3], [9, 1]]))
    # [1.00000,-1.00000,3.00000,-1.00000]
    print(Solution().getCollisionTimes([[1, 2], [2, 1], [4, 3], [7, 2]]))