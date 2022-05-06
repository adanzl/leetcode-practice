package com.leo.leetcode.algorithm.q0200;

import java.util.ArrayList;
import java.util.List;

/**
 * 给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回 所有 能够得到 target 的表达式。
 * 注意，返回表达式中的操作数 不应该 包含前导零。
 * 提示：
 * 1、1 <= num.length <= 10
 * 2、num 仅含数字
 * 3、-2^31 <= target <= 2^31 - 1
 * 链接：https://leetcode-cn.com/problems/expression-add-operators
 */
public class Q282 {

    public static void main(String[] args) {
        // ["1+2+3", "1*2*3"]
        System.out.println(new Q282().addOperators("123", 6));
        // ["2*3+2", "2+3*2"]
        System.out.println(new Q282().addOperators("232", 8));
        // [1*0+5, 10-5]
        System.out.println(new Q282().addOperators("105", 5));
        // []
        System.out.println(new Q282().addOperators("3456237490", 9191));
    }

    public List<String> addOperators(String num, int target) {
        List<String> ret = new ArrayList<>();
        this.num = num.toCharArray();
        this.target = target;
        n = num.length();
        dfs(0, 0, 0, "", ret);
        return ret;
    }

    int n, target;
    char[] num;

    void dfs(int d, long pre, long sum, String s, List<String> ret) {
        if (d == n) {
            if (sum == target) ret.add(s);
            return;
        }
        long val = 0;
        for (int i = d; i < n; i++) {
            if (i != d && num[d] == '0')
                break;
            val = val * 10 + num[i] - '0';
            if (d == 0) dfs(i + 1, val, val, String.valueOf(val), ret);
            else {
                dfs(i + 1, pre * val, sum - pre + pre * val, s + "*" + val, ret);
                dfs(i + 1, val, sum + val, s + "+" + val, ret);
                dfs(i + 1, -val, sum - val, s + "-" + val, ret);
            }

        }
    }

}
