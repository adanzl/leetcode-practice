package com.leo.leetcode.algorithm.q0600;

/**
 * 给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。
 * 提示：1 <= n <= 2^31 - 1
 * 链接：https://leetcode-cn.com/problems/binary-number-with-alternating-bits/
 */
public class Q693 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q693().hasAlternatingBits(5));
        // false
        System.out.println(new Q693().hasAlternatingBits(7));
        // false
        System.out.println(new Q693().hasAlternatingBits(11));
    }

    public boolean hasAlternatingBits(int n) {
        boolean flag = (n & 1) != 0;
        n >>= 1;
        while (n != 0) {
            if (((n & 1) == 0) ^ flag) return false;
            flag = !flag;
            n >>= 1;
        }
        return true;
    }
}
