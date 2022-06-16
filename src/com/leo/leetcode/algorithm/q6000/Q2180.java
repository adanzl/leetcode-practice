package com.leo.leetcode.algorithm.q6000;

/**
 * 给你一个正整数 num ，请你统计并返回 小于或等于 num 且各位数字之和为 偶数 的正整数的数目。
 * 正整数的 各位数字之和 是其所有位上的对应数字相加的结果。
 * 提示：1 <= num <= 1000
 * 链接：https://leetcode.cn/problems/count-integers-with-even-digit-sum
 */
public class Q2180 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q2180().countEven(4));
        // 14
        System.out.println(new Q2180().countEven(30));
    }

    public int countEven(int num) {
        int ret = 0;
        for (int i = 1; i <= num; i++) {
            int n = i, sum = 0;
            while (n != 0) {
                sum += n % 10;
                n /= 10;
            }
            if ((sum & 1) == 0) ret++;
        }
        return ret;
    }
}
