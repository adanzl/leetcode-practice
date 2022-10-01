"""
 * 为了缓解「力扣嘉年华」期间的人流压力，组委会在活动期间开设了一些交通专线。path[i] = [a, b] 表示有一条从地点 a通往地点 b 的 单向 交通专线。
 * 若存在一个地点，满足以下要求，我们则称之为 交通枢纽：
 * 1、所有地点（除自身外）均有一条 单向 专线 直接 通往该地点；
 * 2、该地点不存在任何 通往其他地点 的单向专线。
 * 请返回交通专线的 交通枢纽。若不存在，则返回 -1。
 * 注意：对于任意一个地点，至少被一条专线连通。
 * 提示：
 * 1、1 <= path.length <= 1000
 * 2、0 <= path[i][0], path[i][1] <= 1000
 * path[i][0] 与 path[i][1] 不相等
 * 链接：https://leetcode.cn/problems/D9PW8w/
 * 链接：https://leetcode.cn/contest/season/2022-fall/problems/D9PW8w/
"""
from collections import defaultdict
from typing import *


class Solution:

    def transportationHub(self, path: List[List[int]]) -> int:
        p_dic = defaultdict(set)
        fr, p = set(), set()
        for f, t in path:
            p_dic[t].add(f)
            fr.add(f)
            p.add(t)
            p.add(f)
        for k, v in p_dic.items():
            if len(v) == len(p) - 1 and k not in fr:
                return k
        return -1


if __name__ == '__main__':
    # 3
    print(Solution().transportationHub([[0, 1], [0, 3], [1, 3], [2, 0], [2, 3]]))
    # -1
    print(Solution().transportationHub([[0, 3], [1, 0], [1, 3], [2, 0], [3, 0], [3, 2]]))
