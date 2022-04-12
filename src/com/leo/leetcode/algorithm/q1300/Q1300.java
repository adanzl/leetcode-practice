package com.leo.leetcode.algorithm.q1300;

import java.util.Arrays;

/**
 * 给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，使得将数组中所有大于 value 的值变成 value 后，数组的和最接近  target （最接近表示两者之差的绝对值最小）。
 * 如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。
 * 请注意，答案不一定是 arr 中的数字。
 * 提示：
 * 1 <= arr.length <= 10^4
 * 1 <= arr[i], target <= 10^5
 * 链接：https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target
 */
public class Q1300 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q1300().findBestValue(new int[]{4, 9, 3}, 10));
        // 5
        System.out.println(new Q1300().findBestValue(new int[]{2, 3, 5}, 11));
        // 6
        System.out.println(new Q1300().findBestValue(new int[]{3, 4, 5, 6}, 18));
        // 17422
        System.out.println(new Q1300().findBestValue(new int[]{1547, 83230, 57084, 93444, 70879}, 71237));
        // 5
        System.out.println(new Q1300().findBestValue(new int[]{2, 3, 5}, 10));
        // 11361
        System.out.println(new Q1300().findBestValue(new int[]{60864, 25176, 27249, 21296, 20204}, 56803));
    }

    public int findBestValue(int[] arr, int target) {
        Arrays.sort(arr);
        int n = arr.length, ret = Integer.MAX_VALUE, min = Integer.MAX_VALUE;
        long[] preSum = new long[arr.length + 1];
        for (int i = 0; i < arr.length; i++) preSum[i + 1] = preSum[i] + arr[i];
        int l = 0, r = arr[n - 1], p0 = 0, p1 = n - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            int idx = binarySearch(arr, p0, p1, mid);
            long sum = preSum[idx] + (long) mid * (n - idx), d = Math.abs(sum - target);
            if (min > d) {
                min = (int) d;
                ret = mid;
            }
            if (min == d) ret = Math.min(ret, mid);
            if (sum < target) l = mid + 1;
            else r = mid - 1;
        }
        return ret;
    }

    int binarySearch(int[] arr, int l, int r, int target) {
        while (l <= r) {
            int mid = (l + r) / 2;
            if (arr[mid] == target) return mid;
            if (arr[mid] > target) r = mid - 1;
            else l = mid + 1;
        }
        return l;
    }
}
