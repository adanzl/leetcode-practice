package com.leo.leetcode.algorithm;

import java.util.HashMap;
import java.util.Map;

public class Q1 {
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
