"""
 * 你想要用小写字母组成一个目标字符串 target。 
 * 开始的时候，序列由 target.length 个 '?' 记号组成。而你有一个小写字母印章 stamp。
 * 在每个回合，你可以将印章放在序列上，并将序列中的每个字母替换为印章上的相应字母。你最多可以进行 10 * target.length  个回合。
 * 举个例子，如果初始序列为 "?????"，而你的印章 stamp 是 "abc"，那么在第一回合，你可以得到 "abc??"、"?abc?"、"??abc"。
 * （请注意，印章必须完全包含在序列的边界内才能盖下去。）
 * 如果可以印出序列，那么返回一个数组，该数组由每个回合中被印下的最左边字母的索引组成。如果不能印出序列，就返回一个空数组。
 * 例如，如果序列是 "ababc"，印章是 "abc"，那么我们就可以返回与操作 "?????" -> "abc??" -> "ababc" 相对应的答案 [0, 2];
 * 另外，如果可以印出序列，那么需要保证可以在 10 * target.length 个回合内完成。任何超过此数字的答案将不被接受。
 * 提示：
 * 1、1 <= stamp.length <= target.length <= 1000
 * 2、stamp 和 target 只包含小写字母。
 * 链接：https://leetcode.cn/problems/stamping-the-sequence/
"""

from typing import List

#
# @lc app=leetcode.cn id=936 lang=python3
#
# [936] 戳印序列
#


# @lc code=start
class Solution:

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        # 逆向思考，从target转成'???'，每次选择一个可以的字符串进行转换，拓扑排序思路
        n, n_s = len(target), len(stamp)
        cnt = 0
        tar = list(target)

        def match(idx):
            ret, c = 0, 0
            for i in range(n_s):
                if idx + i >= n: break
                if tar[idx + i] != '?': c += 1
                if tar[idx + i] != '?' and tar[idx + i] != stamp[i]: break
                ret += 1
            return ret == n_s and c

        q = [i for i in range(n - n_s + 1) if match(i)]
        ans = []
        while q:
            for v in q:
                ans.append(v)
                for i in range(n_s):
                    if tar[v + i] != '?':
                        cnt += 1
                    tar[v + i] = '?'
            q = [i for i in range(n - n_s + 1) if match(i)]

        return ans[::-1] if cnt == n else []


# @lc code=end

if __name__ == '__main__':
    # [7, 12, 10, 6, 2, 13, 9, 5, 3, 0]
    print(Solution().movesToStamp("aq", "aqaaqaqqqaqqaaq"))
    # [3,0,1]
    print(Solution().movesToStamp("abca", target="aabcaca"))
    # [0,2]
    print(Solution().movesToStamp("abc", target="ababc"))