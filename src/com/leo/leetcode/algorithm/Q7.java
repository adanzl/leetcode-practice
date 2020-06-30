package com.leo.leetcode.algorithm;

/**
 * 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
 * 链接：https://leetcode-cn.com/problems/reverse-integer/
 */
public class Q7 {

    public static void main(String[] args) {
        System.out.println(new Q7().reverse(123)); // 321
        System.out.println(new Q7().reverse(-123)); // -321
        System.out.println(new Q7().reverse(120)); // 21
    }

    public int reverse(int x) {
        int ret = 0;
        while (x != 0) {
            int ext = x % 10;
            if (ext > 0 && ret > (Integer.MAX_VALUE - ext) / 10 || (ext < 0 && ret < (Integer.MIN_VALUE - ext) / 10)) {
                return 0;
            }
            ret = ret * 10 + ext;
            x /= 10;
        }
        return ret;
    }
}
