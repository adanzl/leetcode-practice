package com.leo.leetcode.lcci;

import com.leo.utils.LCUtil;

import java.util.Arrays;

/**
 * 给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
 * 初始化 A 和 B 的元素数量分别为 m 和 n。
 * 说明: A.length == n + m
 * 链接：https://leetcode.cn/problems/sorted-merge-lcci/
 */
public class Q10_01 {

    public static void main(String[] args) {
        int[] A = LCUtil.stringToIntegerArray("[1,2,3,0,0,0]");
        new Q10_01().merge(A, 3, new int[]{2, 5, 6}, 3);
        System.out.println(Arrays.toString(A)); // [1,2,2,3,5,6]
    }

    public void merge(int[] A, int m, int[] B, int n) {
        int iA = m - 1, iB = n - 1, i = m + n - 1;
        while (i >= 0) {
            if (iA < 0) {
                A[i--] = B[iB--];
            } else if (iB < 0) {
                break;
            } else if (B[iB] > A[iA]) {
                A[i--] = B[iB--];
            } else {
                A[i--] = A[iA--];
            }
        }
    }
}
