"""
 * 给你一棵 n 个节点的树，树的根节点为 0 ，n 个节点的编号为 0 到 n - 1 。
 * 这棵树用一个长度为 n 的数组 parent 表示，其中 parent[i] 是节点 i 的父节点。
 * 由于节点 0 是根节点，所以 parent[0] == -1 。
 * 给你一个长度为 n 的字符串 s ，其中 s[i] 是节点 i 对应的字符。
 * 一开始你有一个空字符串 dfsStr ，定义一个递归函数 dfs(int x) ，它的输入是节点 x ，并依次执行以下操作：
 * 1、按照 节点编号升序 遍历 x 的所有孩子节点 y ，并调用 dfs(y) 。
 * 2、将 字符 s[x] 添加到字符串 dfsStr 的末尾。
 * 注意，所有递归函数 dfs 都共享全局变量 dfsStr 。
 * 你需要求出一个长度为 n 的布尔数组 answer ，对于 0 到 n - 1 的每一个下标 i ，你需要执行以下操作：
 * 1、清空字符串 dfsStr 并调用 dfs(i) 。
 * 2、如果结果字符串 dfsStr 是一个 回文串 ，answer[i] 为 true ，否则 answer[i] 为 false 。
 * 请你返回字符串 answer 。
 * 回文串 指的是一个字符串从前往后与从后往前是一模一样的。
 * 提示：
 * 1、n == parent.length == s.length
 * 2、1 <= n <= 10^5
 * 3、对于所有 i >= 1 ，都有 0 <= parent[i] <= n - 1 。
 * 4、parent[0] == -1
 * 5、parent 表示一棵合法的树。
 * 6、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/check-if-dfs-strings-are-palindromes/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            # 由于 i 是递增的，所以 g[p] 必然是有序的，下面无需排序
            g[p].append(i)
        dfsStr = [''] * n
        # nodes[i] 表示子树 i 的后序遍历的开始时间戳和结束时间戳+1（左闭右开区间）
        nodes = [[0, 0] for _ in range(n)]
        time = 0

        def dfs(x: int) -> None:
            nonlocal time
            nodes[x][0] = time
            for y in g[x]:
                dfs(y)
            dfsStr[time] = s[x]  # 后序遍历
            time += 1
            nodes[x][1] = time

        dfs(0)

        # Manacher 马拉车算法，求任意位置的回文字符串长度
        def manacher(s):
            # 在字符串中插入特殊字符
            # t[i] 为#表示偶数回文，否则表示奇数回文，t的长度为2*n+3
            t = '#'.join(['^'] + s + ['$'])
            p = [0] * (len(t) - 2)  # 表示回文中心到边缘的长度，包括i字符
            # 用 P 的下标 i 减去 P[i]，再除以 2 ，就是原字符串的开头下标了
            p[1] = 1
            boxM = boxR = 0
            for i in range(2, len(p)):  # t[2] 为原字符串第一个字符
                hl = 1
                if i < boxR:
                    hl = min(p[boxM * 2 - i], boxR - i)
                while t[i - hl] == t[i + hl]:
                    hl += 1
                    boxM, boxR = i, i + hl
                p[i] = hl

            return p

        p = manacher(dfsStr)
        is_palindrome = lambda l, r: p[l + r + 1] > r - l
        return [is_palindrome(l, r) for l, r in nodes]


if __name__ == '__main__':
    # [true,true,false,true,true,true]
    print(Solution().findAnswer([-1, 0, 0, 1, 1, 2], s="aababa"))
    # [true,true,true,true,true]
    print(Solution().findAnswer([-1, 0, 0, 0, 0], s="aabcb"))
    #
    # print(Solution().findAnswer())
