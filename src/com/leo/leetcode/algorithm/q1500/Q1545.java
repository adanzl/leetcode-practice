package com.leo.leetcode.algorithm.q1500;

/**
 * 给你两个正整数 n 和 k，二进制字符串  Sn 的形成规则如下：
 * 1、S1 = "0"
 * 2、当 i > 1 时，Si = Si-1 + "1" + reverse(invert(Si-1))
 * 其中 + 表示串联操作，reverse(x) 返回反转 x 后得到的字符串，而 invert(x) 则会翻转 x 中的每一位（0 变为 1，而 1 变为 0）。
 * 例如，符合上述描述的序列的前 4 个字符串依次是：
 * 1、S1 = "0"
 * 2、S2 = "011"
 * 3、S3 = "0111001"
 * 4、S4 = "011100110110001"
 * 请你返回  Sn 的 第 k 位字符 ，题目数据保证 k 一定在 Sn 长度范围以内。
 * 提示：
 * 1、1 <= n <= 20
 * 2、1 <= k <= 2^n - 1
 * 链接：https://leetcode.cn/problems/find-kth-bit-in-nth-binary-string
 */
public class Q1545 {

    public static void main(String[] args) {
        // "0"
        System.out.println(new Q1545().findKthBit(3, 1));
        // "1"
        System.out.println(new Q1545().findKthBit(4, 11));
        // "0"
        System.out.println(new Q1545().findKthBit(1, 1));
        // "1"
        System.out.println(new Q1545().findKthBit(2, 3));
    }

    public char findKthBit(int n, int k) {
        if (k == 1) return '0';
        int mid = 1 << (n - 1);
        if (k == mid) return '1';
        else if (k < mid) return findKthBit(n - 1, k);
        else {
            k = mid * 2 - k;
            return (char) ('0' + '1' - findKthBit(n - 1, k));
        }
    }

}
