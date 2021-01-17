package com.leo.leetcode.algorithm.q1500;

import java.util.Arrays;

public class Q5420 {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(new Q5420().finalPrices(new int[]{8, 4, 6, 2, 3}))); // [4,2,4,2,3]
        System.out.println(Arrays.toString(new Q5420().finalPrices(new int[]{1, 2, 3, 4, 5}))); // [1,2,3,4,5]
        System.out.println(Arrays.toString(new Q5420().finalPrices(new int[]{10, 1, 1, 6}))); // [9,0,1,6]
    }

    public int[] finalPrices(int[] prices) {
        int[] out = new int[prices.length], stack = new int[prices.length];
        for (int i = prices.length - 1, j = 0; i >= 0; i--) {
            while (j > 0 && prices[stack[j - 1]] > prices[i]) j--;
            if (j > 0) out[i] = prices[i] - prices[stack[j - 1]];
            else out[i] = prices[i];
            stack[j++] = i;
        }
        return out;
    }
}
