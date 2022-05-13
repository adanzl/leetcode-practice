package com.leo.leetcode.lcci;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.int2dArrayToString;

/**
 * 编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
 * 链接：https://leetcode-cn.com/problems/zero-matrix-lcci/
 */
public class Q0108 {

    public static void main(String[] args) {
        int[][] arr;
        // [[1,0,1],[0,0,0],[1,0,1]]
        arr = stringToInt2dArray("[[1,1,1],[1,0,1],[1,1,1]]");
        new Q0108().setZeroes(arr);
        System.out.println(int2dArrayToString(arr));
        // [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        arr = stringToInt2dArray("[[0,1,2,0],[3,4,5,2],[1,3,1,5]]");
        new Q0108().setZeroes(arr);
        System.out.println(int2dArrayToString(arr));
    }

    public void setZeroes(int[][] matrix) {
        if (matrix.length == 0) return;
        int r = matrix.length, c = matrix[0].length;
        int[] rMark = new int[r], cMark = new int[c];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] == 0) {
                    rMark[i] = 1;
                    cMark[j] = 1;
                }
            }
        }
        for (int i = 0; i < rMark.length; i++) if (rMark[i] == 1) for (int j = 0; j < c; j++) matrix[i][j] = 0;
        for (int j = 0; j < cMark.length; j++) if (cMark[j] == 1) for (int i = 0; i < r; i++) matrix[i][j] = 0;
    }
}
