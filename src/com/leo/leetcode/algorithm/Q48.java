package com.leo.leetcode.algorithm;

public class Q48 {
    public static void main(String[] args) {
        new Q48().rotate(new int[][]{{0, 1, 2}, {3, 4, 5}, {6, 7, 8}});
    }

    public void rotate(int[][] matrix) {
        for (int x = 0; x < matrix.length; x++) {
            for (int y = x; y < matrix[x].length; y++) {
                int t = matrix[y][x];
                matrix[y][x] = matrix[x][y];
                matrix[x][y] = t;
            }
        }
        for (int x = 0; x < (matrix.length + 1) / 2; x++) {
            for (int y = 0; y < matrix[x].length; y++) {
                int t = matrix[y][x];
                matrix[y][x] = matrix[y][matrix[y].length - 1 - x];
                matrix[y][matrix[y].length - 1 - x] = t;
            }
        }
    }
}
