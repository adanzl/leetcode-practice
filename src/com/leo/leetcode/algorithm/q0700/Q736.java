package com.leo.leetcode.algorithm.q0700;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

/**
 * 给你一个类似 Lisp 语句的字符串表达式 expression，求出其计算结果。
 * 表达式语法如下所示:
 * 1、表达式可以为整数，let 表达式，add 表达式，mult 表达式，或赋值的变量。表达式的结果总是一个整数。(整数可以是正整数、负整数、0)
 * 2、let 表达式采用 "(let v1 e1 v2 e2 ... vn en expr)" 的形式，其中 let 总是以字符串 "let"来表示，接下来会跟随一对或多对交替的变量和表达式，也就是说，第一个变量 v1被分配为表达式 e1 的值，第二个变量 v2 被分配为表达式 e2 的值，依次类推；最终 let 表达式的值为 expr表达式的值。
 * 3、add 表达式表示为 "(add e1 e2)" ，其中 add 总是以字符串 "add" 来表示，该表达式总是包含两个表达式 e1、e2 ，最终结果是 e1 表达式的值与 e2 表达式的值之 和 。
 * 4、mult 表达式表示为 "(mult e1 e2)" ，其中 mult 总是以字符串 "mult" 表示，该表达式总是包含两个表达式 e1、e2，最终结果是 e1 表达式的值与 e2 表达式的值之 积 。
 * 5、在该题目中，变量名以小写字符开始，之后跟随 0 个或多个小写字符或数字。为了方便，"add" ，"let" ，"mult" 会被定义为 "关键字" ，不会用作变量名。
 * 6、最后，要说一下作用域的概念。计算变量名所对应的表达式时，在计算上下文中，首先检查最内层作用域（按括号计），然后按顺序依次检查外部作用域。测试用例中每一个表达式都是合法的。有关作用域的更多详细信息，请参阅示例。
 * 提示：
 * 1、1 <= expression.length <= 2000
 * 2、expression 中不含前导和尾随空格
 * 3、expression 中的不同部分（token）之间用单个空格进行分隔
 * 4、答案和所有中间计算结果都符合 32-bit 整数范围
 * 5、测试用例中的表达式均为合法的且最终结果为整数
 * 链接：https://leetcode.cn/problems/parse-lisp-expression
 */
public class Q736 {

    public static void main(String[] args) {
        // -12
        System.out.println(new Q736().evaluate("(let x 7 -12)"));
        // 14
        System.out.println(new Q736().evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))"));
        // 2
        System.out.println(new Q736().evaluate("(let x 3 x 2 x)"));
        // 5
        System.out.println(new Q736().evaluate("(let x 1 y 2 x (add x y) (add x y))"));
    }

    public int evaluate(String expression) {
        Stack<Integer> values = new Stack<>();
        eval(expression, 0, new Stack<>(), values);
        return values.pop();
    }

    int eval(String expression, int idx, Stack<Map<String, Integer>> symbols, Stack<Integer> values) {
        if (idx >= expression.length()) return idx;
        if (expression.charAt(idx) == '(') idx++;
        char fChar = expression.charAt(idx);
        int end = getSectionEnd(expression, idx);
        String symbol = expression.substring(idx, end);
        if (Character.isDigit(fChar) || fChar == '-') {
            values.push(Integer.parseInt(symbol));
            return end;
        }
        Map<String, Integer> cSymbol = new HashMap<>();
        symbols.push(cSymbol);
        idx = end;
        switch (symbol) {
            case "add":
                idx = eval(expression, idx + 1, symbols, values);
                idx = eval(expression, idx + 1, symbols, values);
                values.push(values.pop() + values.pop());
                break;
            case "mult":
                idx = eval(expression, idx + 1, symbols, values);
                idx = eval(expression, idx + 1, symbols, values);
                values.push(values.pop() * values.pop());
                break;
            case "let":
                int iS = 0;
                String s = "";
                for (int i = idx; i < expression.length(); ) {
                    if (iS % 2 == 0) {
                        // variable
                        if (expression.charAt(idx + 1) == '(') {
                            idx = eval(expression, idx + 1, symbols, values);
                            break;
                        }
                        int e = getSectionEnd(expression, idx);
                        s = expression.substring(idx + 1, e);
                        idx = e;
                        if (expression.charAt(e) == ')') {
                            char cFirst = s.charAt(0);
                            if (Character.isDigit(cFirst) || cFirst == '-') values.push(Integer.parseInt(s));
                            else values.push(findSymbol(symbols, s).get(s));
                            break;
                        }
                    } else {
                        // value
                        idx = eval(expression, idx + 1, symbols, values);
                        cSymbol.put(s, values.pop());
                    }
                    iS++;
                }
                break;
            default:
                // exp
                values.push(findSymbol(symbols, symbol).get(symbol));
                break;
        }
        symbols.pop();
        if (idx < expression.length() && expression.charAt(idx) == ')') idx++;
        return idx;
    }

    Map<String, Integer> findSymbol(Stack<Map<String, Integer>> symbols, String key) {
        for (int i = symbols.size() - 1; i >= 0; i--) {
            if (symbols.get(i).containsKey(key)) return symbols.get(i);
        }
        return null;
    }

    int getSectionEnd(String str, int idx) {
        int iSpace = str.indexOf(' ', idx + 1);
        int rBracket = str.indexOf(')', idx + 1);
        if (iSpace < 0) iSpace = Integer.MAX_VALUE;
        if (rBracket < 0) rBracket = Integer.MAX_VALUE;
        return Math.min(iSpace, rBracket);
    }

}
