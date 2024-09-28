"""
 * 给你一个字符串数组 message 和一个字符串数组 bannedWords。
 * 如果数组中 至少 存在两个单词与 bannedWords 中的任一单词 完全相同，则该数组被视为 垃圾信息。
 * 如果数组 message 是垃圾信息，则返回 true；否则返回 false。
 * 提示：
 * 1、1 <= message.length, bannedWords.length <= 10^5
 * 2、1 <= message[i].length, bannedWords[i].length <= 15
 * 3、message[i] 和 bannedWords[i] 都只由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/report-spam-message/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        ans = 0
        cnt = set(bannedWords)
        for m in message:
            ans += int(m in cnt)
        return ans >= 2


if __name__ == '__main__':
    # True
    print(Solution().reportSpam(["hello", "world", "leetcode"], bannedWords=["world", "hello"]))
    # False
    print(Solution().reportSpam(["hello", "programming", "fun"], bannedWords=["world", "programming", "leetcode"]))
    # False
    print(Solution().reportSpam(["s", "a", "aj", "ps", "h", "ou", "e", "i", "x"],
                                ["j", "a", "b", "fa", "z", "a", "no", "ih", "nq"]))
