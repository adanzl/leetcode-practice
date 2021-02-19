package com.leo.leetcode.algorithm.q0600;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。
 * 你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
 * <p>
 * 提示：
 * 1、nums.length 在1到 50,000 区间范围内。
 * 2、nums[i] 是一个在 0 到 49,999 范围内的整数。
 * <p>
 * 链接：https://leetcode-cn.com/problems/degree-of-an-array
 */
public class Q697 {

    public static void main(String[] args) {
        // 7
        System.out.println(new Q697().findShortestSubArray(stringToIntegerArray("[2,1,1,2,1,3,3,3,1,3,1,3,2]")));
        // 2
        System.out.println(new Q697().findShortestSubArray(stringToIntegerArray("[1,2,2,3,1]")));
        // 6
        System.out.println(new Q697().findShortestSubArray(stringToIntegerArray("[1,2,2,3,1,4,2]")));
    }

    public int findShortestSubArray(int[] nums) {
        int ret = Integer.MAX_VALUE, max = 0, min = Integer.MAX_VALUE, degree = 0;
        for (int n : nums) {
            max = Math.max(max, n);
            min = Math.min(min, n);
        }
        int[][] marks = new int[max - min + 1][3];
        for (int i = 0; i < nums.length; i++) {
            int[] p = marks[nums[i] - min];
            p[0]++;
            if (p[0] == 1) p[1] = i;
            if (p[0] >= degree) {
                degree = p[0];
                p[2] = i;
            }
        }
        if (degree == 1) return 1;
        for (int[] m : marks) if (m[0] == degree) ret = Math.min(m[2] - m[1], ret);
        return ret + 1;
    }
}
