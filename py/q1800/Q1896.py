"""
 * 给你一个 有效的 布尔表达式，用字符串 expression 表示。这个字符串包含字符 '1'，'0'，'&'（按位 与 运算），'|'（按位 或 运算），'(' 和 ')' 。
 * 比方说，"()1|1" 和 "(1)&()" 不是有效 布尔表达式。而 "1"， "(((1))|(0))" 和 "1|(0&(1))" 是 有效 布尔表达式。
 * 你的目标是将布尔表达式的 值 反转 （也就是将 0 变为 1 ，或者将 1 变为 0），请你返回达成目标需要的 最少操作 次数。
 * 比方说，如果表达式 expression = "1|1|(0&0)&1" ，它的 值 为 1|1|(0&0)&1 = 1|1|0&1 = 1|0&1 = 1&1 = 1 。我们想要执行操作将 新的 表达式的值变成 0 。
 * 可执行的 操作 如下：
 * 1、将一个 '1' 变成一个 '0' 。
 * 2、将一个 '0' 变成一个 '1' 。
 * 3、将一个 '&' 变成一个 '|' 。
 * 4、将一个 '|' 变成一个 '&' 。
 * 注意：'&' 的 运算优先级 与 '|' 相同 。计算表达式时，括号优先级 最高 ，然后按照 从左到右 的顺序运算。
 * 提示：
 * 1、1 <= expression.length <= 10^5
 * 2、expression 只包含 '1'，'0'，'&'，'|'，'(' 和 ')'
 * 3、所有括号都有与之匹配的对应括号。
 * 4、不会有空的括号（也就是说 "()" 不是 expression 的子字符串）。
 * 链接：https://leetcode.cn/problems/minimum-cost-to-change-the-final-value-of-expression/
"""


class Node:

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minOperationsToFlip(self, expression: str) -> int:
        # 构建表达式的树状结构，进行树状DP
        def build_node(s, e):
            ret = Node(None)
            idx = s
            while idx < e + 1 and expression[idx] != ')':
                if expression[idx] == '(':
                    sub, idx = build_node(idx + 1, e)
                    if ret.left is None: ret.left = sub
                    else: ret.right = sub
                else:
                    if expression[idx] == '&' or expression[idx] == '|':
                        if ret.val is None: ret.val = expression[idx]
                        else: ret = Node(expression[idx], ret)
                    else:
                        sub = Node(expression[idx])
                        if ret.left is None: ret.left = sub
                        else: ret.right = sub
                    idx += 1
            return ret, idx + 1

        def dfs(node):  # [False Count, True Count]
            if node.val is None: return dfs(node.left)
            if node.val == '0': return [0, 1]
            if node.val == '1': return [1, 0]
            lv, rv = dfs(node.left), dfs(node.right)
            if node.val == '&':
                node.ans = [
                    min(lv[0] + rv[1], lv[1] + rv[0], lv[0] + rv[0]),
                    min(lv[1] + rv[1], lv[0] + rv[1] + 1, lv[1] + rv[0] + 1),
                ]
            else:
                node.ans = [
                    min(lv[0] + rv[1] + 1, lv[1] + rv[0] + 1, lv[0] + rv[0]),
                    min(lv[1] + rv[1], lv[0] + rv[1], lv[1] + rv[0]),
                ]
            return node.ans

        head, _ = build_node(0, len(expression) - 1)
        return max(dfs(head))


if __name__ == '__main__':
    # 1
    print(Solution().minOperationsToFlip("(0|(1|0&1))"))
    # 3
    print(Solution().minOperationsToFlip("(0&0)&(0&0&0)"))
    # 1
    print(Solution().minOperationsToFlip("1&(0|1)"))
