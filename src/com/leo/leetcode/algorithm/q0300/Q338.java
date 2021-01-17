package com.leo.leetcode.algorithm.q0300;

import java.util.Arrays;

public class Q338 {
    public void TestOJ() {
        System.out.println(Arrays.toString(countBits(0))); // []
        System.out.println(Arrays.toString(countBits(2))); // [0,1,1]
        System.out.println(Arrays.toString(countBits(5))); // [0,1,1,2,1,2]
    }

    public int[] countBits(int num) {
        int[] ret = new int[num + 1];
        ret[0] = 0;
        int v = 1;
        for (int i = 1; i <= num; i++) {
            if (v << 1 == i) v <<= 1;
            ret[i] = ret[i - v] + 1;
        }
        return ret;
    }
}
