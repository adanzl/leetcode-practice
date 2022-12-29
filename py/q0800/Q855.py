"""
 * 在考场里，一排有 N 个座位，分别编号为 0, 1, 2, ..., N-1 。
 * 当学生进入考场后，他必须坐在能够使他与离他最近的人之间的距离达到最大化的座位上。如果有多个这样的座位，他会坐在编号最小的座位上。(另外，如果考场里没有人，那么学生就坐在 0 号座位上。)
 * 返回 ExamRoom(int N) 类，它有两个公开的函数：其中，函数 ExamRoom.seat() 会返回一个 int （整型数据），代表学生坐的位置；函数 ExamRoom.leave(int p) 代表坐在座位 p 上的学生现在离开了考场。
 * 每次调用 ExamRoom.leave(p) 时都保证有学生坐在座位 p 上。
 * 提示：
 * 1、1 <= N <= 10^9
 * 2、在所有的测试样例中 ExamRoom.seat() 和 ExamRoom.leave() 最多被调用 10^4 次。
 * 3、保证在调用 ExamRoom.leave(p) 时有学生正坐在座位 p 上。
 * 链接：https://leetcode.cn/problems/exam-room/
"""
from heapq import heappop, heappush


class ExamRoom:

    def __init__(self, n: int):
        self.g = {}  # idx-[l, r]
        self.g[-1] = [-1, n]
        self.g[n] = [-1, n]
        self.n = n
        self.h = []  # [-len, l, r]

    def seat(self) -> int:
        if len(self.g) == 2:
            self.g[0] = [-1, self.n]
            self.g[-1] = [-1, 0]
            self.g[self.n] = [0, self.n]
            return 0
        proc = lambda x: (x // 2) - 1
        l_item, r_item = self.g[self.g[-1][1]], self.g[self.g[self.n][0]]
        len_l, len_r = self.g[-1][1] - 1, self.n - 1 - self.g[self.n][0] - 1
        while self.h:
            ll, l, r = self.h[0]
            if l not in self.g or r not in self.g or self.g[l][1] != r or self.g[r][0] != l:
                heappop(self.h)
                continue
            if -ll > len_l and -ll >= len_r:
                heappop(self.h)
                mid = (l + r) // 2
                if mid - l > 1: heappush(self.h, [-proc(mid - l), l, mid])
                if r - mid > 1: heappush(self.h, [-proc(r - mid), mid, r])
                self.g[l][1] = mid
                self.g[mid] = [l, r]
                self.g[r][0] = mid
                return mid
            break
        if len_l >= len_r:
            if self.g[-1][1] > 1:
                heappush(self.h, [-proc(self.g[-1][1]), 0, self.g[-1][1]])
            self.g[0] = [-1, self.g[-1][1]]
            self.g[-1][1] = 0
            l_item[0] = 0
            return 0
        else:
            if self.n - 1 - self.g[self.n][0] > 1:
                heappush(self.h, [-proc(self.n - 1 - self.g[self.n][0]), self.g[self.n][0], self.n - 1])
            self.g[self.n - 1] = [self.g[self.n][0], self.n]
            self.g[self.n][0] = self.n - 1
            r_item[1] = self.n - 1
            return self.n - 1

    def leave(self, p: int) -> None:
        l, r = self.g[p]
        proc = lambda x: (x // 2) - 1
        self.g[l][1] = r
        self.g[r][0] = l
        if l != -1 and r != self.n:
            heappush(self.h, [-proc(r - l), l, r])
        del self.g[p]


if __name__ == '__main__':
    obj = ExamRoom(7)
    print(obj.seat())  # 0
    print(obj.seat())  # 6
    print(obj.seat())  # 3
    print(obj.seat())  # 1
    obj.leave(1)
    print(obj.seat())  # 1
    print(obj.seat())  # 2
    print(obj.seat())  # 4
    print(obj.seat())  # 5
    obj.leave(4)

    # obj = ExamRoom(7)
    # print(obj.seat())  # 0
    # print(obj.seat())  # 6
    # print(obj.seat())  # 3
    # print(obj.seat())  # 1
    # print(obj.seat())  # 2
    # print(obj.seat())  # 4
    # print(obj.seat())  # 5
    # obj.leave(3)
    # print(obj.seat())  # 3
    # obj.leave(2)

    # obj = ExamRoom(10)
    # print(obj.seat())  # 0
    # print(obj.seat())  # 9
    # print(obj.seat())  # 4
    # print(obj.seat())  # 2
    # obj.leave(4)
    # print(obj.seat())  # 5

    # obj = ExamRoom(10)
    # print(obj.seat())  # 0
    # print(obj.seat())  # 9
    # print(obj.seat())  # 4
    # obj.leave(0)
    # obj.leave(4)
    # print(obj.seat())  # 0
    # print(obj.seat())  # 4
    # print(obj.seat())  # 2
    # print(obj.seat())  # 6
    # print(obj.seat())  # 1
    # print(obj.seat())  # 3
    # print(obj.seat())  # 5
    # print(obj.seat())  # 7
    # print(obj.seat())  # 8
    # obj.leave(0)
    # obj.leave(4)
    # print(obj.seat())  # 0
    # print(obj.seat())  # 4
    # obj.leave(7)
    # print(obj.seat())  # 7
    # obj.leave(3)
    # print(obj.seat())  # 3
    # obj.leave(3)
    # print(obj.seat())  # 3
    # obj.leave(9)
    # print(obj.seat())  # 9
    # obj.leave(0)
    # obj.leave(8)
    # print(obj.seat())  # 0
    # print(obj.seat())  # 8
    # obj.leave(0)
    # obj.leave(8)
    # print(obj.seat())  # 0
    # print(obj.seat())  # 8
    # obj.leave(2)
