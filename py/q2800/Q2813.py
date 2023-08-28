"""
 * 给你一个长度为 n 的二维整数数组 items 和一个整数 k 。
 * items[i] = [profit_i, category_i]，其中 profit_i 和 category_i 分别表示第 i 个项目的利润和类别。
 * 现定义 items 的 子序列 的 优雅度 可以用 total_profit + distinct_categories2 计算，
 * 其中 total_profit 是子序列中所有项目的利润总和，distinct_categories 是所选子序列所含的所有类别中不同类别的数量。
 * 你的任务是从 items 所有长度为 k 的子序列中，找出 最大优雅度 。
 * 用整数形式表示并返回 items 中所有长度恰好为 k 的子序列的最大优雅度。
 * 注意：数组的子序列是经由原数组删除一些元素（可能不删除）而产生的新数组，且删除不改变其余元素相对顺序。
 * 提示：
 * 1、1 <= items.length == n <= 10^5
 * 2、items[i].length == 2
 * 3、items[i][0] == profit_i
 * 4、items[i][1] == category_i
 * 5、1 <= profit_i <= 10^9
 * 6、1 <= category_i <= n
 * 7、1 <= k <= n
 * 链接：https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/
"""
from typing import List


class Solution:

    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        # 反悔贪心
        items.sort(key=lambda x: x[0], reverse=True)
        ans = total_profit = 0
        vis = set()
        duplicate = []  # 重复类别的利润
        for i, (profit, category) in enumerate(items):
            if i < k:
                total_profit += profit
                if category not in vis:
                    vis.add(category)
                else:  # 重复类别
                    duplicate.append(profit)
            elif duplicate and category not in vis:
                vis.add(category)
                total_profit += profit - duplicate.pop()  # 用最小利润替换
            # else: 比前面的利润小，而且类别还重复了，选它只会让 total_profit 变小，len(vis) 不变，优雅度不会变大
            ans = max(ans, total_profit + len(vis)**2)
        return ans


if __name__ == '__main__':
    # 17
    print(Solution().findMaximumElegance([[3, 2], [5, 1], [10, 1]], k=2))
    # 19
    print(Solution().findMaximumElegance([[3, 1], [3, 1], [2, 2], [5, 3]], k=3))
    # 7
    print(Solution().findMaximumElegance([[1, 1], [2, 1], [3, 1]], k=3))
