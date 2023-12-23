"""
 * 给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，
 * 其中 paths[i] = [cityA_i, cityB_i] 表示该线路将会从 cityA_i 直接前往 cityB_i 。
 * 请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。
 * 题目数据保证线路图会形成一条不存在循环的线路，因此恰有一个旅行终点站。
 * 提示：
 * 1、1 <= paths.length <= 100
 * 2、paths[i].length == 2
 * 3、1 <= cityA_i.length, cityB_i.length <= 10
 * 4、cityA_i != cityB_i
 * 5、所有字符串均由大小写英文字母和空格字符组成。
 * 链接：https://leetcode.cn/problems/destination-city
"""

from collections import Counter
from typing import List

#
# @lc app=leetcode.cn id=1436 lang=python3
#
# [1436] 旅行终点站
#


# @lc code=start
class Solution:

    def destCity(self, paths: List[List[str]]) -> str:
        cnt = Counter()
        for f, t in paths:
            cnt[f] += 1
            cnt[t] += 0
        return cnt.most_common()[-1][0]


# @lc code=end

if __name__ == '__main__':
    # "Sao Paulo"
    print(Solution().destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
    # "A"
    print(Solution().destCity([["B", "C"], ["D", "B"], ["C", "A"]]))
    # "Z"
    print(Solution().destCity([["A", "Z"]]))
