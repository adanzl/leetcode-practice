"""
 * 给你两个 二维 整数数组 nums1 和 nums2.
 * 1、nums1[i] = [id_i, val_i] 表示编号为 idi 的数字对应的值等于 val_i 。
 * 2、nums2[i] = [id_i, val_i] 表示编号为 idi 的数字对应的值等于 val_i 。
 * 每个数组都包含 互不相同 的 id ，并按 id 以 递增 顺序排列。
 * 请你将两个数组合并为一个按 id 以递增顺序排列的数组，并符合下述条件：
 * 1、只有在两个数组中至少出现过一次的 id 才能包含在结果数组内。
 * 2、每个 id 在结果数组中 只能出现一次 ，并且其对应的值等于两个数组中该 id 所对应的值求和。如果某个数组中不存在该 id ，则认为其对应的值等于 0 。
 * 返回结果数组。返回的数组需要按 id 以递增顺序排列。
 * 提示：
 * 1、1 <= nums1.length, nums2.length <= 200
 * 2、nums1[i].length == nums2[j].length == 2
 * 3、1 <= id_i, val_i <= 1000
 * 4、数组中的 id 互不相同
 * 5、数据均按 id 以严格递增顺序排列
 * 链接：https://leetcode.cn/problems/merge-two-2d-arrays-by-summing-values/
"""
from collections import Counter
from typing import List


class Solution:

    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        return sorted([[k, v] for k, v in (Counter(dict((k, v) for k, v in nums1)) + Counter(dict((k, v) for k, v in nums2))).items()])


if __name__ == '__main__':
    # [[1,6],[2,3],[3,2],[4,6]]
    print(Solution().mergeArrays([[1, 2], [2, 3], [4, 5]], nums2=[[1, 4], [3, 2], [4, 1]]))
    # [[1,3],[2,4],[3,6],[4,3],[5,5]]
    print(Solution().mergeArrays([[2, 4], [3, 6], [5, 5]], nums2=[[1, 3], [4, 3]]))
