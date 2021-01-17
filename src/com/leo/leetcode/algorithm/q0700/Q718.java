package com.leo.leetcode.algorithm.q0700;

/**
 * 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
 * 说明:
 * 1 <= len(A), len(B) <= 1000
 * 0 <= A[i], B[i] < 100
 * 链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
 */
public class Q718 {

    public static void main(String[] args) {
        System.out.println(new Q718().findLength(new int[]{0, 1, 1, 1, 1}, new int[]{1, 0, 1, 0, 1})); // 2
        System.out.println(new Q718().findLength(new int[]{1, 2, 3, 2, 1}, new int[]{3, 2, 1, 4, 7})); // 3
    }

    public int findLength(int[] A, int[] B) {
        int[][] map = new int[A.length][];
        for (int i = 0; i < A.length; i++) map[i] = new int[B.length];
        int out = 0;
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < B.length; j++) {
                if (i == 0 || j == 0) map[i][j] = A[i] == B[j] ? 1 : 0;
                else if (A[i] == B[j]) map[i][j] = map[i - 1][j - 1] + 1;
                else map[i][j] = 0;
                out = Math.max(out, map[i][j]);
            }
        }
        return out;
    }
}
