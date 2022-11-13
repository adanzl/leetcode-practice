"""
 * 给你一个四舍五入到两位小数的非负浮点数 celsius 来表示温度，以 摄氏度（Celsius）为单位。
 * 你需要将摄氏度转换为 开氏度（Kelvin）和 华氏度（Fahrenheit），并以数组 ans = [kelvin, fahrenheit] 的形式返回结果。
 * 返回数组 ans 。与实际答案误差不超过 10-5 的会视为正确答案。
 * 注意：
 * 1、开氏度 = 摄氏度 + 273.15
 * 2、华氏度 = 摄氏度 * 1.80 + 32.00
 * 提示：0 <= celsius <= 1000
 * 链接：https://leetcode.cn/problems/convert-the-temperature/
"""

from typing import List


class Solution:

    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]


if __name__ == '__main__':
    # [309.65000,97.70000]
    print(Solution().convertTemperature(36.50))
    # [395.26000,251.79800]
    print(Solution().convertTemperature(122.11))