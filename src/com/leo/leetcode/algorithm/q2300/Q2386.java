package com.leo.leetcode.algorithm.q2300;

import java.util.*;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums 和一个 正 整数 k 。你可以选择数组的任一 子序列 并且对其全部元素求和。
 * 数组的 第 k 大和 定义为：可以获得的第 k 个 最大 子序列和（子序列和允许出现重复）
 * 返回数组的 第 k 大和 。
 * 子序列是一个可以由其他数组删除某些或不删除元素排生而来的数组，且派生过程不改变剩余元素的顺序。
 * 注意：空子序列的和视作 0 。
 * 提示：
 * 1、n == nums.length
 * 2、1 <= n <= 10^5
 * 3、-10^9 <= nums[i] <= 10^9
 * 4、1 <= k <= min(2000, 2n)
 * 链接：https://leetcode.cn/problems/find-the-k-sum-of-an-array
 */
public class Q2386 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q2386().kSum(stringToIntegerArray("[2,4,-2]"), 5));
        // 10
        System.out.println(new Q2386().kSum(stringToIntegerArray("[1,-2,3,4,-10,12]"), 16));
    }

    public long kSum(int[] nums, long k) {
        long sum = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) sum += nums[i];
            else nums[i] = -nums[i];
        }
        // 转化成了第k大的子序列的和的问题
        Arrays.sort(nums);
        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(o -> o[0]));
        pq.offer(new long[]{0, -1});
        for (int i = 0; i < k - 1 && !pq.isEmpty(); i++) {
            long[] cur = pq.poll();
            long v = cur[0];
            int idx = (int) cur[1];
            if (idx == n - 1) continue;
            // 判定核心是新增加的元素一定大约弹出的元素
            pq.offer(new long[]{v + nums[idx + 1], idx + 1});
            if (idx >= 0) {
                pq.offer(new long[]{v - nums[idx] + nums[idx + 1], idx + 1});
            }
        }
        assert pq.peek() != null;
        return sum - pq.peek()[0];
    }
}
