package com.leo.leetcode.algorithm.q0800;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.int2dArrayToString;

/**
 * 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
 * 水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
 * 反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。
 * <p>
 * 说明:
 * 1、1 <= A.length = A[0].length <= 20
 * 2、0 <= A[i][j] <= 1
 * <p>
 * 链接：https://leetcode-cn.com/problems/flipping-an-image
 */
public class Q832 {

    public static void main(String[] args) {
        // [[1,0,0],[0,1,0],[1,1,1]]
        System.out.println(int2dArrayToString(new Q832().flipAndInvertImage(stringToInt2dArray("[[1,1,0],[1,0,1],[0,0,0]]"))));
        // [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
        System.out.println(int2dArrayToString(new Q832().flipAndInvertImage(stringToInt2dArray("[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]"))));
    }

    public int[][] flipAndInvertImage(int[][] A) {
        int r = A.length, c = A[0].length;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < (c + 1) >> 1; j++) {
                int t = A[i][c - 1 - j];
                A[i][c - 1 - j] = A[i][j] ^ 1;
                A[i][j] = t ^ 1;
            }
        }
        return A;
    }
}
