package com.leo.leetcode.algorithm.q0400;

/**
 * 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 位数字。
 * <p>
 * 注意：n 是正数且在 32 位整数范围内（n < 2^31）。
 * <p>
 * 链接：https://leetcode-cn.com/problems/nth-digit
 */
public class Q400 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q400().findNthDigit(1000000000));
        // 0
        System.out.println(new Q400().findNthDigit(11));
        // 1
        System.out.println(new Q400().findNthDigit(12));
        // 3
        System.out.println(new Q400().findNthDigit(3));
        // 6
        System.out.println(new Q400().findNthDigit(300));
    }

    public int findNthDigit(int n) {
        int[] marks = {9, 180, 2700, 36000, 450000, 5400000, 63000000, 720000000};
        int index = 0;
        for (; index < marks.length; index++) {
            if (marks[index] > n) break;
            n -= marks[index];
        }
        int flag = index + 1;
        int base = index == 0 ? 0 : 1;
        while (index-- != 0) base *= 10;
        int c = base + n / flag, r = (flag - n % flag) % flag;
        if (r == 0 && flag != 1) c--;
        while (r-- != 0) c /= 10;
        return c % 10;
    }
}
