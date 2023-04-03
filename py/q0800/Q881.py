"""
 * 给定数组 people 。people[i]表示第 i 个人的体重 ，船的数量不限，每艘船可以承载的最大重量为 limit。
 * 每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。
 * 返回 承载所有人所需的最小船数 。
 * 提示：
 * 1、1 <= people.length <= 5 * 10^4
 * 2、1 <= people[i] <= limit <= 3 * 10^4
 * 链接：https://leetcode.cn/problems/boats-to-save-people/
"""
from typing import List


class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        light, heavy = 0, len(people) - 1
        while light <= heavy:
            if people[light] + people[heavy] > limit:
                heavy -= 1
            else:
                light += 1
                heavy -= 1
            ans += 1
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().numRescueBoats([1, 2], limit=3))
    # 3
    print(Solution().numRescueBoats([3, 2, 2, 1], limit=3))
    # 4
    print(Solution().numRescueBoats([3, 5, 3, 4], limit=5))
