"""
 * 给你四个整数 length ，width ，height 和 mass ，分别表示一个箱子的三个维度和质量，请你返回一个表示箱子 类别 的字符串。
 * 1、如果满足以下条件，那么箱子是 "Bulky" 的：
 *  1)、箱子 至少有一个 维度大于等于 10^4 。
 *  2)、或者箱子的 体积 大于等于 10^9 。
 * 2、如果箱子的质量大于等于 100 ，那么箱子是 "Heavy" 的。
 * 3、如果箱子同时是 "Bulky" 和 "Heavy" ，那么返回类别为 "Both" 。
 * 4、如果箱子既不是 "Bulky" ，也不是 "Heavy" ，那么返回类别为 "Neither" 。
 * 5、如果箱子是 "Bulky" 但不是 "Heavy" ，那么返回类别为 "Bulky" 。
 * 6、如果箱子是 "Heavy" 但不是 "Bulky" ，那么返回类别为 "Heavy" 。
 * 注意，箱子的体积等于箱子的长度、宽度和高度的乘积。
 * 提示：
 * 1、1 <= length, width, height <= 10^5
 * 2、1 <= mass <= 10^3
 * 链接：https://leetcode.cn/problems/categorize-box-according-to-criteria
"""

#
# @lc app=leetcode.cn id=2525 lang=python3
#
# [2525] 根据规则将箱子分类
#


# @lc code=start
class Solution:

    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        b = length >= 10**4 or width >= 10**4 or height >= 10**4 or length * width * height >= 10**9
        h = mass >= 100
        if b and h: return 'Both'
        if b: return 'Bulky'
        if h: return 'Heavy'
        return 'Neither'


# @lc code=end

if __name__ == '__main__':
    # "Heavy"
    print(Solution().categorizeBox(1000, width=35, height=700, mass=300))
    # "Neither"
    print(Solution().categorizeBox(200, width=50, height=800, mass=50))
