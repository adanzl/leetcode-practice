package com.leo.leetcode.algorithm.q0300;

import java.util.Arrays;
import java.util.Random;

public class Q384 {

    public static void main(String[] args) {
        int[] nums;
        nums = new int[]{1, 2, 3};
        Solution obj = new Solution(nums);
        System.out.println(Arrays.toString(obj.shuffle())); // [3, 1, 2]
        System.out.println(Arrays.toString(obj.reset())); // [1, 2, 3]
        System.out.println(Arrays.toString(obj.shuffle())); // [1, 3, 2]]
    }

    static class Solution {

        int[] nums;
        int[] original;
        Random random = new Random();

        public Solution(int[] nums) {
            this.nums = nums;
            this.original = nums.clone();
        }

        public int[] reset() {
            return original;
        }

        public int[] shuffle() {
            for (int i = 0; i < nums.length; i++) {
                int index = random.nextInt(nums.length - i) + i;
                int v = nums[i];
                nums[i] = nums[index];
                nums[index] = v;
            }
            return nums;
        }
    }
}
