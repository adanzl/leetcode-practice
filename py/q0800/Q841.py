"""
 * 有 n 个房间，房间按从 0 到 n - 1 编号。最初，除 0 号房间外的其余所有房间都被锁住。你的目标是进入所有的房间。然而，你不能在没有获得钥匙的时候进入锁住的房间。
 * 当你进入一个房间，你可能会在里面找到一套不同的钥匙，每把钥匙上都有对应的房间号，即表示钥匙可以打开的房间。你可以拿上所有钥匙去解锁其他房间。
 * 给你一个数组 rooms 其中 rooms[i] 是你进入 i 号房间可以获得的钥匙集合。如果能进入 所有 房间返回 true，否则返回 false。
 * 提示：
 * 1、n == rooms.length
 * 2、2 <= n <= 1000
 * 3、0 <= rooms[i].length <= 1000
 * 4、1 <= sum(rooms[i].length) <= 3000
 * 5、0 <= rooms[i][j] < n
 * 6、所有 rooms[i] 的值 互不相同
 * 链接：https://leetcode.cn/problems/keys-and-rooms/
"""
from typing import Deque, List


class Solution:

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = Deque([0])
        vis = set([0])
        while q:
            k = q.popleft()
            for nx in rooms[k]:
                if nx in vis: continue
                q.append(nx)
                vis.add(nx)
        return len(vis) == len(rooms)


if __name__ == '__main__':
    # True
    print(Solution().canVisitAllRooms([[1], [2], [3], []]))
    # False
    print(Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
