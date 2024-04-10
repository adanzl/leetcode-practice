"""
 * 给你一个二进制字符串 binary ，它仅有 0 或者 1 组成。你可以使用下面的操作任意次对它进行修改：
 * 1、操作 1 ：如果二进制串包含子字符串 "00" ，你可以用 "10" 将其替换。
 *     比方说， "00010" -> "10010"
 * 2、操作 2 ：如果二进制串包含子字符串 "10" ，你可以用 "01" 将其替换。
 *     比方说， "00010" -> "00001"
 * 请你返回执行上述操作任意次以后能得到的 最大二进制字符串 。如果二进制字符串 x 对应的十进制数字大于二进制字符串 y 对应的十进制数字，那么我们称二进制字符串 x 大于二进制字符串 y 。
 * 提示：
 * 1、1 <= binary.length <= 10^5
 * 2、binary 仅包含 '0' 和 '1' 。
 * 链接：https://leetcode.cn/problems/maximum-binary-string-after-change
"""

from typing import Counter, List

#
# @lc app=leetcode.cn id=1702 lang=python3
#
# [1702] 修改后的最大二进制字符串
#


# @lc code=start
class Solution:

    def maximumBinaryString1(self, binary: str) -> str:
        n = len(binary)
        bb = list(binary)
        ans = []
        id_0 = []
        for i in range(n - 1, -1, -1):
            if binary[i] == '0':
                id_0.append(i)
        for i in range(n - 1):
            if len(id_0) == 0:
                ans.extend(['1'] * (n - i))
                return ''.join(ans)
            v = bb[i:i + 2]
            if v[0] == '0' and v[1] == '0':
                ans.append("1")
                id_0.pop()
            elif v[0] == '1' and v[1] == '0':
                ans.append("1")
            elif v[0] == '0' and v[1] == '1':
                if len(id_0) > 1:
                    id_0.pop()
                    ii = id_0.pop()
                    ans.append('1')
                    bb[ii] = '1'
                    bb[i + 1] = '0'
                    id_0.append(i + 1)
                else:
                    ans.append('0')
                    ans.extend(['1'] * (n - i - 1))
                    return ''.join(ans)
            else:  # '11'
                ans.append('1')
        if id_0:
            ans.append('0')
        else:
            ans.append('1')
        return ''.join(ans)

    def maximumBinaryString(self, binary: str) -> str:

        # if no '0' in binary: return binary
        left0, zeros = binary.find('0'), binary.count('0')
        if zeros < 2: return binary
        ans = '1' * (left0 + zeros - 1) + '0'
        return ans.ljust(len(binary), '1')


# @lc code=end

if __name__ == '__main__':
    # '0'
    print(Solution().maximumBinaryString('0'))
    # '10'
    print(Solution().maximumBinaryString('10'))
    # "111011"
    print(Solution().maximumBinaryString("000110"))
    # "01"
    print(Solution().maximumBinaryString("01"))
