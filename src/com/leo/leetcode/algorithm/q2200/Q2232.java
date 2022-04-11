package com.leo.leetcode.algorithm.q2200;

/**
 * 给你一个下标从 0 开始的字符串 expression ，格式为 "<num1>+<num2>" ，其中 <num1> 和 <num2> 表示正整数。
 * 请你向 expression 中添加一对括号，使得在添加之后， expression 仍然是一个有效的数学表达式，
 * 并且计算后可以得到 最小 可能值。左括号 必须 添加在 '+' 的左侧，而右括号必须添加在 '+' 的右侧。
 * 返回添加一对括号后形成的表达式 expression ，且满足 expression 计算得到 最小 可能值。如果存在多个答案都能产生相同结果，返回任意一个答案。
 * 生成的输入满足：expression 的原始值和添加满足要求的任一对括号之后 expression 的值，都符合 32-bit 带符号整数范围。
 * 提示：
 * 1、3 <= expression.length <= 10
 * 2、expression 仅由数字 '1' 到 '9' 和 '+' 组成
 * 3、expression 由数字开始和结束
 * 4、expression 恰好仅含有一个 '+'.
 * 5、expression 的原始值和添加满足要求的任一对括号之后 expression 的值，都符合 32-bit 带符号整数范围
 * 链接：https://leetcode-cn.com/problems/minimize-result-by-adding-parentheses-to-expression
 */
public class Q2232 {
    public static void main(String[] args) {
        // (12+3)0
        System.out.println(new Q2232().minimizeResult("12+30"));
        // 2(47+38)
        System.out.println(new Q2232().minimizeResult("247+38"));
        // 1(2+3)4
        System.out.println(new Q2232().minimizeResult("12+34"));
        // 1(2+39)
        System.out.println(new Q2232().minimizeResult("12+39"));
        // (999+999)
        System.out.println(new Q2232().minimizeResult("999+999"));
    }

    public String minimizeResult(String expression) {
        String[] exp = expression.split("\\+");
        String exp1 = exp[0], exp2 = exp[1];
        int min = Integer.parseInt(exp1) + Integer.parseInt(exp2);
        String ret = "(" + expression + ")";
        for (int i = 1; i < exp2.length(); i++) {
            String e3 = exp2.substring(0, i), e4 = exp2.substring(i);
            long value = (Long.parseLong(exp1) + Long.parseLong(e3))
                    * Long.parseLong(e4);
            if (value < min) {
                ret = "(" + exp1 + "+" + e3 + ")" + e4;
                min = (int) value;
            }
        }
        for (int i = 1; i < exp1.length(); i++) {
            for (int j = 1; j < exp2.length(); j++) {
                String e1 = exp1.substring(0, i), e2 = exp1.substring(i), e3 = exp2.substring(0, j), e4 = exp2.substring(j);
                long value = Long.parseLong(e1) *
                        (Long.parseLong(e2) + Long.parseLong(e3))
                        * Long.parseLong(e4);
                if (value < min) {
                    ret = e1 + "(" + e2 + "+" + e3 + ")" + e4;
                    min = (int) value;
                }
            }
        }
        for (int i = 1; i < exp1.length(); i++) {
            String e1 = exp1.substring(0, i), e2 = exp1.substring(i);
            long value = Long.parseLong(e1) * (Long.parseLong(e2) + Long.parseLong(exp2));
            if (value < min) {
                ret = e1 + "(" + e2 + "+" + exp2 + ")";
                min = (int) value;
            }
        }
        return ret;
    }
}
