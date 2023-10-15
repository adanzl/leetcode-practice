"""
 * 给你一个下标从 0 开始的字符串数组 words ，其中 words[i] 要么是一个字符串形式的正整数，要么是字符串 "prev" 。
 * 我们从数组的开头开始遍历，对于 words 中的每个 "prev" 字符串，找到 words 中的 上一个遍历的整数 ，定义如下：
 * 1、k 表示到当前位置为止的连续 "prev" 字符串数目（包含当前字符串），令下标从 0 开始的 整数 数组 nums 表示目前为止遍历过的所有整数，
 *     同时用 nums_reverse 表示 nums 反转得到的数组，那么当前 "prev" 对应的 上一个遍历的整数 是 nums_reverse 数组中下标为 (k - 1) 的整数。
 * 2、如果 k 比目前为止遍历过的整数数目 更多 ，那么上一个遍历的整数为 -1 。
 * 请你返回一个整数数组，包含所有上一个遍历的整数。
 * 提示：
 * 1、1 <= words.length <= 100
 * 2、words[i] == "prev" 或 1 <= int(words[i]) <= 100 
 * 链接：https://leetcode.cn/problems/last-visited-integers/
"""
from typing import List
#
# @lc app=leetcode.cn id=2899 lang=python3
#

# @lc code=start

class Solution:

    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        cnt = 0
        s = []
        ans = []
        for w in words:
            if w == 'prev':
                cnt += 1
                if cnt > len(s):
                    ans.append(-1)
                else:
                    ans.append(s[-cnt])
            else:
                cnt = 0
                s.append(int(w))
        return ans

# @lc code=end

if __name__ == '__main__':
    # [2,1,-1]
    print(Solution().lastVisitedIntegers(["1", "2", "prev", "prev", "prev"]))
    # [1,2,1]
    print(Solution().lastVisitedIntegers(["1", "prev", "2", "prev", "prev"]))
