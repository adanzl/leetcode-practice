"""
 * 给你一个下标从 0 开始的二维数组 variables ，其中 variables[i] = [a_i, b_i, c_i, m_i]，以及一个整数 target 。
 * 如果满足以下公式，则下标 i 是 好下标：
 * 1、0 <= i < variables.length
 * 2、((a_i^b_i % 10)^c_i) % m_i == target
 * 返回一个由 好下标 组成的数组，顺序不限 。
 * 提示：
 * 1、1 <= variables.length <= 100
 * 2、variables[i] == [a_i, b_i, c_i, m_i]
 * 3、1 <= a_i, b_i, c_i, m_i <= 10^3
 * 4、0 <= target <= 10^3
 * 链接：https://leetcode.cn/problems/double-modular-exponentiation/
"""
from typing import List


class Solution:

    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        return [
            i for i in range(len(variables))
            if target == ((variables[i][0]**variables[i][1] % 10)**variables[i][2]) % variables[i][3]
        ]


if __name__ == '__main__':
    # [0,2]
    print(Solution().getGoodIndices([[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]], target=2))
    # []
    print(Solution().getGoodIndices([[39, 3, 1000, 1000]], target=17))
