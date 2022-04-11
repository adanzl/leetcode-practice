package com.leo.leetcode.algorithm.q2200;

import java.util.*;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个非负整数数组 nums 和一个整数 k 。每次操作，你可以选择 nums 中 任一 元素并将它 增加 1 。
 * 请你返回 至多 k 次操作后，能得到的 nums的 最大乘积 。
 * 由于答案可能很大，请你将答案对 10^9 + 7 取余后返回。
 * 提示：
 * 1、1 <= nums.length, k <= 10^5
 * 2、0 <= nums[i] <= 10^6
 * 链接：https://leetcode-cn.com/problems/maximum-product-after-k-increments
 */
public class Q2233 {

    public static void main(String[] args) {
        // 216
        System.out.println(new Q2233().maximumProduct(stringToIntegerArray("[6,3,3,2]"), 2));
        // 20
        System.out.println(new Q2233().maximumProduct(stringToIntegerArray("[0,4]"), 5));
    }

    public int maximumProduct(int[] nums, int k) {
        int MOD = 1_000_000_007;
        long ret = 1;
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int num : nums) minHeap.add(num);
        while (k-- > 0 && !minHeap.isEmpty()) minHeap.add(minHeap.poll() + 1);
        for (int num : minHeap) ret = (ret * num) % MOD;
        return (int) ret;
    }
}
