"""
 * 给你一个字符串 s 和一个整数 k 。
 * k 子序列指的是 s 的一个长度为 k 的 子序列 ，且所有字符都是 唯一 的，也就是说每个字符在子序列里只出现过一次。
 * 定义 f(c) 为字符 c 在 s 中出现的次数。
 * k 子序列的 美丽值 定义为这个子序列中每一个字符 c 的 f(c) 之 和 。
 * 比方说，s = "abbbdd" 和 k = 2 ，我们有：
 * 1、f('a') = 1, f('b') = 3, f('d') = 2
 * 2、s 的部分 k 子序列为：
 * 2.1、"abbbdd" -> "ab" ，美丽值为 f('a') + f('b') = 4
 * 2.2、"abbbdd" -> "ad" ，美丽值为 f('a') + f('d') = 3
 * 2.3、"abbbdd" -> "bd" ，美丽值为 f('b') + f('d') = 5
 * 请你返回一个整数，表示所有 k 子序列 里面 美丽值 是 最大值 的子序列数目。由于答案可能很大，将结果对 109 + 7 取余后返回。
 * 一个字符串的子序列指的是从原字符串里面删除一些字符（也可能一个字符也不删除），不改变剩下字符顺序连接得到的新字符串。
 * 注意：
 * f(c) 指的是字符 c 在字符串 s 的出现次数，不是在 k 子序列里的出现次数。
 * 两个 k 子序列如果有任何一个字符在原字符串中的下标不同，则它们是两个不同的子序列。所以两个不同的 k 子序列可能产生相同的字符串。
 * 提示：
 * 1、1 <= s.length <= 2 * 10^5
 * 2、1 <= k <= s.length
 * 3、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/count-k-subsequences-of-a-string-with-maximum-beauty/
"""
from collections import Counter
from itertools import combinations


class Solution:

    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        cnt = Counter(s)
        ss = sorted([[v, c] for v, c in cnt.items()], key=lambda x: x[1], reverse=True)
        a = []
        lst = []
        for i, (v, c) in enumerate(ss):
            if i < k:
                a.append([v, c])
            elif a and a[-1][1] == c:
                lst.append([v, c])
            else:
                break
        while a and lst and a[-1][1] == lst[-1][1]:
            lst.append(a.pop())
        if len(lst) + len(a) < k:
            return 0
        ans = 1 if a else 0
        for v, c in a:
            ans *= c
        ct = k - len(a)
        if ct:
            s_lst = 0
            for cc in combinations(lst, ct):
                vv = 1
                for _, c in cc:
                    vv *= c
                s_lst += vv
            ans = max(ans, 1) * s_lst
        return ans % (10**9 + 7)


if __name__ == '__main__':
    # 2
    print(Solution().countKSubsequencesWithMaxBeauty("ci", 1))
    # 6
    print(Solution().countKSubsequencesWithMaxBeauty("kjojr", 3))
    # 0
    print(Solution().countKSubsequencesWithMaxBeauty("dd", 2))
    # 2
    print(Solution().countKSubsequencesWithMaxBeauty("abbcd", k=4))
    # 4
    print(Solution().countKSubsequencesWithMaxBeauty("bcca", k=2))
