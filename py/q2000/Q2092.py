"""
 * 给你一个整数 n ，表示有 n 个专家从 0 到 n - 1 编号。另外给你一个下标从 0 开始的二维整数数组 meetings ，
 * 其中 meetings[i] = [x_i, y_i, time_i] 表示专家 xi 和专家 yi 在时间 time_i 要开一场会。
 * 一个专家可以同时参加 多场会议 。最后，给你一个整数 firstPerson 。
 * 专家 0 有一个 秘密 ，最初，他在时间 0 将这个秘密分享给了专家 firstPerson 。
 * 接着，这个秘密会在每次有知晓这个秘密的专家参加会议时进行传播。
 * 更正式的表达是，每次会议，如果专家 xi 在时间 time_i 时知晓这个秘密，那么他将会与专家 yi 分享这个秘密，反之亦然。
 * 秘密共享是 瞬时发生 的。也就是说，在同一时间，一个专家不光可以接收到秘密，还能在其他会议上与其他专家分享。
 * 在所有会议都结束之后，返回所有知晓这个秘密的专家列表。你可以按 任何顺序 返回答案。
 * 提示：
 * 1、2 <= n <= 10^5
 * 2、1 <= meetings.length <= 10^5
 * 3、meetings[i].length == 3
 * 4、0 <= x_i, y_i <= n - 1
 * 5、x_i != y_i
 * 6、1 <= time_i <= 10^5
 * 7、1 <= firstPerson <= n - 1
 * 链接：https://leetcode.cn/problems/find-all-people-with-secret
"""
from collections import defaultdict
from typing import List


class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        fa = defaultdict(lambda: -1)

        def find(parent, x):
            if parent[x] == x or parent[x] == -1: return x
            parent[x] = find(parent, parent[x])
            return parent[x]

        fa[firstPerson] = 0
        mm = defaultdict(list)
        for x, y, t in meetings:
            mm[t].append([x, y])
        for t in sorted(mm.keys()):
            ff = defaultdict(lambda: -1)
            for x, y in mm[t]:
                r0, r1 = find(fa, x), find(fa, y)
                lr0, lr1 = find(ff, x), find(ff, y)
                if lr0:
                    ff[lr0] = lr1
                else:
                    ff[lr1] = lr0
                if r0 == 0 or r1 == 0:
                    ff[lr0] = ff[lr1] = 0
            for v in list(ff.keys()):
                if find(fa, v) == 0 or find(ff, v) == 0:
                    fa[find(fa, v)] = 0
        return [i for i in range(n) if find(fa, i) == 0]


if __name__ == '__main__':
    # [0,1,2,3,4]
    print(Solution().findAllPeople(5, meetings=[[3, 4, 2], [1, 2, 1], [2, 3, 1]], firstPerson=1))
    # [0,1,3,4]
    print(Solution().findAllPeople(5, [[1, 4, 3], [0, 4, 3]], 3))
    # [0,1,2,3,5]
    print(Solution().findAllPeople(6, meetings=[[1, 2, 5], [2, 3, 8], [1, 5, 10]], firstPerson=1))
    # [0,1,3]
    print(Solution().findAllPeople(4, meetings=[[3, 1, 3], [1, 2, 2], [0, 3, 3]], firstPerson=3))
