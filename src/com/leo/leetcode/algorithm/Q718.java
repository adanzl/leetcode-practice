package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

public class Q718 {


    public static void main(String[] args) {
        System.out.println(new Q718().findLength(LCUtil.stringToIntegerArray("[0,1,1,1,1]"), LCUtil.stringToIntegerArray("[1,0,1,0,1]"))); // 2
    }

    public int findLength(int[] A, int[] B) {
        int[][] map = new int[A.length][];
        for (int i = 0; i < A.length; i++) {
            map[i] = new int[B.length];
        }
        int out = 0;
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < B.length; j++) {
                if (i == 0 || j == 0) {
                    map[i][j] = A[i] == B[j] ? 1 : 0;
                } else if (A[i] == B[j]) {
                    map[i][j] = map[i - 1][j - 1] + 1;
                } else {
                    map[i][j] = Math.max(map[i - 1][j], map[i][j - 1]);
                }
                out = Math.max(out, map[i][j]);
            }
        }
        return out;
    }
}
