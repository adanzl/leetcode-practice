package com.leo.leetcode.algorithm.q0500;

/**
 * 给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。
 * 提示：
 * -10^7 <= num <= 10^7
 * 链接：https://leetcode-cn.com/problems/base-7/
 */
public class Q504 {

    public static void main(String[] args) {
        // 202
        System.out.println(new Q504().convertToBase7(100));
        // -10
        System.out.println(new Q504().convertToBase7(-7));
        // 0
        System.out.println(new Q504().convertToBase7(0));
    }

    public String convertToBase7(int num) {
        if (num == 0) return "0";
        StringBuilder ret = new StringBuilder();
        int n = num;
        num = Math.abs(num);
        while (num != 0) {
            ret.append(num % 7);
            num /= 7;
        }
        if (n < 0) ret.append("-");
        return ret.reverse().toString();
    }
}
