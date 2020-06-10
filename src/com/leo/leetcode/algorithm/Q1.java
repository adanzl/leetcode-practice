package com.leo.leetcode.algorithm;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Q1 {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(new Q1().twoSum(new int[]{2, 7, 11, 15}, 9)));
    }

    public int[] twoSum(int[] nums, int target) {
        int[] ret = new int[2];
        Map<Integer, Integer> m = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int v = nums[i];
            int right = target - v;
            if (m.containsKey(right)) {
                return new int[]{i, m.get(right)};
            } else {
                m.put(v, i);
            }
        }

        return ret;
    }

}
