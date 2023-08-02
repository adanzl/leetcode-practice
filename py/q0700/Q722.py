"""
 * 给一个 C++ 程序，删除程序中的注释。这个程序source是一个数组，其中source[i]表示第 i 行源码。 这表示每行源码由 '\n' 分隔。
 * 在 C++ 中有两种注释风格，行内注释和块注释。
 * 1、字符串// 表示行注释，表示//和其右侧的其余字符应该被忽略。
 * 2、字符串/* 表示一个块注释，它表示直到下一个（非重叠）出现的*/之间的所有字符都应该被忽略。（阅读顺序为从左到右）非重叠是指，字符串/*/并没有结束块注释，因为注释的结尾与开头相重叠。
 * 第一个有效注释优先于其他注释。
 * 1、如果字符串//出现在块注释中会被忽略。
 * 2、同样，如果字符串/*出现在行或块注释中也会被忽略。
 * 如果一行在删除注释之后变为空字符串，那么不要输出该行。即，答案列表中的每个字符串都是非空的。
 * 样例中没有控制字符，单引号或双引号字符。
 * 比如，source = "string s = "/* Not a comment. */";" 不会出现在测试样例里。
 *   此外，没有其他内容（如定义或宏）会干扰注释。
 * 我们保证每一个块注释最终都会被闭合， 所以在行或块注释之外的/*总是开始新的注释。
 * 最后，隐式换行符可以通过块注释删除。 有关详细信息，请参阅下面的示例。
 * 从源代码中删除注释后，需要以相同的格式返回源代码。
 * 提示:
 * 1、1 <= source.length <= 100
 * 2、0 <= source[i].length <= 80
 * 3、source[i] 由可打印的 ASCII 字符组成。
 * 4、每个块注释都会被闭合。
 * 5、给定的源码中不会有单引号、双引号或其他控制字符。
 * 链接：https://leetcode.cn/problems/remove-comments/
"""
import re
from typing import List


class Solution:

    def removeComments1(self, source: List[str]) -> List[str]:
        s = re.sub('//.*|/\*(\s|.)*?\*/', '', '\n'.join(source))
        return list(filter(len, s.split('\n')))

    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        block = False
        for line in source:
            concat = False
            if block:
                end = line.find('*/')
                if end == -1:
                    continue
                else:
                    block = False
                    line = line[end + 2:]
                    if len(line) == 0:
                        continue
                    # ans[-1] += line
                    concat = True
            c_idx = line.find('//')
            cb_idx = line.find('/*')
            if (c_idx < cb_idx or cb_idx == -1) and c_idx != -1:
                line = line[:c_idx]
                cb_idx = -1
            while cb_idx != -1:
                end = line.find('*/', cb_idx + 2)
                if end == -1:
                    block = True
                    line = line[:cb_idx]
                    break
                else:
                    line = line[:cb_idx] + line[end + 2:]
                    cb_idx = line.find('/*')
                    c_idx = line.find('//')
                    if (c_idx < cb_idx or cb_idx == -1) and c_idx != -1:
                        line = line[:c_idx]
                        cb_idx = -1
            if len(line) != 0:
                if concat:
                    ans[-1] += line
                else:
                    ans.append(line)
        return ans


if __name__ == '__main__':
    # ["ae*"]
    print(Solution().removeComments(["a/*/b//*c", "blank", "d/*/e*//f"]))
    # ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
    print(Solution().removeComments(
        ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
    # ["a","blank","d/f"]
    print(Solution().removeComments(["a//*b//*c", "blank", "d/*/e*//f"]))
    # ["ab"]
    print(Solution().removeComments(["a/*comment", "line", "more_comment*/b"]))