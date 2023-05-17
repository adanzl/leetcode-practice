"""
 * 给出基数为 -2 的两个数 arr1 和 arr2，返回两数相加的结果。
 * 数字以 数组形式 给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。
 * 例如，arr = [1,1,0,1] 表示数字 (-2)^3 + (-2)^2 + (-2)^0 = -3。
 * 数组形式 中的数字 arr 也同样不含前导零：即 arr == [0] 或 arr[0] == 1。
 * 返回相同表示形式的 arr1 和 arr2 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。
 * 提示：
 * 1、1 <= arr1.length, arr2.length <= 1000
 * 2、arr1[i] 和 arr2[i] 都是 0 或 1
 * 3、arr1 和 arr2 都没有前导 0
 * 链接：https://leetcode.cn/problems/adding-two-negabinary-numbers/
"""
from typing import List


class Solution:

    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = max(len(arr1), len(arr2))
        arr = [0] * n
        a = 0
        for i in range(n):
            v = -a
            if i < len(arr1):
                v += arr1[-i - 1]
            if i < len(arr2):
                v += arr2[-i - 1]
            if v >= 0:
                a, r = divmod(v, 2)
            else:
                a = -1
                r = 1
            arr[n - 1 - i] = r
        ans = arr if a == 0 else [1, 1] + arr
        idx = 0
        for idx in range(len(ans)):
            if ans[idx] != 0:
                break
        return ans[idx:]


if __name__ == '__main__':
    # [1,1,1,1,0]
    print(Solution().addNegabinary([1, 0, 1], arr2=[1, 0, 1]))
    # [1,0,0,0,0]
    print(Solution().addNegabinary([1, 1, 1, 1, 1], arr2=[1, 0, 1]))
    # [0]
    print(Solution().addNegabinary([0], arr2=[0]))
    # [1]
    print(Solution().addNegabinary([0], arr2=[1]))
