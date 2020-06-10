package com.leo.leetcode.offer;

import com.leo.utils.LCUtil;

import java.util.Arrays;
import java.util.LinkedList;

public class Q59 {

    public static void main(String[] args) {
        new Q59().TestOJ();
    }

    public void TestOJ() {
        System.out.println(Arrays.toString(maxSlidingWindow(LCUtil.stringToIntegerArray("[-7,-8,7,5,7,1,6,0]"), 4))); // [7,7,7,7,7]
        System.out.println(Arrays.toString(maxSlidingWindow(LCUtil.stringToIntegerArray("[1,3,1,2,0,5]"), 3))); // [3,3,2,5]
        System.out.println(Arrays.toString(maxSlidingWindow(LCUtil.stringToIntegerArray("[1,3,-1,-3,5,3,6,7]"), 3))); // [3, 3, 5, 5, 6, 7]
    }

    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums.length == 0) return new int[0];
        LinkedList<Integer> q = new LinkedList<>();
        int[] out = new int[nums.length - k + 1];
        for (int i = 0; i < nums.length; i++) {
            if (i > k - 1 && !q.isEmpty() && nums[i - k] == nums[q.peek()]) q.poll();
            int n = nums[i];
            while (!q.isEmpty() && nums[q.peek()] < n) q.poll();
            while (!q.isEmpty() && nums[q.getLast()] < n) q.removeLast();
            q.add(i);
            if (i >= k - 1) {
                out[i - k + 1] = nums[q.peek()];
            }
        }
        return out;
    }
}
