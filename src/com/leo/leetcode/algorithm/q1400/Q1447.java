package com.leo.leetcode.algorithm.q1400;

import java.util.ArrayList;
import java.util.List;

/**
 * 给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于  n 的 最简 分数 。
 * 分数可以以 任意 顺序返回。
 * 提示：
 * 1 <= n <= 100
 * 链接：https://leetcode-cn.com/problems/simplified-fractions/
 */
public class Q1447 {

    public static void main(String[] args) {
        // ["1/2"]
        System.out.println(new Q1447().simplifiedFractions(2));
        // ["1/2","1/3","2/3"]
        System.out.println(new Q1447().simplifiedFractions(3));
        // ["1/2","1/3","1/4","2/3","3/4"]
        System.out.println(new Q1447().simplifiedFractions(4));
        // []
        System.out.println(new Q1447().simplifiedFractions(1));
    }

    public List<String> simplifiedFractions(int n) {
        List<String> ret = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j < i; j++) {
                if (getGcd(i, j) == 1) ret.add(j + "/" + i);
            }
        }
        return ret;
    }

    int getGcd(int a, int b) {
        int remind = a % b;
        if (remind == 0) return b;
        return getGcd(b, remind);
    }
}
