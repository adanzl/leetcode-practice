package com.leo.leetcode.algorithm.q0400;

import com.leo.utils.TestCase;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
 * 你需要返回给定数组中的重要翻转对的数量。
 * 注意:
 * 1、给定数组的长度不会超过50000。
 * 2、输入数组中的所有数字都在32位整数的表示范围内。
 * 链接：https://leetcode-cn.com/problems/reverse-pairs
 */
public class Q493 {
    // 利用归并特性
    public static void main(String[] args) {
        // 0
        System.out.println(new Q493().reversePairs(stringToIntegerArray("[2147483647,2147483647,2147483647,2147483647,2147483647,2147483647]")));
        // 2
        System.out.println(new Q493().reversePairs(stringToIntegerArray("[1,3,2,3,1]")));
        // 3
        System.out.println(new Q493().reversePairs(stringToIntegerArray("[2,4,3,5,1]")));
        // 624975000
        TestCase tc = new TestCase("resources/Q493/Case001.txt");
        System.out.println(new Q493().reversePairs(stringToIntegerArray(tc.getData(0))));
    }

    public int reversePairs(int[] nums) {
        return merge(nums, 0, nums.length, new int[nums.length]);
    }

    int merge(int[] nums, int s, int e, int[] tmp) {
        if (s == e - 1) return 0;
        int mid = (s + e) >> 1, ret = 0;
        ret += merge(nums, s, mid, tmp);
        ret += merge(nums, mid, e, tmp);
        int l = s, r = mid;
        while (l < mid && r < e) {
            while (nums[l] <= ((long) nums[r] << 1) && l < mid) l++;
            ret += mid - l;
            r++;
        }

        int i0 = s, i1 = mid, idx = 0;
        for (; i0 < mid && i1 < e; idx++) {
            if (nums[i0] < nums[i1]) tmp[idx] = nums[i0++];
            else tmp[idx] = nums[i1++];
        }
        while (i0 < mid) tmp[idx++] = nums[i0++];
        while (i1 < e) tmp[idx++] = nums[i1++];
        System.arraycopy(tmp, 0, nums, s, e - s);
        return ret;
    }

}
