"""
 * 数组 arr 中 大于 前面和后面相邻元素的元素被称为 峰值 元素。
 * 给你一个整数数组 nums 和一个二维整数数组 queries 。
 * 你需要处理以下两种类型的操作：
 * 1、queries[i] = [1, l_i, r_i] ，求出子数组 nums[l_i..r_i] 中 峰值 元素的数目。
 * 2、queries[i] = [2, index_i, val_i] ，将 nums[index_i] 变为 val_i 。
 * 请你返回一个数组 answer ，它依次包含每一个第一种操作的答案。
 * 注意：子数组中 第一个 和 最后一个 元素都 不是 峰值元素。
 * 提示：
 * 1、3 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 3、1 <= queries.length <= 10^5
 * 4、queries[i][0] == 1 或者 queries[i][0] == 2
 * 5、对于所有的 i ，都有：
 * 6、queries[i][0] == 1 ：0 <= queries[i][1] <= queries[i][2] <= nums.length - 1
 * 7、queries[i][0] == 2 ：0 <= queries[i][1] <= nums.length - 1, 1 <= queries[i][2] <= 10^5
 * 链接：https://leetcode.cn/problems/peaks-in-array/description/
"""
from typing import List


# 树状数组 下标从 1 开始，求和
class BIT:

    def __init__(self, n):
        self.tree = [0] * n

    def add(self, i, val):
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i  # low_bit

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res


class Solution:

    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        n = len(nums)
        arr = [0] * n
        t = BIT(n + 1)
        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                t.add(i + 1, 1)
                arr[i] = 1
        for a, v0, v1 in queries:
            if a == 1:
                ans.append((t.query(v1) - t.query(v0 + 1)) if v0 != v1 else 0)
            else:
                if 0 < v0 - 1 < n - 1:  # left
                    nv = int(nums[v0 - 2] < nums[v0 - 1] and nums[v0 - 1] > v1)
                    if nv != arr[v0 - 1]:
                        t.add(v0, 1 if nv else -1)
                    arr[v0 - 1] = nv
                if 0 < v0 + 1 < n - 1:  # right
                    nv = int(v1 < nums[v0 + 1] and nums[v0 + 1] > nums[v0 + 2])
                    if nv != arr[v0 + 1]:
                        t.add(v0 + 2, 1 if nv else -1)
                    arr[v0 + 1] = nv
                if 0 < v0 < n - 1:
                    nv = int(nums[v0 - 1] < v1 and v1 > nums[v0 + 1])
                    if nv != arr[v0]:
                        t.add(v0 + 1, 1 if nv else -1)
                    arr[v0] = nv
                nums[v0] = v1
        return ans


if __name__ == '__main__':
    # [0,0]
    print(Solution().countOfPeaks([5, 4, 8, 6], [[1, 2, 2], [1, 2, 3], [2, 1, 6]]))
    # [0,1]
    print(Solution().countOfPeaks([4, 1, 4, 2, 1, 5], queries=[[2, 2, 4], [1, 0, 2], [1, 0, 4]]))
    # [0]
    print(Solution().countOfPeaks([3, 1, 4, 2, 5], queries=[[2, 3, 4], [1, 0, 4]]))
