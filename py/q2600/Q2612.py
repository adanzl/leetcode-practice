"""
 * 给你一个整数 n 和一个在范围 [0, n - 1] 以内的整数 p ，它们表示一个长度为 n 且下标从 0 开始的数组 arr ，数组中除了下标为 p 处是 1 以外，其他所有数都是 0 。
 * 同时给你一个整数数组 banned ，它包含数组中的一些位置。banned 中第 i 个位置表示 arr[banned[i]] = 0 ，题目保证 banned[i] != p 。
 * 你可以对 arr 进行 若干次 操作。一次操作中，你选择大小为 k 的一个 子数组 ，并将它 翻转 。
 * 在任何一次翻转操作后，你都需要确保 arr 中唯一的 1 不会到达任何 banned 中的位置。换句话说，arr[banned[i]] 始终 保持 0 。
 * 请你返回一个数组 ans ，对于 [0, n - 1] 之间的任意下标 i ，ans[i] 是将 1 放到位置 i 处的 最少 翻转操作次数，如果无法放到位置 i 处，此数为 -1 。
 * 1、子数组 指的是一个数组里一段连续 非空 的元素序列。
 * 2、对于所有的 i ，ans[i] 相互之间独立计算。
 * 3、将一个数组中的元素 翻转 指的是将数组中的值变成 相反顺序 。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、0 <= p <= n - 1
 * 3、0 <= banned.length <= n - 1
 * 4、0 <= banned[i] <= n - 1
 * 5、1 <= k <= n 
 * 6、banned[i] != p
 * 7、banned 中的值 互不相同 。
 * 链接：https://leetcode.cn/problems/minimum-reverse-operations/
"""
from typing import Deque, List

from sortedcontainers import SortedList


class Solution:

    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        ans = [-1] * n
        if k == 1:
            # 处理特殊情况 k = 1
            ans[p] = 0
            return ans

        ban = set(banned)
        st = [SortedList() for _ in range(2)]
        for i in range(n):
            if i != p and i not in ban:
                st[i % 2].add(i)
        # bfs
        q = Deque()
        q.append(p)
        ans[p] = 0
        while q:
            now = q.popleft()
            # 计算可以跳的范围
            L = max(-(k - 1), k - 1 - now * 2)
            R = min(k - 1, -(k - 1) + (n - now - 1) * 2)
            # 寻找第一个大于等于 now + L 的位置，并开始枚举后面连续的位置
            x = (now + (k - 1)) % 2
            idx = st[x].bisect_left(now + L)  # type: ignore
            while idx != len(st[x]):
                # 遇到了第一个大于 now + R 的位置，结束枚举
                if st[x][idx] > now + R:
                    break
                # 这个位置还没被跳过，但是可以从 now 一步跳过来
                # 更新答案，并从 set<int> 里去掉
                ans[st[x][idx]] = ans[now] + 1  # type: ignore
                q.append(st[x][idx])
                st[x].remove(st[x][idx])  # type: ignore
        return ans


if __name__ == '__main__':
    # [0,-1,-1,1]
    print(Solution().minReverseOperations(4, p=0, banned=[1, 2], k=4))
    # [0,-1,-1,-1,-1]
    print(Solution().minReverseOperations(5, p=0, banned=[2, 4], k=3))
    # [-1,-1,0,-1]
    print(Solution().minReverseOperations(4, p=2, banned=[0, 1, 3], k=1))
