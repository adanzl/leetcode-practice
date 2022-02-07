package com.leo.leetcode.algorithm.q0000;

/**
 * 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
 * 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
 * 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
 * 说明：你不能倾斜容器，且 n 的值至少为 2。
 * 链接：https://leetcode-cn.com/problems/container-with-most-water
 */
public class Q11 {
    public static void main(String[] args) {
        System.out.println(new Q11().maxArea(new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7})); // 49
    }

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
