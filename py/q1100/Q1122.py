"""
 * 给你两个数组，arr1 和 arr2，arr2 中的元素各不相同，arr2 中的每个元素都出现在 arr1 中。
 * 对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。
 * 未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
 * 提示：
 * 1、1 <= arr1.length, arr2.length <= 1000
 * 2、0 <= arr1[i], arr2[i] <= 1000
 * 3、arr2 中的元素 arr2[i]  各不相同 
 * 4、arr2 中的每个元素 arr2[i] 都出现在 arr1 中
 * 链接：https://leetcode.com/problems/relative-sort-array
"""

#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#


# @lc code=start
class Solution(object):

    def relativeSortArray(self, arr1, arr2):
        return sorted(arr1, key=lambda x: arr2.index(x) if x in arr2 else 1001 + x)


# @lc code=end

if __name__ == '__main__':
    # [2,2,2,1,4,3,3,9,6,7,19]
    print(Solution().relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]))
    # [22,28,8,6,17,44]
    print(Solution().relativeSortArray([28, 6, 22, 8, 44, 17], arr2=[22, 28, 8, 6]))
