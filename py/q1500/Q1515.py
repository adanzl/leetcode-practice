"""
 * 一家快递公司希望在新城市建立新的服务中心。
 * 公司统计了该城市所有客户在二维地图上的坐标，并希望能够以此为依据为新的服务中心选址：
 *     使服务中心 到所有客户的欧几里得距离的总和最小 。
 * 给你一个数组 positions ，其中 positions[i] = [x_i, y_i] 表示第 i 个客户在二维地图上的位置，
 * 返回到所有客户的 欧几里得距离的最小总和 。
 * 换句话说，请你为服务中心选址，该位置的坐标 [x_center, y_center] 需要使下面的公式取到最小值：
 * 与真实值误差在 10^-5之内的答案将被视作正确答案。
 * 提示：
 * 1、1 <= positions.length <= 50
 * 2、positions[i].length == 2
 * 3、0 <= x_i, y_i <= 100
 * 链接：https://leetcode.cn/problems/best-position-for-a-service-centre
"""

from typing import List

#
# @lc app=leetcode.cn id=1515 lang=python3
#
# [1515] 服务中心的最佳位置
#


# @lc code=start
class Solution:

    def getMinDistSum(self, positions: List[List[int]]) -> float:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # 爬山法
        # 初始时，我们选择一个「步长」step，表示每次移动的距离。如果我们当前在位置 (x,y)，我们就依次枚举四个方向 (dx,dy)，
        # 并判断 (x+step⋅dx,y+step⋅dy) 对应的函数值是否更小。
        # 如果找到一个满足要求的方向，我们就进行移动；
        # 否则说明我们当前的「步长」较大，直接越过了最值点，因此调整步长为原来的一半，直到步长小于给定的阈值 e
        eps = 1e-7
        step = 1.0
        decay = 0.5

        n = len(positions)

        x = sum(pos[0] for pos in positions) / n
        y = sum(pos[1] for pos in positions) / n

        # 计算服务中心 (xc, yc) 到客户的欧几里得距离之和
        get_dis = lambda xc, yc: sum(((x - xc)**2 + (y - yc)**2)**0.5 for x, y in positions)

        while step > eps:
            modified = False
            for dx, dy in dirs:
                xNext = x + step * dx
                yNext = y + step * dy
                if get_dis(xNext, yNext) < get_dis(x, y):
                    x, y = xNext, yNext
                    modified = True
                    break
            if not modified:
                step *= (1.0 - decay)

        return get_dis(x, y)


# @lc code=end

if __name__ == '__main__':
    # 4.00000
    print(Solution().getMinDistSum([[0, 1], [1, 0], [1, 2], [2, 1]]))
    # 2.82843
    print(Solution().getMinDistSum([[1, 1], [3, 3]]))
    # 2.73205
    print(Solution().getMinDistSum([[1, 1], [0, 0], [2, 0]]))
