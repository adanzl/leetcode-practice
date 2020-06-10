package com.leo.leetcode.lcof;

import com.leo.utils.LCUtil;

import java.util.Arrays;

/**
 * 本题与主站 54 题相同
 */
public class Q29 {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(new Q29().spiralOrder(LCUtil.stringToInt2dArray("[[1,2,3],[4,5,6],[7,8,9]]")))); // [1,2,3,6,9,8,7,4,5]
        System.out.println(Arrays.toString(new Q29().spiralOrder(LCUtil.stringToInt2dArray("[[1,2,3,4],[5,6,7,8],[9,10,11,12]]")))); // [1,2,3,4,8,12,11,10,9,5,6,7]
    }

    public int[] spiralOrder(int[][] matrix) {
        if (matrix.length == 0) return new int[0];
        if (matrix[0].length == 0) return matrix[0];
        int d = 0; // 0: R, 1: D, 2: L, 3: U
        int x = 0, y = 0, i = 0, minX = 0, maxX = matrix[0].length - 1, minY = 0, maxY = matrix.length - 1;
        int[] out = new int[(maxX + 1) * (maxY + 1)];
        while (i < out.length) {
            if (d == 0) { // R
                if (x <= maxX) {
                    out[i++] = matrix[y][x++];
                } else {
                    d = 1;
                    x = maxX;
                    y++;
                    minY++;
                }
            } else if (d == 1) { // D
                if (y <= maxY) {
                    out[i++] = matrix[y++][x];
                } else {
                    d = 2;
                    y = maxY;
                    x--;
                    maxX--;
                }
            } else if (d == 2) { // L
                if (x >= minX) {
                    out[i++] = matrix[y][x--];
                } else {
                    d = 3;
                    x = minX;
                    y--;
                    maxY--;
                }
            } else { // U
                if (y >= minY) {
                    out[i++] = matrix[y--][x];
                } else {
                    d = 0;
                    y = minY;
                    x++;
                    minX++;
                }
            }
        }
        return out;
    }
}
