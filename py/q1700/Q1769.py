"""
 * 有 n 个盒子。给你一个长度为 n 的二进制字符串 boxes ，其中 boxes[i] 的值为 '0' 表示第 i 个盒子是 空 的，而 boxes[i] 的值为 '1' 表示盒子里有 一个 小球。
 * 在一步操作中，你可以将 一个 小球从某个盒子移动到一个与之相邻的盒子中。第 i 个盒子和第 j 个盒子相邻需满足 abs(i - j) == 1 。
 * 注意，操作执行后，某些盒子中可能会存在不止一个小球。
 * 返回一个长度为 n 的数组 answer ，其中 answer[i] 是将所有小球移动到第 i 个盒子所需的 最小 操作数。
 * 每个 answer[i] 都需要根据盒子的 初始状态 进行计算。
 * 提示：
 * 1、n == boxes.length
 * 2、1 <= n <= 2000
 * 3、boxes[i] 为 '0' 或 '1'
 * 链接：https://leetcode.cn/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
"""
from typing import List


class Solution:

    def minOperations(self, boxes: str) -> List[int]:
        return [sum(abs(j - i) for j, c in enumerate(boxes) if c == '1') for i in range(len(boxes))]


if __name__ == '__main__':
    # [1,1,3]
    print(Solution().minOperations("110"))
    # [11,8,5,4,3,4]
    print(Solution().minOperations("001011"))