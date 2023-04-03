"""
 * 有两只老鼠和 n 块不同类型的奶酪，每块奶酪都只能被其中一只老鼠吃掉。
 * 下标为 i 处的奶酪被吃掉的得分为：
 * 1、如果第一只老鼠吃掉，则得分为 reward1[i] 。
 * 2、如果第二只老鼠吃掉，则得分为 reward2[i] 。
 * 给你一个正整数数组 reward1 ，一个正整数数组 reward2 ，和一个非负整数 k 。
 * 请你返回第一只老鼠恰好吃掉 k 块奶酪的情况下，最大 得分为多少。
 * 提示：
 * 1、1 <= n == reward1.length == reward2.length <= 10^5
 * 2、1 <= reward1[i], reward2[i] <= 1000
 * 3、0 <= k <= n
 * 链接：https://leetcode.cn/problems/mice-and-cheese/
"""
from typing import List


class Solution:

    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        ans = 0
        arr = sorted([[v1 - v2, i] for i, (v1, v2) in enumerate(zip(reward1, reward2))], reverse=True)
        ids = set([i for _, i in arr[:k]])
        for i, (v1, v2) in enumerate(zip(reward1, reward2)):
            if i in ids:
                ans += v1
            else:
                ans += v2
        return ans


if __name__ == '__main__':
    # 15
    print(Solution().miceAndCheese([1, 1, 3, 4], reward2=[4, 4, 1, 1], k=2))
    # 2
    print(Solution().miceAndCheese([1, 1], reward2=[1, 1], k=2))
