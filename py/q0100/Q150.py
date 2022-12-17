"""
 * 根据 逆波兰表示法，求表达式的值。
 * 有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
 * 注意 两个整数之间的除法只保留整数部分。
 * 可以保证给定的逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
 * 提示：
 * 1、1 <= tokens.length <= 10^4
 * 2、tokens[i] 是一个算符（"+"、"-"、"*" 或 "/"），或是在范围 [-200, 200] 内的一个整数
 * 逆波兰表达式：
 * 逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。
 * 1、平常使用的算式则是一种中缀表达式，如 ( 1 + 2 ) * ( 3 + 4 ) 。
 * 2、该算式的逆波兰表达式写法为 ( ( 1 2 + ) ( 3 4 + ) * ) 。
 * 逆波兰表达式主要有以下两个优点：
 * 1、去掉括号后表达式无歧义，上式即便写成 1 2 + 3 4 + * 也可以依据次序计算出正确结果。
 * 2、适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中
 * 链接：https://leetcode.cn/problems/evaluate-reverse-polish-notation/
"""
from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                v1, v2 = s.pop(), s.pop()
                if t == '+': s.append(v1 + v2)
                elif t == '*': s.append(v1 * v2)
                elif t == '-': s.append(v2 - v1)
                else: s.append(int(v2 / v1))
            else:
                s.append(int(t))
        return s[-1]


if __name__ == '__main__':
    # 9
    print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
    # 6
    print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
    # 22
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
