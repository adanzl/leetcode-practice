package com.leo.leetcode.algorithm.q1500;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。
 * 请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。
 * <p>
 * 提示：
 * 1、n == mat.length == mat[i].length
 * 2、1 <= n <= 100
 * 3、1 <= mat[i][j] <= 100
 * 链接：https://leetcode-cn.com/problems/matrix-diagonal-sum/
 */
public class Q1572 {
    public static void main(String[] args) {
        // 25
        System.out.println(new Q1572().diagonalSum(stringToInt2dArray("[[1,2,3],[4,5,6],[7,8,9]]")));
        // 8
        System.out.println(new Q1572().diagonalSum(stringToInt2dArray("[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]")));
        // 5
        System.out.println(new Q1572().diagonalSum(stringToInt2dArray("[[5]]")));
    }

    public int diagonalSum(int[][] mat) {
        int ret = 0, len = mat.length;
        for (int i = 0; i < len; i++) {
            ret += mat[i][i];
            ret += mat[i][len - i - 1];
        }
        if ((len & 1) == 1) ret -= mat[len / 2][len / 2];
        return ret;
    }
}
