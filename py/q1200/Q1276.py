"""
 * 圣诞活动预热开始啦，汉堡店推出了全新的汉堡套餐。为了避免浪费原料，请你帮他们制定合适的制作计划。
 * 给你两个整数 tomatoSlices 和 cheeseSlices，分别表示番茄片和奶酪片的数目。不同汉堡的原料搭配如下：
 * 1、巨无霸汉堡：4 片番茄和 1 片奶酪
 * 2、小皇堡：2 片番茄和 1 片奶酪
 * 请你以 [total_jumbo, total_small]（[巨无霸汉堡总数，小皇堡总数]）的格式返回恰当的制作方案，使得剩下的番茄片 tomatoSlices 和奶酪片 cheeseSlices 的数量都是 0。
 * 如果无法使剩下的番茄片 tomatoSlices 和奶酪片 cheeseSlices 的数量为 0，就请返回 []。
 * 提示：
 * 1、0 <= tomatoSlices <= 10^7
 * 2、0 <= cheeseSlices <= 10^7
 * 链接：https://leetcode.cn/problems/number-of-burgers-with-no-waste-of-ingredients
"""
from typing import List
#
# @lc app=leetcode.cn id=1276 lang=python3
#
#

# @lc code=start


class Solution:

    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        x = (tomatoSlices - cheeseSlices * 2) / 2
        y = cheeseSlices - x
        return [] if x < 0 or y < 0 or x != int(x) else [int(x), int(y)]


# @lc code=end

if __name__ == '__main__':
    # [1,6]
    print(Solution().numOfBurgers(16, cheeseSlices=7))
    # []
    print(Solution().numOfBurgers(17, cheeseSlices=4))
    # []
    print(Solution().numOfBurgers(4, cheeseSlices=17))
    # [0,0]
    print(Solution().numOfBurgers(0, cheeseSlices=0))
    # [0,1]
    print(Solution().numOfBurgers(2, cheeseSlices=1))
