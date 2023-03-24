"""
 * 设计一个算法：接收一个字符流，并检查这些字符的后缀是否是字符串数组 words 中的一个字符串。
 * 例如，words = ["abc", "xyz"] 且字符流中逐个依次加入 4 个字符 'a'、'x'、'y' 和 'z' ，
 * 你所设计的算法应当可以检测到 "axyz" 的后缀 "xyz" 与 words 中的字符串 "xyz" 匹配。
 * 按下述要求实现 StreamChecker 类：
 * 1、StreamChecker(String[] words) ：构造函数，用字符串数组 words 初始化数据结构。
 * 2、boolean query(char letter)：从字符流中接收一个新字符，如果字符流中的任一非空后缀能匹配 words 中的某一字符串，返回 true ；否则，返回 false。
 * 提示：
 * 1、1 <= words.length <= 2000
 * 2、1 <= words[i].length <= 200
 * 3、words[i] 由小写英文字母组成
 * 4、letter 是一个小写英文字母
 * 5、最多调用查询 4 * 10^4 次
 * 链接：https://leetcode.cn/problems/stream-of-characters
"""
from typing import List


class StreamChecker:

    class TNode:

        def __init__(self, c):
            self.children = {}
            self.end = False
            self.c = c

    def __init__(self, words: List[str]):
        self.queries = set()
        self.tire = StreamChecker.TNode(None)
        for word in words:
            node = self.tire
            for c in word:
                if c not in node.children:
                    node.children[c] = StreamChecker.TNode(c)
                node = node.children[c]
            node.end = True

    def query(self, letter: str) -> bool:
        ans = False
        queries = self.queries
        self.queries = set()
        for q in queries:
            if letter in q.children:
                q = q.children[letter]
                if q.end:
                    ans = True
                self.queries.add(q)
        if letter in self.tire.children:
            q = self.tire.children[letter]
            if q.end:
                ans = True
            else:
                self.queries.add(q)
        return ans


if __name__ == '__main__':
    streamChecker = StreamChecker(["cd", "f", "kl"])
    print(streamChecker.query("a"))  # 返回 False
    print(streamChecker.query("b"))  # 返回 False
    print(streamChecker.query("c"))  # 返回 False
    print(streamChecker.query("d"))  # 返回 True ，因为 'cd' 在 words 中
    print(streamChecker.query("e"))  # 返回 False
    print(streamChecker.query("f"))  # 返回 True ，因为 'f' 在 words 中
    print(streamChecker.query("g"))  # 返回 False
    print(streamChecker.query("h"))  # 返回 False
    print(streamChecker.query("i"))  # 返回 False
    print(streamChecker.query("j"))  # 返回 False
    print(streamChecker.query("k"))  # 返回 False
    print(streamChecker.query("l"))  # 返回 True ，因为 'kl' 在 words 中
