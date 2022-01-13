package com.leo.leetcode.algorithm.q0300;

/**
 * 累加数 是一个字符串，组成它的数字可以形成累加序列。
 * 一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
 * 给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。
 * 说明：累加序列里的数 不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
 * 提示：
 * 1、1 <= num.length <= 35
 * 2、num 仅由数字（0 - 9）组成
 * <p>
 * 进阶：你计划如何处理由于过大的整数输入导致的溢出?
 * <p>
 * 链接：https://leetcode-cn.com/problems/additive-number
 */
public class Q306 {

    public static void main(String[] args) {
        System.out.println(new Q306().isAdditiveNumber("11111111111011111111111")); // true
        System.out.println(new Q306().isAdditiveNumber("198019823962")); // true
        System.out.println(new Q306().isAdditiveNumber("199111992")); // true
        System.out.println(new Q306().isAdditiveNumber("0235813")); // false
        System.out.println(new Q306().isAdditiveNumber("1203")); // false
        System.out.println(new Q306().isAdditiveNumber("0112")); // true
        System.out.println(new Q306().isAdditiveNumber("01012")); // false
        System.out.println(new Q306().isAdditiveNumber("11")); // false
        System.out.println(new Q306().isAdditiveNumber("111")); // false
        System.out.println(new Q306().isAdditiveNumber("199100199")); // true
        System.out.println(new Q306().isAdditiveNumber("112358")); // true
    }

    public boolean isAdditiveNumber(String num) {
        if (num.length() < 3) return false;
        Num.num = num;
        int len = num.length() / 2;
        for (int i = 1; i <= len; i++) {
            for (int j = 1; j <= len; j++) {
                if (valid(new Num(0, i), new Num(i, i + j)))
                    return true;
                if (Num.num.charAt(i) == '0') break;
            }
            if (Num.num.charAt(0) == '0') break;
        }
        return false;
    }

    boolean valid(Num n0, Num n1) {
        int len = Num.num.length();
        long sum = n0.value + n1.value;
        for (int i = 1; n1.e + i <= len && i <= len / 2; i++) {
            Num n2 = new Num(n1.e, n1.e + i);
            if (n2.value > sum) continue;
            if (n2.value == sum) return n2.e == len || valid(n1, n2);
            if (Num.num.charAt(n1.e) == '0') break;
        }
        return false;
    }

    static class Num {
        public static String num;
        int s, e;
        long value;

        Num(int s, int e) {
            this.s = s;
            this.e = e;
            this.value = Long.parseLong(num.substring(s, e));
        }
    }
}
