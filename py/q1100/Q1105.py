"""
 * 给定一个数组 books ，其中 books[i] = [thickness_i, height_i] 表示第 i 本书的厚度和高度。你也会得到一个整数 shelfWidth 。
 * 按顺序 将这些书摆放到总宽度为 shelfWidth 的书架上。
 * 先选几本书放在书架上（它们的厚度之和小于等于书架的宽度 shelfWidth ），然后再建一层书架。重复这个过程，直到把所有的书都放在书架上。
 * 需要注意的是，在上述过程的每个步骤中，摆放书的顺序与你整理好的顺序相同。
 * 例如，如果这里有 5 本书，那么可能的一种摆放情况是：第一和第二本书放在第一层书架上，第三本书放在第二层书架上，第四和第五本书放在最后一层书架上。
 * 每一层所摆放的书的最大高度就是这一层书架的层高，书架整体的高度为各层高之和。
 * 以这种方式布置书架，返回书架整体可能的最小高度。
 * 提示：
 * 1、1 <= books.length <= 1000
 * 2、1 <= thickness_i <= shelfWidth <= 1000
 * 3、1 <= height_i <= 1000
 * 链接：https://leetcode.cn/problems/filling-bookcase-shelves/
"""
from typing import List


class Solution:

    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):  # 遍历尝试以books[i]作为一行书架的开头
            w, h = books[i]  # width-height
            dp[i] = dp[i + 1] + h
            for j in range(i + 1, n):  # 扩展当前行，尝试将后面的书拿到当前行，计算移动书之后的最小值
                pw, ph = books[j]
                if w + pw <= shelfWidth:  # 当前行无法扩展时break
                    w += pw
                    h = max(h, ph)
                    dp[i] = min(dp[i], h + dp[j + 1])
                else:
                    break
        return dp[0]


if __name__ == '__main__':
    # 6
    print(Solution().minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4))
    # 4
    print(Solution().minHeightShelves([[1, 3], [2, 4], [3, 2]], 6))
