
class Solution:

    def __init__(self, n, capacities):
        self.w = [0] * (n+1)
        self.parent = list(range(n + 1))
        self.next = list(range(1, n + 2))
        self.capacities = capacities
        pass

    def add_water(self, idx, water):
        while idx < len(self.w):
            remain = self.capacities[idx - 1] - self.w[idx]
            if remain >= water:
                self.w[idx] += water
                return
            else:
                water -= remain
                self.w[idx] += remain
                self.merge(idx - 1, idx)
                idx = self.next[self.find(idx)]
        return

    def query(self, idx):
        return self.w[idx]

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, v1, v2):
        r1, r2 = self.find(v1), self.find(v2)
        if r1 == r2:
            return
        self.parent[r2] = r1
        self.next[r1] = self.next[r2]


if __name__ == '__main__':
    # obj = Solution(2, [5, 10])
    # obj.add_water(1, 4)
    # print(obj.query(1))  # 4
    # obj.add_water(2, 5)
    # obj.add_water(1, 4)
    # print(obj.query(1))  # 5
    # print(obj.query(2))  # 8

    # obj = Solution(3, [5, 10, 8])
    # obj.add_water(1, 12)
    # print(obj.query(2))  # 7
    # obj.add_water(1, 6)
    # obj.add_water(3, 2)
    # print(obj.query(2))  # 10
    # print(obj.query(3))  # 5
    n = int(input())
    obj = Solution(n, [int(n) for n in input("").split()])
    q = int(input())
    for _ in range(q):
        query = [int(n) for n in input("").split()]
        if query[0] == 1:
            obj.add_water(query[1], query[2])
        else:
            print(obj.query(query[1]))
