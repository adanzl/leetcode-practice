"""
 * 给你一个长度为 n 的数组 happiness ，以及一个 正整数 k 。
 * n 个孩子站成一队，其中第 i 个孩子的 幸福值 是 happiness[i] 。
 * 你计划组织 k 轮筛选从这 n 个孩子中选出 k 个孩子。
 * 在每一轮选择一个孩子时，所有 尚未 被选中的孩子的 幸福值 将减少 1 。
 * 注意，幸福值 不能 变成负数，且只有在它是正数的情况下才会减少。
 * 选择 k 个孩子，并使你选中的孩子幸福值之和最大，返回你能够得到的 最大值 。
 * 提示：
 * 1、1 <= n == happiness.length <= 2 * 10^5
 * 2、1 <= happiness[i] <= 10^8
 * 3、1 <= k <= n
 * 链接：https://leetcode.cn/problems/maximize-happiness-of-selected-children/
"""
from typing import List


class Solution:

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
        sub = 0
        for i, num in enumerate(sorted(happiness, reverse=True)):
            if i >= k or num - sub <= 0:
                break
            ans += num - sub
            sub += 1
        return ans


if __name__ == '__main__':
    # 53
    print(Solution().maximumHappinessSum([12, 1, 42], 3))
    # 4
    print(Solution().maximumHappinessSum([1, 2, 3], k=2))
    # 1
    print(Solution().maximumHappinessSum([1, 1, 1, 1], k=2))
    # 5
    print(Solution().maximumHappinessSum([2, 3, 4, 5], k=1))
