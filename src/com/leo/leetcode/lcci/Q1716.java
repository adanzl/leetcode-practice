package com.leo.leetcode.lcci;

/**
 * 一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。
 * 给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。
 * 注意：本题相对原题稍作改动
 * 链接：https://leetcode.cn/problems/the-masseuse-lcci
 */
public class Q1716 {

    public static void main(String[] args) {
        System.out.println(new Q1716().massage(new int[]{1, 2, 3, 1})); // 4
        System.out.println(new Q1716().massage(new int[]{2, 7, 9, 3, 1})); // 12
        System.out.println(new Q1716().massage(new int[]{2, 1, 4, 5, 3, 1, 1, 3})); // 12
    }

    public int massage(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        if (nums.length == 2) return Math.max(nums[0], nums[1]);
        int[] mark = new int[nums.length];
        mark[0] = nums[0];
        mark[1] = Math.max(nums[0], nums[1]);
        int out = mark[0];
        for (int i = 2; i < nums.length; i++) {
            mark[i] = Math.max(mark[i - 1], mark[i - 2] + nums[i]);
            out = Math.max(out, mark[i]);
        }
        return out;
    }
}
