package com.leo.leetcode.algorithm.q1800;

import com.leo.utils.TestCase;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。
 * 数组 nums1 和 nums2 的 绝对差值和 定义为所有 |nums1[i] - nums2[i]|（0 <= i < n）的 总和（下标从 0 开始）。
 * 你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。
 * 在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 10^9 + 7 取余 后返回。
 * |x| 定义为：
 * 1、如果 x >= 0 ，值为 x ，或者
 * 2、如果 x <= 0 ，值为 -x
 * 提示：
 * 1、n == nums1.length
 * 2、n == nums2.length
 * 3、1 <= n <= 10^5
 * 4、1 <= nums1[i], nums2[i] <= 10^5
 * 链接：https://leetcode-cn.com/problems/minimum-absolute-sum-difference
 */
public class Q1818 {

    public static void main(String[] args) {
        // 999979264
        TestCase tc = new TestCase("resources/Q1818/Case001.txt");
        System.out.println(new Q1818().minAbsoluteSumDiff(
                stringToIntegerArray(tc.getData(0)),
                stringToIntegerArray(tc.getData(1))));
        // 20
        System.out.println(new Q1818().minAbsoluteSumDiff(
                stringToIntegerArray("[56,51,39,1,12,14,58,82,18,41,70,64,18,7,44,90,55,23,11,79,59,76,67,92,60,80,57,11,66,32,76,73,35,65,55,37,38,26,4,7,64,84,98,61,78,1,80,33,5,66,32,30,52,29,41,2,21,83,30,35,21,30,13,26,36,93,81,41,98,23,20,19,45,52,25,51,52,24,2,45,21,97,11,92,28,37,58,29,5,18,98,94,86,65,88,8,75,12,9,66]"),
                stringToIntegerArray("[64,32,98,65,67,40,71,93,74,24,49,80,98,35,86,52,99,65,15,92,83,84,80,71,46,11,26,70,80,2,81,57,97,12,68,10,49,80,24,18,45,72,33,94,60,5,94,99,14,41,25,83,77,67,49,70,94,83,55,17,61,44,50,62,3,36,67,10,2,39,53,62,44,72,66,7,3,6,80,38,43,100,17,25,24,78,8,4,36,86,9,68,99,64,65,15,42,59,79,66]")));
        // 20
        System.out.println(new Q1818().minAbsoluteSumDiff(stringToIntegerArray("[1,10,4,4,2,7]"), stringToIntegerArray("[9,3,5,1,7,4]")));
        // 3
        System.out.println(new Q1818().minAbsoluteSumDiff(stringToIntegerArray("[1,7,5]"), stringToIntegerArray("[2,3,5]")));
        // 0
        System.out.println(new Q1818().minAbsoluteSumDiff(stringToIntegerArray("[2,4,6,8,10]"), stringToIntegerArray("[2,4,6,8,10]")));
    }

    public int minAbsoluteSumDiff(int[] nums1, int[] nums2) {
        int n = nums1.length, max = 0, MOD = 1_000_000_007;
        long sum = 0;
        int[] numSorted = Arrays.copyOf(nums1, n);
        Arrays.sort(numSorted);
        for (int i = 0; i < n; i++) sum += Math.abs(nums1[i] - nums2[i]);
        for (int i = 0; i < n; i++) {
            int l = 0, r = n - 1, n2 = nums2[i];
            while (l <= r) {
                int mid = (l + r) >> 1;
                if (numSorted[mid] < n2) l = mid + 1;
                else r = mid - 1;
            }
            if (l >= n || (l > 0 && Math.abs(n2 - numSorted[l]) > Math.abs(n2 - numSorted[l - 1]))) l--;
            max = Math.max(max, Math.abs(nums2[i] - nums1[i]) - Math.abs(nums2[i] - numSorted[l])) % MOD;
        }
        return (int) ((sum - max) % MOD);
    }
}
