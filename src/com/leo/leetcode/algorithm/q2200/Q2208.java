package com.leo.leetcode.algorithm.q2200;

import java.util.PriorityQueue;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个正整数数组 nums 。每一次操作中，你可以从 nums 中选择 任意 一个数并将它减小到 恰好 一半。（注意，在后续操作中你可以对减半过的数继续执行操作）
 * 请你返回将 nums 数组和 至少 减少一半的 最少 操作数。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^7
 * 链接：https://leetcode-cn.com/problems/minimum-operations-to-halve-array-sum
 */
public class Q2208 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q2208().halveArray(stringToIntegerArray("[3,8,20]")));
        // 3
        System.out.println(new Q2208().halveArray(stringToIntegerArray("[5,19,8,1]")));
    }

    public int halveArray(int[] nums) {
        double sum = 0, dst;
        PriorityQueue<Double> q = new PriorityQueue<>((o1, o2) -> Double.compare(o2, o1));
        for (int n : nums) {
            sum += n;
            q.add((double) n);
        }
        dst = sum / 2;
        int ret = 0;
        while (dst > 0 && !q.isEmpty()) {
            double n = q.poll();
            dst -= n / 2;
            q.add(n / 2);
            ret++;
        }
        return ret;
    }
}
