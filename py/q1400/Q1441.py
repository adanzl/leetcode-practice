"""
 * 给你一个数组 target 和一个整数 n。每次迭代，需要从  list = { 1 , 2 , 3 ..., n } 中依次读取一个数字。
 * 请使用下述操作来构建目标数组 target ：
 * 1、"Push"：从 list 中读取一个新元素， 并将其推入数组中。
 * 2、"Pop"：删除数组中的最后一个元素。
 * 3、如果目标数组构建完成，就停止读取更多元素。
 * 题目数据保证目标数组严格递增，并且只包含 1 到 n 之间的数字。
 * 请返回构建目标数组所用的操作序列。如果存在多个可行方案，返回任一即可。
 * 提示：
 * 1、1 <= target.length <= 100
 * 2、1 <= n <= 100
 * 3、1 <= target[i] <= n
 * 4、target 严格递增
 * 链接：https://leetcode.cn/problems/build-an-array-with-stack-operations/
"""
from typing import List


class Solution:

    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        num = 1
        for t in target:
            while True:
                ans.append("Push")
                if num == t: break
                ans.append("Pop")
                num += 1
            num += 1
        return ans


if __name__ == '__main__':
    # ["Push","Push","Pop","Push"]
    print(Solution().buildArray([1, 3], 3))
    # ["Push","Push","Push"]
    print(Solution().buildArray([1, 2, 3], 3))
    # ["Push","Push"]
    print(Solution().buildArray([1, 2], 4))
