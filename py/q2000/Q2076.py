"""
 * 给你一个整数 n ，表示网络上的用户数目。每个用户按从 0 到 n - 1 进行编号。
 * 给你一个下标从 0 开始的二维整数数组 restrictions ，其中 restrictions[i] = [xi, yi] 意味着用户 xi 和用户 yi 不能 成为 朋友 ，
 * 不管是 直接 还是通过其他用户 间接 。
 * 最初，用户里没有人是其他用户的朋友。给你一个下标从 0 开始的二维整数数组 requests 表示好友请求的列表，
 * 其中 requests[j] = [uj, vj] 是用户 uj 和用户 vj 之间的一条好友请求。
 * 如果 uj 和 vj 可以成为 朋友 ，那么好友请求将会 成功 。
 * 每个好友请求都会按列表中给出的顺序进行处理（即，requests[j] 会在 requests[j + 1] 前）。
 * 一旦请求成功，那么对所有未来的好友请求而言， uj 和 vj 将会 成为直接朋友 。
 * 返回一个 布尔数组 result ，其中元素遵循此规则：如果第 j 个好友请求 成功 ，那么 result[j] 就是 true ；否则，为 false 。
 * 注意：如果 uj 和 vj 已经是直接朋友，那么他们之间的请求将仍然 成功 。
 * 提示：
 * 1、2 <= n <= 1000
 * 2、0 <= restrictions.length <= 1000
 * 3、restrictions[i].length == 2
 * 4、0 <= xi, yi <= n - 1
 * 5、xi != yi
 * 6、1 <= requests.length <= 1000
 * 7、requests[j].length == 2
 * 8、0 <= uj, vj <= n - 1
 * 9、uj != vj
 * 链接：https://leetcode.com/problems/process-restricted-friend-requests/
"""

from typing import List

#
# @lc app=leetcode.cn id=2076 lang=python3
#
# [2076] 处理含限制条件的好友请求
#


# @lc code=start
class Solution:

    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        fa = [i for i in range(n)]

        def find(x):
            if fa[x] == x: return x
            fa[x] = find(fa[x])
            return fa[x]

        ans = []
        for a, b in requests:
            r0, r1 = find(a), find(b)
            if r0 == r1:
                ans.append(True)
                continue
            if r0 > r1: r0, r1 = r1, r0
            valid = True
            for re0, re1 in restrictions:
                r_0, r_1 = find(re0), find(re1)
                if r_0 > r_1: r_0, r_1 = r_1, r_0
                if r_0 == r0 and r_1 == r1:
                    valid = False
                    break
            ans.append(valid)
            if valid:
                fa[r1] = r0
        return ans


# @lc code=end

if __name__ == '__main__':
    # [true,false]
    print(Solution().friendRequests(3, restrictions=[[0, 1]], requests=[[0, 2], [2, 1]]))
    # [true,false]
    print(Solution().friendRequests(3, restrictions=[[0, 1]], requests=[[1, 2], [0, 2]]))
    # [true,false,true,false]
    print(Solution().friendRequests(5, restrictions=[[0, 1], [1, 2], [2, 3]], requests=[[0, 4], [1, 2], [3, 1], [3, 4]]))
