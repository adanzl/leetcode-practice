package com.leo.leetcode.algorithm;

public class Q11 {
    public int maxArea(int[] height) {
        int ret = 0;
        for (int step = 1; step < height.length; step++) {
            for (int i = 0; i + step < height.length; i++) {
                ret = Math.max(ret, step * Math.min(height[i], height[i + step]));
            }
        }
        return ret;
    }
}
