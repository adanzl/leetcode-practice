package com.leo.leetcode.algorithm.q1700;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 我们称一个分割整数数组的方案是 好的 ，当它满足：
 * 1、数组被分成三个 非空 连续子数组，从左至右分别命名为 left ， mid ， right 。
 * 2、left 中元素和小于等于 mid 中元素和，mid 中元素和小于等于 right 中元素和。
 * 给你一个 非负 整数数组 nums ，请你返回 好的 分割 nums 方案数目。由于答案可能会很大，请你将结果对 109 + 7 取余后返回。
 * 提示：
 * 1、3 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^4
 * 链接：https://leetcode-cn.com/problems/ways-to-split-array-into-three-subarrays
 */
public class Q1712 {
    // 二分查找，各种参数
    public static void main(String[] args) {
        // 1
        System.out.println(new Q1712().waysToSplit(stringToIntegerArray("[1,1,1]")));
        // 5
        System.out.println(new Q1712().waysToSplit(stringToIntegerArray("[0,2,2,2,0,5]")));
        // 4
        System.out.println(new Q1712().waysToSplit(stringToIntegerArray("[1,2,2,2,0,5]")));
        // 3
        System.out.println(new Q1712().waysToSplit(stringToIntegerArray("[1,2,2,2,5,0]")));
        // 0
        System.out.println(new Q1712().waysToSplit(stringToIntegerArray("[3,2,1]")));
    }

    public int waysToSplit(int[] nums) {
        int MOD = 1_000_000_007, sum = 0, n = nums.length;
        long ret = 0;
        int[] preSum = new int[n + 1];
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            preSum[i + 1] = sum;
        }
        for (int i = 1; i < n - 1; i++) {
            int b0 = getIdx(preSum, i + 1, n - 1, 2 * preSum[i], true, true);
            if (b0 == -1) continue;
            int b1 = getIdx(preSum, b0, n - 1, (preSum[i] + sum) / 2, false, false);
            if (b1 == -1) continue;
            ret = (ret + b1 - b0 + 1) % MOD;
        }
        return (int) ret;
    }

    int getIdx(int[] arr, int left, int right, int v, boolean lSide, boolean upper) {
        int ret = -1, l = left, r = right;
        while (l <= r) {
            int mid = (l + r) >> 1;
            if (arr[mid] < v) l = mid + 1;
            else if (arr[mid] == v) {
                ret = mid;
                if (lSide) r = mid - 1;
                else l = mid + 1;
            } else r = mid - 1;
        }
        if (ret != -1) return ret;
        if (upper) {
            if (l <= right) return l;
        } else if (r >= left) return r;
        return -1;
    }
}
