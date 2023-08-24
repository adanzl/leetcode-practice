"""
 * 你的笔记本键盘存在故障，每当你在上面输入字符 'i' 时，它会反转你所写的字符串。而输入其他字符则可以正常工作。
 * 给你一个下标从 0 开始的字符串 s ，请你用故障键盘依次输入每个字符。
 * 返回最终笔记本屏幕上输出的字符串。
 * 提示：
 * 1、1 <= s.length <= 100
 * 2、s 由小写英文字母组成
 * 3、s[0] != 'i'
 * 链接：https://leetcode.cn/problems/faulty-keyboard/
"""


class Solution:

    def finalString(self, s: str) -> str:
        ans = []
        for c in s:
            if c == 'i':
                ans.reverse()
            else:
                ans.append(c)
        return ''.join(ans)


if __name__ == '__main__':
    # 'rtsng'
    print(Solution().finalString("string"))
    # 'ponter'
    print(Solution().finalString("poiinter"))