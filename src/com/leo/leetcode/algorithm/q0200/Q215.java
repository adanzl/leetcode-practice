package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.LCUtil;

import java.util.PriorityQueue;
import java.util.Queue;

/**
 * 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
 * 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
 * 提示：
 * 1、1 <= k <= nums.length <= 10^4
 * 2、-10^4 <= nums[i] <= 10^4
 * 链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
 */
public class Q215 {

    public static void main(String[] args) {
        new Q215().TestOJ();
    }

    public void TestOJ() {
        // 5
        System.out.println(findKthLargest(LCUtil.stringToIntegerArray("[3,2,1,5,6,4]"), 2));
        // 4
        System.out.println(findKthLargest(LCUtil.stringToIntegerArray("[3,2,3,1,2,4,5,5,6]"), 4));
        // 2
        System.out.println(findKthLargest1(LCUtil.stringToIntegerArray("[3,2]"), 2));
        // 3
        System.out.println(findKthLargest1(LCUtil.stringToIntegerArray("[3]"), 1));
    }

    public int findKthLargest(int[] nums, int k) {
        Queue<Integer> q = new PriorityQueue<>();
        for (int v : nums) {
            q.add(v);
            if (q.size() == k + 1) q.poll();
        }
        return q.isEmpty() ? -1 : q.peek();
    }

    public int findKthLargest1(int[] nums, int k) {
        if (nums.length < k) return -1;
        if (nums.length == 1) return nums[0];
        int start = 0, end = nums.length - 1;
        while (true) {
            int ret = nums[start];
            int l = start, r = end;
            while (l < r) {
                while (nums[r] >= ret && l < r) r--;
                while (nums[l] <= ret && l < r) l++;
                swap(nums, l, r);
            }
            swap(nums, start, l);
            if (l == nums.length - k) return nums[l];
            if (l < nums.length - k) start = l + 1;
            else end = l - 1;
        }
    }

    void swap(int[] nums, int l, int r) {
        if (l == r) return;
        int t = nums[r];
        nums[r] = nums[l];
        nums[l] = t;
    }
}
