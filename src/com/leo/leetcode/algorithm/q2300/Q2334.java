package com.leo.leetcode.algorithm.q2300;

import java.util.Stack;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums 和一个整数 threshold 。
 * 找到长度为 k 的 nums 子数组，满足数组中 每个 元素都 大于 threshold / k 。
 * 请你返回满足要求的 任意 子数组的 大小 。如果没有这样的子数组，返回 -1 。
 * 子数组 是数组中一段连续非空的元素序列。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i], threshold <= 10^9
 * 链接：https://leetcode.cn/problems/subarray-with-elements-greater-than-varying-threshold
 */
public class Q2334 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q2334().validSubArraySize(stringToIntegerArray("[1,3,4,3,1]"), 6));
        // 1/2/3/4/5
        System.out.println(new Q2334().validSubArraySize(stringToIntegerArray("[6,5,6,5,8]"), 7));
    }


    public int validSubArraySize(int[] nums, int threshold) {
        int n = nums.length;
        Stack<Integer> stack = new Stack<>();
        int[] lList = new int[n], rList = new int[n];
        for (int i = 0; i < n; i++) {
            lList[i] = -1;
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) stack.pop();
            if (!stack.isEmpty()) lList[i] = stack.peek();
            stack.push(i);
        }
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            rList[i] = n;
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) stack.pop();
            if (!stack.isEmpty()) rList[i] = stack.peek();
            stack.push(i);
        }
        for (int i = 0; i < n; i++) {
            int l = lList[i], r = rList[i];
            if (nums[i] > threshold / (r - l - 1)) return r - l - 1;
        }
        return -1;
    }

}
