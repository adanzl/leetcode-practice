package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.LCUtil;

import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;

/**
 * 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
 * 你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
 * 返回 滑动窗口中的最大值 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、-10^4 <= nums[i] <= 10^4
 * 3、1 <= k <= nums.length
 * 链接：https://leetcode-cn.com/problems/sliding-window-maximum
 */
public class Q239 {
    public static void main(String[] args) {
        new Q239().TestOJ();
    }

    public void TestOJ() {
        // [3,3,5,5,6,7]
        System.out.println(Arrays.toString(maxSlidingWindow(LCUtil.stringToIntegerArray(" [1,3,-1,-3,5,3,6,7]"), 3)));
        // [3,3,5,5,6,7]
        System.out.println(Arrays.toString(maxSlidingWindow1(LCUtil.stringToIntegerArray(" [1,3,-1,-3,5,3,6,7]"), 3)));
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
