"""
 * 给你一个二进制字符串 s 和一个正整数 k 。
 * 如果 s 的某个子字符串中 1 的个数恰好等于 k ，则称这个子字符串是一个 美丽子字符串 。
 * 令 len 等于 最短 美丽子字符串的长度。
 * 返回长度等于 len 且字典序 最小 的美丽子字符串。如果 s 中不含美丽子字符串，则返回一个 空 字符串。
 * 对于相同长度的两个字符串 a 和 b ，如果在 a 和 b 出现不同的第一个位置上，
 * a 中该位置上的字符严格大于 b 中的对应字符，则认为字符串 a 字典序 大于 字符串 b 。
 * 例如，"abcd" 的字典序大于 "abcc" ，因为两个字符串出现不同的第一个位置对应第四个字符，而 d 大于 c 。
 * 提示：
 * 1、1 <= s.length <= 100
 * 2、1 <= k <= s.length
 * 链接：https://leetcode.cn/problems/shortest-and-lexicographically-smallest-beautiful-string/
"""


class Solution:

    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ''
        ln = 10**10
        ids = []
        cnt = 0
        for i, c in enumerate(s):
            if c == '1':
                cnt += 1
                ids.append(i)
                if cnt >= k:
                    idx = ids[cnt - k]
                    ss = s[idx:i + 1]
                    if ln > len(ss) or (ln == len(ss) and ans > ss):
                        ans = ss
                        ln = len(ans)
        return ans


if __name__ == '__main__':
    # "11"
    print(Solution().shortestBeautifulSubstring("11", k=2))
    # "11001"
    print(Solution().shortestBeautifulSubstring("100011001", k=3))
    # "11"
    print(Solution().shortestBeautifulSubstring("1011", k=2))
    # ""
    print(Solution().shortestBeautifulSubstring("000", k=1))
