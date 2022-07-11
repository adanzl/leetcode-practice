package com.leo.leetcode.algorithm.q2300;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，长度为 n 。
 * 数组 nums1 和 nums2 的 差值平方和 定义为所有满足 0 <= i < n 的 (nums1[i] - nums2[i])2 之和。
 * 同时给你两个正整数 k1 和 k2 。你可以将 nums1 中的任意元素 +1 或者 -1 至多 k1 次。
 * 类似的，你可以将 nums2 中的任意元素 +1 或者 -1 至多 k2 次。
 * 请你返回修改数组 nums1 至多 k1 次且修改数组 nums2 至多 k2 次后的最小 差值平方和 。
 * 注意：你可以将数组中的元素变成 负 整数。
 * 提示：
 * 1、n == nums1.length == nums2.length
 * 2、1 <= n <= 10^5
 * 3、0 <= nums1[i], nums2[i] <= 10^5
 * 4、0 <= k1, k2 <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-sum-of-squared-difference
 */
public class Q2333 {

    public static void main(String[] args) {
        // 5000000000000
        System.out.println(new Q2333().minSumSquareDiff(stringToIntegerArray("[1000000,1000000,1000000,1000000,1000000]"), stringToIntegerArray("[0,0,0,0,0]"), 0, 0));
        // 0
        System.out.println(new Q2333().minSumSquareDiff(stringToIntegerArray("[10,10,10,11,5]"), stringToIntegerArray("[1,0,6,6,1]"), 11, 27));
        // 43
        System.out.println(new Q2333().minSumSquareDiff(stringToIntegerArray("[1,4,10,12]"), stringToIntegerArray("[5,8,6,9]"), 1, 1));
        // 579
        System.out.println(new Q2333().minSumSquareDiff(stringToIntegerArray("[1,2,3,4]"), stringToIntegerArray("[2,10,20,19]"), 0, 0));
    }

    public long minSumSquareDiff(int[] nums1, int[] nums2, int k1, int k2) {
        int n = nums1.length;
        int[] d = new int[n];
        for (int i = 0; i < n; i++) d[i] = Math.abs(nums1[i] - nums2[i]);
        Arrays.sort(d);
        int k = k1 + k2, l = 0, r = d[n - 1], v = Integer.MAX_VALUE;
        long remain = 0;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            long sum = 0;
            for (int num : d) {
                if (num > mid) sum += num - mid;
            }
            if (sum > k) l = mid + 1;
            else {
                r = mid - 1;
                v = mid;
                remain = k - sum;
            }
        }
        long ret = 0;
        for (int i = n - 1; i >= 0; i--) {
            long num = d[i];
            if (num > v) num = v;
            if (num > 0 && remain-- > 0) num--;
            ret += num * num;
        }
        return ret;
    }
}
