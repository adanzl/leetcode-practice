"""
 * 链接：https://www.acwing.com/problem/content/description/4712/
"""

from bisect import bisect_left


# 树状数组 下标从 1 开始，二维求和
class BIT:

    def __init__(self, n):
        self.tree = [[0, 0]] * (n + 1)

    def add(self, i, val):
        while i < len(self.tree):
            self.tree[i] = [self.tree[i][0] + val[0], self.tree[i][1] + val[1]]
            i += i & -i  # low_bit

    def query(self, i):
        res = [0, 0]
        while i > 0:
            res = [res[0] + self.tree[i][0], res[1] + self.tree[i][1]]
            i &= i - 1
        return res


n = int(input())
nums = list(map(int, input().split()))
# n = 4  # 4
# nums = list(map(int, "10 8 3 1".split()))
# n = 3  # 1
# nums = list(map(int, "3 2 1".split()))
# n = 4  # 1
# nums = list(map(int, "1 5 4 3".split()))
ans = 0
st = sorted(nums)
arr = [bisect_left(st, num) for num in nums]  # 离散化
tree = BIT(n + 1)

for num in arr:
    v1, v2 = tree.query(n), tree.query(num + 1)
    tree.add(num + 1, [1, v2[0] - v1[0]])
    ans += v2[1] - v1[1]

print(ans)