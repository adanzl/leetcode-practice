"""
 * 给定一个放有字母和数字的数组，找到最长的子数组，且包含的字母和数字的个数相同。
 * 返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。
 * 提示：array.length <= 100000
 * 链接：https://leetcode.cn/problems/find-longest-subarray-lcci/
"""
from typing import List


class Solution:

    def findLongestSubarray(self, array: List[str]) -> List[str]:
        idx_dic = {0: -1}
        cnt = 0
        ans_len, ans_l = 0, -1
        for i, c in enumerate(array):
            if c.isdigit():
                cnt += 1
            else:
                cnt -= 1
            if cnt in idx_dic:
                if i - idx_dic[cnt] > ans_len:
                    ans_len = i - idx_dic[cnt]
                    ans_l = idx_dic[cnt] + 1
            else:
                idx_dic[cnt] = i
        return [] if ans_len == 0 else array[ans_l:ans_l + ans_len]


if __name__ == '__main__':
    # ["A","1"]
    print(Solution().findLongestSubarray(["A", "1"]))
    # ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
    print(Solution().findLongestSubarray(["A", "1", "B", "C", "D", "2", "3", "4", "E", "5", "F", "G", "6", "7", "H", "I", "J", "K", "L", "M"]))
    # []
    print(Solution().findLongestSubarray(["A", "A"]))
