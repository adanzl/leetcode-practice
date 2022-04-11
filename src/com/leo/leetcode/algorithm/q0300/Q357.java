package com.leo.leetcode.algorithm.q0300;

/**
 * 给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10n 。
 * 提示： 0 <= n <= 8
 * 链接：https://leetcode-cn.com/problems/count-numbers-with-unique-digits/
 */
public class Q357 {

    public static void main(String[] args) {
        // 91
        System.out.println(new Q357().countNumbersWithUniqueDigits(2));
        // 1
        System.out.println(new Q357().countNumbersWithUniqueDigits(0));
    }

    public int countNumbersWithUniqueDigits(int n) {
        if (n == 0) return 1;
        int res = 10, uniqueDigits = 9, availableNumber = 9;
        while (n-- > 1 && availableNumber > 0) {
            uniqueDigits = uniqueDigits * availableNumber;
            res += uniqueDigits;
            availableNumber--;
        }
        return res;
    }
}
