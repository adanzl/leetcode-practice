package com.leo.leetcode.algorithm.q0400;

/**
 * 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
 * 给出两个整数 x 和 y，计算它们之间的汉明距离。
 * <p>
 * 注意：
 * 0 ≤ x, y < 231.
 * <p>
 * 链接：https://leetcode-cn.com/problems/hamming-distance
 */
public class Q461 {
    public static void main(String[] args) {
        System.out.println(new Q461().hammingDistance(93, 73)); // 2
        System.out.println(new Q461().hammingDistance(1, 4)); // 2
    }

    public int hammingDistance(int x, int y) {
        int v = x ^ y, out = 0;
        while (v != 0) {
            if ((v & 1) == 1) out++;
            v >>= 1;
        }
        return out;
    }
}
