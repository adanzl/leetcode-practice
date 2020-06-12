package com.leo.leetcode.lcci;

import com.leo.utils.LCUtil;

import java.util.Arrays;

public class Q1001 {

    public static void main(String[] args) {
        int[] A = LCUtil.stringToIntegerArray("[1,2,3,0,0,0]");
        new Q1001().merge(A, 3, new int[]{2, 5, 6}, 3);
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
