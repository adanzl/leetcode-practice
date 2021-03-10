package com.leo.leetcode.algorithm.q0200;

import java.util.ArrayList;
import java.util.List;

/**
 * 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。
 * 你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。
 *
 * 链接：https://leetcode-cn.com/problems/different-ways-to-add-parentheses
 */
public class Q241 {

    public static void main(String[] args) {
        // [0, 2]
        System.out.println(new Q241().diffWaysToCompute("2-1-1"));
        // [-34, -14, -10, -10, 10]
        System.out.println(new Q241().diffWaysToCompute("2*3-4*5"));
    }

    public List<Integer> diffWaysToCompute(String input) {
        return func(input.toCharArray(), 0, input.length());
    }

    List<Integer> func(char[] str, int s, int e) {
        List<Integer> ret = new ArrayList<>();
        int n = 0, p = s;
        boolean bNum = true;
        while (p < e) {
            if (!Character.isDigit(str[p])) {
                bNum = false;
                break;
            }
            n = n * 10 + str[p] - '0';
            p++;
        }
        if (bNum) {
            ret.add(n);
            return ret;
        }
        while (p < e) {
            char c = str[p];
            if (c == '-' || c == '+' || c == '*') merge(func(str, s, p), func(str, p + 1, e), c, ret);
            p++;
        }
        return ret;
    }

    void merge(List<Integer> l0, List<Integer> l1, char opt, List<Integer> out) {
        for (int v0 : l0) {
            for (int v1 : l1) {
                if (opt == '-') out.add(v0 - v1);
                else if (opt == '+') out.add(v0 + v1);
                else if (opt == '*') out.add(v0 * v1);
            }
        }
    }
}
