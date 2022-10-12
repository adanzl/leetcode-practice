"""
 * 给你一个长度为 n 的 整数 数组 pref 。找出并返回满足下述条件且长度为 n 的数组 arr ：
 * pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
 * 注意 ^ 表示 按位异或（bitwise-xor）运算。
 * 可以证明答案是 唯一 的。
 * 提示：
 * 1、1 <= pref.length <= 10^5
 * 2、0 <= pref[i] <= 10^6
 * 链接：https://leetcode.cn/problems/find-the-original-array-of-prefix-xor/
"""
from typing import List


class Solution:

    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        for i in range(1, len(pref)):
            ans.append(pref[i - 1] ^ pref[i])
        return ans


if __name__ == '__main__':
    # [5,7,2,3,2]
    print(Solution().findArray([5, 2, 0, 3, 1]))
    # [13]
    print(Solution().findArray([13]))
