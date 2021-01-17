package com.leo.leetcode.algorithm.q0900;

import com.leo.utils.LCUtil;

public class Q974 {
    public static void main(String[] args) {
        System.out.println(new Q974().subarrayDivByK(LCUtil.stringToIntegerArray("[-1,2,9]"), 2)); // 2
        System.out.println(new Q974().subarrayDivByK(LCUtil.stringToIntegerArray("[4,5,0,-2,-3,1]"), 5)); // 7
        System.out.println(new Q974().subarrayDivByK(LCUtil.stringToIntegerArray("[-2]"), 6)); // 0
    }

    public int subarrayDivByK(int[] A, int K) {
        int[] m = new int[K];
        int[] sums = new int[A.length];
        int out = 0;
        m[0] = 1;
        for (int i = 0; i < A.length; i++) {
            if (i == 0) sums[i] = A[i];
            else sums[i] = sums[i - 1] + A[i];
            int v = sums[i] % K;
            if (v < 0) v += K;
            out += m[v];
            m[v]++;
        }
        return out;
    }
}
