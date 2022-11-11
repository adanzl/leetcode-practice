"""
 * 给你一个以字符串形式表述的 布尔表达式（boolean） expression，返回该式的运算结果。
 * 有效的表达式需遵循以下约定：
 * 1、"t"，运算结果为 True
 * 2、"f"，运算结果为 False
 * 3、"!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT）
 * 4、"&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND）
 * 5、"|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR）
 * 提示：
 * 1、1 <= expression.length <= 20000
 * 2、expression[i] 由 {'(', ')', '&', '|', '!', 't', 'f', ','} 中的字符组成。
 * 3、expression 是以上述形式给出的有效表达式，表示一个布尔值。
 * 链接：https://leetcode.cn/problems/parsing-a-boolean-expression/
"""


class Solution:

    def parseBoolExpr1(self, expression: str) -> bool:

        def f(idx):
            e = expression[idx]
            if e == 't': return True, idx + 1
            if e == 'f': return False, idx + 1
            vals = []
            idx = idx + 1  # (
            while True:
                v, idx = f(idx + 1)
                vals.append(v)
                if expression[idx] == ')':
                    break
            ret = vals[0]
            if e == '!': ret = not ret
            for i in range(1, len(vals)):
                if e == '|': ret |= vals[i]
                elif e == '&': ret &= vals[i]
            return ret, idx + 1

        return f(0)[0]

    def parseBoolExpr(self, expression):

        def my_or(*xs):
            return any(xs)

        def my_and(*xs):
            return all(xs)

        e = expression.replace('t', '1')
        e = e.replace('f', '0')
        e = e.replace('|', 'my_or')
        e = e.replace('&', 'my_and')
        e = e.replace('!', 'not ')
        return bool(eval(e))


if __name__ == '__main__':
    # True
    print(Solution().parseBoolExpr("!(f)"))
    # False
    print(Solution().parseBoolExpr("|(&(t,f,t),!(t))"))
    # True
    print(Solution().parseBoolExpr("|(f,t)"))
    # False
    print(Solution().parseBoolExpr("&(t,f)"))