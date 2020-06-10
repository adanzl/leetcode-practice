package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;

public class Q239 {
    public static void main(String[] args) {
        new Q239().TestOJ();
    }

    public void TestOJ() {
        System.out.println(Arrays.toString(maxSlidingWindow(LCUtil.stringToIntegerArray(" [1,3,-1,-3,5,3,6,7]"), 3))); // [3,3,5,5,6,7]
        System.out.println(Arrays.toString(maxSlidingWindow1(LCUtil.stringToIntegerArray(" [1,3,-1,-3,5,3,6,7]"), 3))); // [3,3,5,5,6,7]
    }

    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums.length == 0 || k == 0) return nums;
        int[] out = new int[nums.length - k + 1];
        Queue<Integer> q = new PriorityQueue<>((o1, o2) -> o2 - o1);
        int j = 0;
        for (int num : nums) {
            q.add(num);
            if (q.size() == k) {
                int v = nums[j];
                out[j] = q.peek();
                q.remove(v);
                j++;
            }
        }
        return out;
    }

    public int[] maxSlidingWindow1(int[] nums, int k) {
        if (nums.length == 0) return nums;
        int[] out = new int[nums.length - k + 1];
        int j, maxPos = -1;
        for (int i = 0; i <= nums.length - k; ++i) {
            j = i + k - 1;
            if (maxPos != -1 && nums[j] >= nums[maxPos]) {
                maxPos = j;
                out[i] = nums[maxPos];
            } else if (i <= maxPos) {
                out[i] = nums[maxPos];
            } else {
                int maxWindow = Integer.MIN_VALUE;
                int maxPosWindow = 0;
                for (int z = i; z <= j; ++z) {
                    if (nums[z] > maxWindow) {
                        maxPosWindow = z;
                        maxWindow = nums[z];
                    }
                }
                maxPos = maxPosWindow;
                out[i] = nums[maxPos];
            }
        }
        return out;
    }
}
