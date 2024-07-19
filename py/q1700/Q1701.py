"""
 * 有一个餐厅，只有一位厨师。你有一个顾客数组 customers ，
 * 其中 customers[i] = [arrival_i, time_i] ：
 * 1、arrival_i 是第 i 位顾客到达的时间，到达时间按 非递减 顺序排列。
 * 2、time_i 是给第 i 位顾客做菜需要的时间。
 * 当一位顾客到达时，他将他的订单给厨师，厨师一旦空闲的时候就开始做这位顾客的菜。
 * 每位顾客会一直等待到厨师完成他的订单。厨师同时只能做一个人的订单。厨师会严格按照 订单给他的顺序 做菜。
 * 请你返回所有顾客需要等待的 平均 时间。与标准答案误差在 10^-5 范围以内，都视为正确结果。
 * 提示：
 * 1、1 <= customers.length <= 10^5
 * 2、1 <= arrival_i, time_i <= 10^4
 * 3、arrival_i <= arrival_(i+1)
 * 链接：https://leetcode.cn/problems/average-waiting-time
"""

from typing import List

#
# @lc app=leetcode.cn id=1701 lang=python3
#
# [1701] 平均等待时间
#


# @lc code=start
class Solution:

    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        ans, lst = 0, 1
        for a, t in customers:
            lst = max(lst, a) + t
            ans += lst - a
        return ans / n


# @lc code=end

if __name__ == '__main__':
    # 5.000
    print(Solution().averageWaitingTime([[1, 2], [2, 5], [4, 3]]))
    # 3.250
    print(Solution().averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]))
