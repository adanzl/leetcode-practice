"""
 * PyPy 3-64
 * 链接：https://codeforces.com/contest/962/problem/C
"""

square = []
for i in range(1, 10**5):
    if i * i > 2 * 10**9:
        break
    square.append(i * i)


class Solution:

    def func(self, num):
        ans = 10
        sn = str(num)
        for q in square:
            sq = str(q)
            v = 0
            i_sq, i_n = 0, 0
            while i_sq < len(sq) and i_n < len(sn):
                if sq[i_sq] == sn[i_n]:
                    i_sq += 1
                else:
                    v += 1
                i_n += 1
            if len(sq) == i_sq:
                v += len(sn) - i_n
                ans = min(ans, v)
        return -1 if ans == 10 else ans


if __name__ == '__main__':

    # # -1
    # print(Solution().func(333))
    # # 2
    # print(Solution().func(8314))
    # # 0
    # print(Solution().func(625))

    num = input("")
    print(Solution().func(num))
