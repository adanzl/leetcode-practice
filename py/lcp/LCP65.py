"""
 * 力扣嘉年华为了确保更舒适的游览环境条件，在会场的各处设置了湿度调节装置，这些调节装置受控于总控室中的一台控制器。
 * 控制器中已经预设了一些调节指令，整数数组operate[i] 表示第 i 条指令增加空气湿度的大小。现在你可以将任意数量的指令修改为降低湿度（变化的数值不变），以确保湿度尽可能的适宜：
 * 1、控制器会选择 一段连续的指令 ，从而进行湿度调节的操作；
 * 2、这段指令最终对湿度影响的绝对值，即为当前操作的「不适宜度」
 * 3、在控制器所有可能的操作中，最大 的「不适宜度」即为「整体不适宜度」
 * 请返回在所有修改指令的方案中，可以得到的 最小 「整体不适宜度」。
 * 提示：
 * 1、1 <= operate.length <= 1000
 * 2、1 <= operate[i] <= 1000
 * 链接：https://leetcode.cn/problems/3aqs1c/
"""
from typing import List


class Solution:

    def unSuitability(self, operate: List[int]) -> int:
        # 任意子数组和的绝对值的最大值 = 前缀和数组最大值 - 前缀和数组最小值
        # 「整体不适宜度」== 任意子数组和的绝对值的最大值
        # 原问题转化为求为每个数组元素加+-号之后，求 任意子数组和的绝对值的最大值 的最小值
        limit = max(operate) * 2 + 1
        inf = 0x3c3c3c3c
        # 我们需要（当前前缀和，最大前缀和，最小前缀和）来表示数组状态，替换为（当前前缀和-最小前缀和，最大前缀和-最小前缀和）
        # 滚动dp[i][j]: 第i个数时前缀和距离最小前缀和的距离
        dp = [0] + [inf] * limit
        for x in operate:
            ndp = [inf] * (limit + 1)
            for j, dis in enumerate(dp):
                if dis == inf: continue  # 无效的长度（无法组成）
                if j + x <= limit: ndp[j + x] = min(ndp[j + x], max(dis, j + x))
                if j >= x: ndp[j - x] = min(ndp[j - x], dis)
                else:
                    ndp[0] = min(ndp[0], dis - j + x)
            dp = ndp
        return min(dp)


if __name__ == '__main__':
    # 8
    print(Solution().unSuitability([5, 3, 7]))
    # 20
    print(Solution().unSuitability([20, 10]))
