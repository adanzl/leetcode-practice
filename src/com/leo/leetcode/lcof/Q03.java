package com.leo.leetcode.lcof;

public class Q03 {

    public static void main(String[] args) {
        System.out.println(new Q03().findRepeatNumber(new int[]{2, 3, 1, 0, 2, 5, 3})); // 2 || 3
    }

    public int findRepeatNumber(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int p = nums[i];
            while (p != i) {
                int t = nums[p];
                if (t == p) return p;
                nums[p] = p;
                p = t;
            }
        }
        return -1;
    }
}
