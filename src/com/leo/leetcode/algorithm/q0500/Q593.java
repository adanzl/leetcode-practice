package com.leo.leetcode.algorithm.q0500;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定2D空间中四个点的坐标 p1, p2, p3 和 p4，如果这四个点构成一个正方形，则返回 true 。
 * 点的坐标 pi 表示为 [xi, yi] 。输入 不是 按任何顺序给出的。
 * 一个 有效的正方形 有四条等边和四个等角(90度角)。
 * 提示:
 * 1、p1.length == p2.length == p3.length == p4.length == 2
 * 2、-10^4 <= xi, yi <= 10^4
 * 链接：https://leetcode.cn/problems/valid-square
 */
public class Q593 {

    public static void main(String[] args) {
        // false
        System.out.println(new Q593().validSquare(stringToIntegerArray("[0,0]"), stringToIntegerArray("[0,0]"), stringToIntegerArray("[0,0]"), stringToIntegerArray("[0,0]")));
        // true
        System.out.println(new Q593().validSquare(stringToIntegerArray("[0,0]"), stringToIntegerArray("[1,1]"), stringToIntegerArray("[1,0]"), stringToIntegerArray("[0,1]")));
        // false
        System.out.println(new Q593().validSquare(stringToIntegerArray("[0,0]"), stringToIntegerArray("[1,1]"), stringToIntegerArray("[1,0]"), stringToIntegerArray("[0,12]")));
        // true
        System.out.println(new Q593().validSquare(stringToIntegerArray("[1,0]"), stringToIntegerArray("[-1,0]"), stringToIntegerArray("[0,1]"), stringToIntegerArray("[0,-1]")));
    }

    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        int[][] ps = new int[][]{p1, p2, p3, p4};
        Arrays.sort(ps, (a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);
        double d1 = dist2(ps[0], ps[1]), d2 = dist2(ps[0], ps[2]), d3 = dist2(ps[3], ps[1]), d4 = dist2(ps[3], ps[2]);
        if (d1 == 0 || d1 != d2 || d2 != d3 || d3 != d4) return false;
        int[] v1 = vector(ps[0], ps[1]), v2 = vector(ps[0], ps[2]), v3 = vector(ps[3], ps[1]), v4 = vector(ps[3], ps[2]);
        return dot(v1, v2) == 0 && dot(v3, v4) == 0;
    }

    int[] vector(int[] p1, int[] p2) {
        return new int[]{p2[0] - p1[0], p2[1] - p1[1]};
    }

    int dot(int[] v1, int[] v2) {
        return v1[0] * v1[1] + v2[1] * v2[0];
    }

    double dist2(int[] p1, int[] p2) {
        return (p2[0] - p1[0]) * (p2[0] - p1[0]) + (p2[1] - p1[1]) * (p2[1] - p1[1]);
    }
}
