package com.leo.leetcode.algorithm.q1500;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。
 * 请你找到这个数组里第 k 个缺失的正整数。
 * 提示：
 * 1、1 <= arr.length <= 1000
 * 2、1 <= arr[i] <= 1000
 * 3、1 <= k <= 1000
 * 4、对于所有 1 <= i < j <= arr.length 的 i 和 j 满足 arr[i] < arr[j]
 * 链接：https://leetcode-cn.com/problems/kth-missing-positive-number
 */
public class Q1539 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q1539().findKthPositive(stringToIntegerArray("[2]"), 1));
        // 9
        System.out.println(new Q1539().findKthPositive(stringToIntegerArray("[2,3,4,7,11]"), 5));
        // 6
        System.out.println(new Q1539().findKthPositive(stringToIntegerArray("[1,2,3,4]"), 2));
    }

    public int findKthPositive(int[] arr, int k) {
        int l = 0, r = arr.length - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] - mid - 1 >= k) r = mid - 1;
            else l = mid + 1;
        }
        return l + k;
    }
}
