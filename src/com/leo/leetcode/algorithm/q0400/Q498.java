package com.leo.leetcode.algorithm.q0400;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
 * 提示：
 * 1、m == mat.length
 * 2、n == mat[i].length
 * 3、1 <= m, n <= 10^4
 * 4、1 <= m * n <= 10^4
 * 5、-10^5 <= mat[i][j] <= 10^5
 * 链接：https://leetcode.cn/problems/diagonal-traverse
 */
public class Q498 {

    public static void main(String[] args) {
        // [1,2,4,7,5,3,6,8,9]
        System.out.println(Arrays.toString(new Q498().findDiagonalOrder(stringToInt2dArray("[[1,2,3],[4,5,6],[7,8,9]]"))));
        // [1,2,3,4]
        System.out.println(Arrays.toString(new Q498().findDiagonalOrder(stringToInt2dArray("[[1,2],[3,4]]"))));
    }

    public int[] findDiagonalOrder(int[][] mat) {
        int m = mat.length, n = mat[0].length, idx = 0, i = 0, j = 0, d = 1;
        int[] res = new int[m * n];
        while (idx < res.length) {
            res[idx++] = mat[i][j];
            if (d == 1) {
                if (i - 1 >= 0 && j + 1 < n) {
                    i--;
                    j++;
                } else {
                    if (j + 1 < n) j++;
                    else i++;
                    d = -d;
                }
            } else {
                if (i + 1 < m && j - 1 >= 0) {
                    i++;
                    j--;
                } else {
                    if (i + 1 < m) i++;
                    else j++;
                    d = -d;
                }
            }
        }
        return res;
    }
}
