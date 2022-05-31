package com.leo.leetcode.algorithm.q2200;

import static com.leo.utils.LCUtil.stringToIntegerArray;

import java.util.*;

/**
 * 给你一个下标从 0 开始的整数数组 nums 。在一步操作中，移除所有满足 nums[i - 1] > nums[i] 的 nums[i] ，其中 0 < i < nums.length 。
 * 重复执行步骤，直到 nums 变为 非递减 数组，返回所需执行的操作数。
 * 链接：https://leetcode.cn/problems/steps-to-make-array-non-decreasing
 */
public class Q2289 {
    public static void main(String[] args) {
        // 3
        System.out.println(new Q2289().totalSteps(stringToIntegerArray("[5,3,4,4,7,3,6,11,8,5,11]")));
        // 3
        System.out.println(new Q2289().totalSteps(stringToIntegerArray("[7,14,4,14,13,2,6,13]")));
        // 6
        System.out.println(new Q2289().totalSteps(stringToIntegerArray("[10,1,2,3,4,5,6,1,2,3]")));
        // 0
        System.out.println(new Q2289().totalSteps(stringToIntegerArray("[4,5,7,7,13]")));
    }

    public int totalSteps(int[] nums) {
        int n = nums.length, ret = 0;
        int[] link = new int[n];
        link[n - 1] = -1;
        for (int i = 0; i < n - 1; i++) link[i] = i + 1;
        Queue<Integer> queue = new LinkedList<>();
        process(nums, link, 0, queue, false);
        if (!queue.isEmpty()) ret++;
        while (!queue.isEmpty()) {
            int size = queue.size(), count = 0;
            while (size-- > 0 && !queue.isEmpty()) {
                int cur = queue.poll();
                if (link[cur] == -1) continue;
                count += process(nums, link, cur, queue, true);
            }
            if (count > 0) ret++;
        }

        return ret;
    }

    int process(int[] nums, int[] link, int p, Queue<Integer> queue, boolean firstBreak) {
        int cur = link[p], pre = p, ret = 0;
        while (cur != -1) {
            int next = link[cur];
            if (nums[pre] > nums[cur]) {
                queue.add(pre);
                link[cur] = -1;
                ret++;
            } else {
                link[p] = cur;
                p = cur;
                if (firstBreak) return ret;
            }
            pre = cur;
            cur = next;
        }
        link[p] = -1;
        return ret;
    }
}
