package com.leo.leetcode.algorithm.q0500;

/**
 * 给定一个表示分数加减运算的字符串 expression ，你需要返回一个字符串形式的计算结果。
 * 这个结果应该是不可约分的分数，即最简分数。 如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1。
 * 提示:
 * 1、输入和输出字符串只包含 '0' 到 '9' 的数字，以及 '/', '+' 和 '-'。
 * 2、输入和输出分数格式均为 ±分子/分母。如果输入的第一个分数或者输出的分数是正数，则 '+' 会被省略掉。
 * 3、输入只包含合法的最简分数，每个分数的分子与分母的范围是 [1,10]。 如果分母是1，意味着这个分数实际上是一个整数。
 * 4、输入的分数个数范围是 [1,10]。
 * 5、最终结果的分子与分母保证是 32 位整数范围内的有效整数。
 * 链接：https://leetcode.cn/problems/fraction-addition-and-subtraction
 */
public class Q592 {

    public static void main(String[] args) {
        // "-1/6"
        System.out.println(new Q592().fractionAddition("1/3-1/2"));
        // "1/3"
        System.out.println(new Q592().fractionAddition("-1/2+1/2+1/3"));
        // "0/1"
        System.out.println(new Q592().fractionAddition("-1/2+1/2"));
    }

    public String fractionAddition(String expression) {
        long[] ret = new long[]{0, 1}, num = new long[]{0, 0};
        int idx = 0, sign = 1;
        for (char c : expression.toCharArray()) {
            if (c == '-' || c == '+') {
                if (idx == 1) {
                    num[0] *= sign;
                    ret = add(ret, num);
                    idx = 0;
                    num[0] = 0;
                    num[1] = 0;
                }
                sign = c == '-' ? -1 : 1;
            } else if (c == '/') {
                idx++;
            } else {
                num[idx] = num[idx] * 10 + (c - '0');
            }
        }
        if (num[1] != 0) {
            num[0] *= sign;
            ret = add(ret, num);
        }
        return ret[0] + "/" + ret[1];
    }

    long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    long[] add(long[] num1, long[] num2) {
        num1[0] = num1[0] * num2[1] + num1[1] * num2[0];
        num1[1] = num1[1] * num2[1];
        if (num1[0] == 0) {
            num1[1] = 1;
        } else {
            long g = Math.abs(gcd(num1[0], num1[1]));
            num1[0] /= g;
            num1[1] /= g;
        }
        return num1;
    }
}
