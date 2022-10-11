"""
 * 给你一个字符串 s 和一个机器人，机器人当前有一个空字符串 t 。执行以下操作之一，直到 s 和 t 都变成空字符串：
 * 1、删除字符串 s 的 第一个 字符，并将该字符给机器人。机器人把这个字符添加到 t 的尾部。
 * 2、删除字符串 t 的 最后一个 字符，并将该字符给机器人。机器人将该字符写到纸上。
 * 请你返回纸上能写出的字典序最小的字符串。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/using-a-robot-to-print-the-lexicographically-smallest-string/
"""


class Solution:

    def robotWithString(self, s: str) -> str:
        n = len(s)
        t = []
        ans = []
        min_idx = [n - 1] * n
        for i in range(n - 2, -1, -1):
            min_idx[i] = i if s[i] <= s[min_idx[i + 1]] else min_idx[i + 1]
        i = 0
        while i < n:
            l = len(t)
            for j in range(l - 1, -1, -1):
                if t[j] <= s[min_idx[i]]:
                    ans += t[j]
                    del t[j]
                else:
                    break
            t += s[i:min_idx[i]]
            ans.append(s[min_idx[i]])
            i = min_idx[i] + 1
        ans += t[::-1]
        return "".join(ans)


if __name__ == '__main__':
    # "fnohopzv"
    print(Solution().robotWithString("vzhofnpo"))
    # "abc"
    print(Solution().robotWithString("bac"))
    # "addb"
    print(Solution().robotWithString("bdda"))
    # "azz"
    print(Solution().robotWithString("zza"))