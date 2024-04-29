"""
 * 给你一个长度为 n 、下标从 0 开始的整数数组 batteryPercentages ，表示 n 个设备的电池百分比。
 * 你的任务是按照顺序测试每个设备 i，执行以下测试操作：
 * 1、如果 batteryPercentages[i] 大于 0：
 *  1）、增加 已测试设备的计数。
 *  2）、将下标在 [i + 1, n - 1] 的所有设备的电池百分比减少 1，确保它们的电池百分比 不会低于 0 ，即 batteryPercentages[j] = max(0, batteryPercentages[j] - 1)。
 *  3）、移动到下一个设备。
 * 2、否则，移动到下一个设备而不执行任何测试。
 * 返回一个整数，表示按顺序执行测试操作后 已测试设备 的数量。
 * 提示：
 * 1、1 <= n == batteryPercentages.length <= 100 
 * 2、0 <= batteryPercentages[i] <= 100
 * 链接：https://leetcode.cn/problems/count-tested-devices-after-test-operations/
"""
from typing import List


class Solution:

    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        n = len(batteryPercentages)
        for i in range(n):
            if batteryPercentages[i]:
                ans += 1
                for j in range(i + 1, n):
                    batteryPercentages[j] = max(0, batteryPercentages[j] - 1)
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().countTestedDevices([1, 1, 2, 1, 3]))
    # 2
    print(Solution().countTestedDevices([0, 1, 2]))
