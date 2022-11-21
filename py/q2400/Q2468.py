"""
 * 给你一个字符串 message 和一个正整数 limit 。
 * 你需要根据 limit 将 message 分割 成一个或多个 部分 。
 * 每个部分的结尾都是 "<a/b>" ，其中 "b" 用分割出来的总数 替换， "a" 用当前部分所在的编号 替换 ，编号从 1 到 b 依次编号。
 * 除此以外，除了最后一部分长度 小于等于 limit 以外，其他每一部分（包括结尾部分）的长度都应该 等于 limit 。
 * 你需要确保分割后的结果数组，删掉每部分的结尾并 按顺序 连起来后，能够得到 message 。同时，结果数组越短越好。
 * 请你返回 message  分割后得到的结果数组。如果无法按要求分割 message ，返回一个空数组。
 * 提示：
 * 1、1 <= message.length <= 10^4
 * 2、message 只包含小写英文字母和 ' ' 。
 * 3、1 <= limit <= 10^4
 * 链接：https://leetcode.cn/problems/split-message-based-on-limit/
"""
from typing import List


class Solution:

    def splitMessage(self, message: str, limit: int) -> List[str]:

        n = len(message)
        i = cap = 0
        while True:
            i += 1
            if i < 10:
                tail_len = 5
            elif i < 100:
                if i == 10: cap -= 9
                tail_len = 7
            elif i < 1000:
                if i == 100: cap -= 99
                tail_len = 9
            else:
                if i == 1000: cap -= 999
                tail_len = 11
            if limit - tail_len <= 0: return []
            cap += limit - tail_len
            if cap < n: continue

            ans = []
            k = 0
            for j in range(1, i + 1):
                tail = f"<{j}/{i}>"
                if j < i:
                    m = limit - len(tail)
                    ans.append(message[k:k + m] + tail)
                    k += m
                else:
                    ans.append(message[k:] + tail)
            return ans


if __name__ == '__main__':
    # ["thi<1/14>","s i<2/14>","s r<3/14>","eal<4/14>","ly <5/14>","a v<6/14>","ery<7/14>"," aw<8/14>","eso<9/14>","me<10/14>"," m<11/14>","es<12/14>","sa<13/14>","ge<14/14>"]
    print(Solution().splitMessage("this is really a very awesome message", 9))
    # ["short mess<1/2>","age<2/2>"]
    print(Solution().splitMessage("short message", 15))
