package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

import java.util.PriorityQueue;
import java.util.Queue;

public class Q215 {

    public static void main(String[] args) {
        new Q215().TestOJ();
    }

    public void TestOJ() {
        System.out.println(findKthLargest(LCUtil.stringToIntegerArray("[3,2,1,5,6,4]"), 2)); // 5
        System.out.println(findKthLargest(LCUtil.stringToIntegerArray("[3,2,3,1,2,4,5,5,6]"), 4)); // 4
        System.out.println(findKthLargest1(LCUtil.stringToIntegerArray("[3,2]"), 2)); // 2
        System.out.println(findKthLargest1(LCUtil.stringToIntegerArray("[3]"), 1)); // 3
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
