"""
 * 给你一个字符串 target、一个字符串数组 words 以及一个整数数组 costs，这两个数组长度相同。
 * 设想一个空字符串 s。
 * 你可以执行以下操作任意次数（包括零次）：
 * 1、选择一个在范围  [0, words.length - 1] 的索引 i。
 * 2、将 words[i] 追加到 s。
 * 3、该操作的成本是 costs[i]。
 * 返回使 s 等于 target 的 最小 成本。如果不可能，返回 -1。
 * 提示：
 * 1、1 <= target.length <= 5 * 10^4
 * 2、1 <= words.length == costs.length <= 5 * 10^4
 * 3、1 <= words[i].length <= target.length
 * 4、所有 words[i].length 的总和小于或等于 5 * 10^4
 * 5、target 和 words[i] 仅由小写英文字母组成。
 * 6、1 <= costs[i] <= 10^4
 * 链接：https://leetcode.cn/problems/construct-string-with-minimum-cost/
"""

from collections import defaultdict
from typing import List

#
# @lc app=leetcode.cn id=3213 lang=python3
#
#

# @lc code=start


class Trie:

    def __init__(self):
        self.children = {}
        self.c_end = 0  # 为单词结尾个数
        self.string = ''  # 单词
        self.fail = None  # 失配位置
        self.last = None  # 后缀链接（suffix link），用来快速跳到一定是某个 words[k] 的最后一个字母的节点（等于 root 则表示没有）

    def insert(self, s: str):
        node = self
        for c in s:
            if c not in node.children:
                node.children[c] = Trie()
                node.children[c].last = self
            node = node.children[c]
        node.c_end += 1
        node.string = s

    def query(self, s) -> bool:
        node = self
        for c in s:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.c_end != 0

    def build_failed(self):
        root = self
        queue = [root]  # root所在层为第0层
        while queue:  # 广度优先遍历
            node = queue.pop(0)
            # 将其孩子逐个加入列队
            for i, child in node.children.items():
                if node == root:
                    child.fail = root  # 第1层的节点的fail总是指向root
                else:
                    p = node.fail  # 第2层以下的节点, 其fail是在另一个分支上
                    while p:
                        # 遍历它的孩子，看它们有没与当前孩子相同字符的节点
                        if i in p.children:
                            child.fail = p.children[i]
                            # 沿着 last 往上走，可以直接跳到一定是某个 words[k] 的最后一个字母的节点（如果跳到 root 表示没有匹配）
                            child.last = child.fail if child.fail.c_end else child.fail.last
                            break
                        p = p.fail
                    if not p:
                        child.fail = root
                        child.last = root
                queue.append(child)

    def match(self, text):
        root, p = self, self
        ret, unique = [], set()
        for i, c in enumerate(text):
            while p != root and c not in p.children:  # type: ignore
                p = p.fail  #  失配指针发挥作用 # type: ignore
            # 如果没有匹配的，从 root 开始重新匹配
            p = p.children[c] if c in p.children else root  # type: ignore
            node: Trie = p
            while node != root:
                #  收集出可以匹配的模式串
                if node.c_end:
                    pos = i - len(node.string) + 1
                    # console.log(`匹配模式串 ${node.pattern}其起始位置在${pos}`)
                    if not node.string in unique:
                        unique.add(node.string)
                        ret.append(node.string)
                node = node.fail  # type: ignore
        return ret


class Solution:

    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        # AC 自动机
        n = len(target)
        LIMIT = 0x3c3c3c3c3c3c3c
        dp = [0] + [LIMIT] * n
        t = Trie()
        cost_dic = defaultdict(lambda: LIMIT)
        for w, c in zip(words, costs):
            t.insert(w)
            cost_dic[w] = min(cost_dic[w], c)
        t.build_failed()
        # print(t.match(target))
        cur = t
        for i, c in enumerate(target):
            while cur != t and c not in cur.children:  # type: ignore
                cur = cur.fail  #  失配指针发挥作用 # type: ignore
            # 如果没有匹配的，从 root 开始重新匹配
            cur = cur.children[c] if c in cur.children else t  # type: ignore
            node: Trie = cur
            while node != t:
                #  收集出可以匹配的模式串
                if node.c_end:
                    dp[i + 1] = min(dp[i + 1], cost_dic[node.string] + dp[i + 1 - len(node.string)])
                node = node.last  # type: ignore

        return dp[-1] if dp[-1] != LIMIT else -1


# @lc code=end

if __name__ == '__main__':
    # 7
    print(Solution().minimumCost("abcdef", ["abdef", "abc", "d", "def", "ef"], [100, 1, 1, 10, 5]))
    # -1
    print(Solution().minimumCost("aaaa", ["z", "zz", "zzz"], [1, 10, 100]))
