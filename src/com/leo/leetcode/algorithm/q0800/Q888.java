package com.leo.leetcode.algorithm.q0800;

import java.util.Arrays;

public class Q888 {

    public static void main(String[] args) {
        // [26,11]
        System.out.println(Arrays.toString(new Q888().fairCandySwap(new int[]{1, 17, 14, 1, 16}, new int[]{26, 11})));
        // [1,2]
        System.out.println(Arrays.toString(new Q888().fairCandySwap(new int[]{1, 1}, new int[]{2, 2})));
        // [1,2]
        System.out.println(Arrays.toString(new Q888().fairCandySwap(new int[]{1, 2}, new int[]{2, 3})));
        // [2,3]
        System.out.println(Arrays.toString(new Q888().fairCandySwap(new int[]{2}, new int[]{1, 3})));
        // [5,4]
        System.out.println(Arrays.toString(new Q888().fairCandySwap(new int[]{1, 2, 5}, new int[]{2, 4})));
    }

    public int[] fairCandySwap(int[] A, int[] B) {
        int sum = 0;
        boolean[] flag = new boolean[100001];
        for (int n : A) sum += n;
        for (int n : B) {
            sum -= n;
            flag[n] = true;
        }
        sum /= 2;
        for (int a : A) {
            int diff = a - sum;
            if (diff >= 0 && diff < flag.length && flag[diff]) return new int[]{a, a - sum};
        }
        return new int[]{0, 0};
    }
}
