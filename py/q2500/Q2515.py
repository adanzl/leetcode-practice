"""
 * 给你一个下标从 0 开始的 环形 字符串数组 words 和一个字符串 target 。环形数组 意味着数组首尾相连。
 * 形式上， words[i] 的下一个元素是 words[(i + 1) % n] ，而 words[i] 的前一个元素是 words[(i - 1 + n) % n] ，其中 n 是 words 的长度。
 * 从 startIndex 开始，你一次可以用 1 步移动到下一个或者前一个单词。
 * 返回到达目标字符串 target 所需的最短距离。如果 words 中不存在字符串 target ，返回 -1 。
 * 提示：
 * 1、1 <= words.length <= 100
 * 2、1 <= words[i].length <= 100
 * 3、words[i] 和 target 仅由小写英文字母组成
 * 4、0 <= startIndex < words.length
 * 链接：https://leetcode.cn/problems/shortest-distance-to-target-string-in-a-circular-array/
"""
from typing import List


class Solution:

    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = n + 1
        for i in range(n):
            if words[(startIndex + i) % n] == target:
                ans = min(ans, i)
            if words[(startIndex - i + n) % n] == target:
                ans = min(ans, i)
        return ans if ans != n + 1 else -1


if __name__ == '__main__':
    # 1
    print(Solution().closetTarget(["hello", "i", "am", "leetcode", "hello"], "hello", 1))
    # 1
    print(Solution().closetTarget(["a", "b", "leetcode"], "leetcode", 0))
    # -1
    print(Solution().closetTarget(["i", "eat", "leetcode"], "ate", 0))
