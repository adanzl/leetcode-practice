package com.leo.leetcode.algorithm.q1500;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。
 * 一个子数组指的是原数组中连续的一个子序列。
 * 请你返回满足题目要求的最短子数组的长度。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、0 <= arr[i] <= 10^9
 * 链接：https://leetcode-cn.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted
 */
public class Q1574 {

    public static void main(String[] args) {
        // 13
        System.out.println(new Q1574().findLengthOfShortestSubArray(stringToIntegerArray("[36,6,1,19,26,24,27,34,2,16,31,10,8,2,10,14,29,35,37]")));
        // 5
        System.out.println(new Q1574().findLengthOfShortestSubArray(stringToIntegerArray("[8,9,5,8,11,14,2]")));
        // 8
        System.out.println(new Q1574().findLengthOfShortestSubArray(stringToIntegerArray("[13,0,14,7,18,18,18,16,8,15,20]")));
        // 4
        System.out.println(new Q1574().findLengthOfShortestSubArray(stringToIntegerArray("[5,4,3,2,1]")));
        // 3
        System.out.println(new Q1574().findLengthOfShortestSubArray(stringToIntegerArray("[2,2,2,1,1,1]")));
        // 3
        System.out.println(new Q1574().findLengthOfShortestSubArray(stringToIntegerArray("[1,2,3,10,4,2,3,5]")));
        // 2
        System.out.println(new Q1574().findLengthOfShortestSubArray(stringToIntegerArray("[1,2,3,10,0,7,8,9]")));
        // 0
        System.out.println(new Q1574().findLengthOfShortestSubArray(stringToIntegerArray("[1,2,3]")));
        // 0
        System.out.println(new Q1574().findLengthOfShortestSubArray(stringToIntegerArray("[1]")));
    }

    public int findLengthOfShortestSubArray(int[] arr) {
        int n = arr.length, l = 0, r = n - 1;
        while (r > 0 && arr[r] >= arr[r - 1]) r--;
        if (r == 0) return 0;
        while (l < n - 1 && arr[l + 1] >= arr[l]) l++;
        if (arr[r] >= arr[l]) return r - l - 1;
        if (arr[n - 1] < arr[0]) return Math.min(n - l - 1, r);
        int ret = r;
        for (int i = 0; i <= l; i++) ret = Math.min(ret, search(arr, r, n - 1, arr[i]) - i - 1);
        return ret;
    }

    int search(int[] arr, int l, int r, int target) {
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] < target) l = mid + 1;
            else r = mid - 1;
        }
        return l;
    }
}
