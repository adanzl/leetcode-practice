"""
 * 给你一个餐馆信息数组 restaurants，其中  restaurants[i] = [id_i, rating_i, veganFriendly_i, price_i, distance_i]。
 * 你必须使用以下三个过滤器来过滤这些餐馆信息。
 * 其中素食者友好过滤器 veganFriendly 的值可以为 true 或者 false，如果为 true 就意味着你应该只包括 veganFriendly_i 为 true 的餐馆，
 * 为 false 则意味着可以包括任何餐馆。
 * 此外，我们还有最大价格 maxPrice 和最大距离 maxDistance 两个过滤器，它们分别考虑餐厅的价格因素和距离因素的最大值。
 * 过滤后返回餐馆的 id，按照 rating 从高到低排序。如果 rating 相同，那么按 id 从高到低排序。
 * 简单起见， veganFriendly_i 和 veganFriendly 为 true 时取值为 1，为 false 时，取值为 0 。
 * 提示：
 * 1、1 <= restaurants.length <= 10^4
 * 2、restaurants[i].length == 5
 * 3、1 <= id_i, rating_i, price_i, distance_i <= 10^5
 * 4、1 <= maxPrice, maxDistance <= 10^5
 * 5、veganFriendly_i 和 veganFriendly 的值为 0 或 1 。
 * 6、所有 id_i 各不相同。
 * 链接：https://leetcode.cn/problems/filter-restaurants-by-vegan-friendly-price-and-distance
"""

from typing import List

#
# @lc app=leetcode.cn id=1333 lang=python3
#
# [1333] 餐厅过滤器
#


# @lc code=start
class Solution:

    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ans = []
        for id, rating, vegan, price, distance in restaurants:
            if veganFriendly and not vegan: continue
            if price > maxPrice: continue
            if distance > maxDistance: continue
            ans.append([id, rating])
        ans.sort(key=lambda x: (x[1], x[0]), reverse=True)
        return [x[0] for x in ans]


# @lc code=end

if __name__ == '__main__':
    # [3,1,5]
    print(Solution().filterRestaurants([[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]], veganFriendly=1, maxPrice=50, maxDistance=10))
    # [4,3,2,1,5]
    print(Solution().filterRestaurants([[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]], veganFriendly=0, maxPrice=50, maxDistance=10))
    # [4,5]
    print(Solution().filterRestaurants([[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]], veganFriendly=0, maxPrice=30, maxDistance=3))
