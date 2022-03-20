package com.leo.leetcode.algorithm.q1800;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你两个大小为 n x n 的二进制矩阵 mat 和 target 。
 * 现 以 90 度顺时针轮转 矩阵 mat 中的元素 若干次 ，如果能够使 mat 与 target 一致，返回 true ；否则，返回 false 。
 * 提示：
 * 1、n == mat.length == target.length
 * 2、n == mat[i].length == target[i].length
 * 3、1 <= n <= 10
 * 4、mat[i][j] 和 target[i][j] 不是 0 就是 1
 * 链接：https://leetcode-cn.com/problems/determine-whether-matrix-can-be-obtained-by-rotation
 */
public class Q1886 {

    public static void main(String[] args) {
        // 转度数       原坐标         转换坐标
        //  90°        [x, y]   ->   [y, n-x]
        //  180°       [x, y]   ->   [n-x, n-y]
        //  270°       [x, y]   ->   [n-y, x]
        // true
        System.out.println(new Q1886().findRotation(stringToInt2dArray("[[0,1],[1,0]]"), stringToInt2dArray("[[1,0],[0,1]]")));
        // false
        System.out.println(new Q1886().findRotation(stringToInt2dArray("[[0,1],[1,1]]"), stringToInt2dArray("[[1,0],[0,1]]")));
        // true
        System.out.println(new Q1886().findRotation(stringToInt2dArray("[[0,0,0],[0,1,0],[1,1,1]]"), stringToInt2dArray("[[1,1,1],[0,1,0],[0,0,0]]")));
    }

    public boolean findRotation(int[][] mat, int[][] target) {
        boolean ret = true;
        int n = mat.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] != target[i][j]) {
                    ret = false;
                    break;
                }
            }
        }
        if (ret) return true;
        ret = true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[j][n - i - 1] != target[i][j]) {
                    ret = false;
                    break;
                }
            }
        }
        if (ret) return true;
        ret = true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[n - i - 1][n - j - 1] != target[i][j]) {
                    ret = false;
                    break;
                }
            }
        }
        if (ret) return true;
        ret = true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[n - j - 1][i] != target[i][j]) {
                    ret = false;
                    break;
                }
            }
        }
        return ret;
    }
}
