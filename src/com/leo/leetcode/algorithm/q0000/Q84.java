package com.leo.leetcode.algorithm.q0000;

import java.util.Stack;

/**
 * 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
 * 求在该柱状图中，能够勾勒出来的矩形的最大面积。
 * 提示：
 * 1、1 <= heights.length <=10^5
 * 2、0 <= heights[i] <= 10^4
 * 链接：https://leetcode.cn/problems/largest-rectangle-in-histogram/
 */
public class Q84 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q84().largestRectangleArea(new int[]{0, 0, 0}));
        // 10
        System.out.println(new Q84().largestRectangleArea(new int[]{2, 1, 5, 6, 2, 3}));
        // 9
        System.out.println(new Q84().largestRectangleArea(new int[]{9, 0}));
        // 4
        System.out.println(new Q84().largestRectangleArea(new int[]{2, 3}));
    }

    // 以第i根柱子为最矮柱子所能延伸的最大面积
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        long ret = 0;
        if (n == 0) return 0;
        int[] lPreMin = new int[n], rPreMin = new int[n];
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && heights[i] <= heights[stack.peek()]) stack.pop();
            lPreMin[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && heights[i] <= heights[stack.peek()]) stack.pop();
            rPreMin[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
            int left = lPreMin[i], right = rPreMin[i];
            ret = Math.max(ret, (long) (right - left - 1) * heights[i]);
        }
        return (int) ret;
    }
}
