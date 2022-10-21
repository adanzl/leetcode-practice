"""
 * 给定一个单词列表 words 和一个整数 k ，返回前 k 个出现次数最多的单词。
 * 返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， 按字典顺序 排序。
 * 注意：
 * 1、1 <= words.length <= 500
 * 2、1 <= words[i] <= 10
 * 3、words[i] 由小写英文字母组成。
 * 4、k 的取值范围是 [1, 不同 words[i] 的数量]
 * 链接：https://leetcode.cn/problems/top-k-frequent-words/
"""
from typing import Counter, List


class Solution:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [i[0] for i in sorted([(k, v) for k, v in Counter(words).items()], key=lambda x: (-x[1], x[0]))][:k]


if __name__ == '__main__':
    # ["i", "love"]
    print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
    # ["the", "is", "sunny", "day"]
    print(Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
