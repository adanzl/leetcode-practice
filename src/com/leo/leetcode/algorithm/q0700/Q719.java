package com.leo.leetcode.algorithm.q0700;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。
 * 提示:
 * 1、2 <= len(nums) <= 10000.
 * 2、0 <= nums[i] < 1000000.
 * 3、1 <= k <= len(nums) * (len(nums) - 1) / 2.
 * 链接：https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance
 */
public class Q719 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q719().smallestDistancePair(stringToIntegerArray("[1,3,1,1]"), 4));
        // 2
        System.out.println(new Q719().smallestDistancePair(stringToIntegerArray("[1,3,1,1]"), 5));
        // 2
        System.out.println(new Q719().smallestDistancePair(stringToIntegerArray("[1,3,1,1]"), 6));
        // 0
        System.out.println(new Q719().smallestDistancePair(stringToIntegerArray("[1,3,1]"), 1));
        // 0
        System.out.println(new Q719().smallestDistancePair(stringToIntegerArray("[1,3,1,1]"), 2));
        // 1
        System.out.println(new Q719().smallestDistancePair(stringToIntegerArray("[1,3,1,1,4]"), 4));
    }

    public int smallestDistancePair(int[] nums, int k) {
        Arrays.sort(nums);
        int l = 0, r = nums[nums.length - 1] - nums[0];
        while (l <= r) {
            int mid = l + ((r - l) >> 1);
            int count = getKCount(nums, mid);
            if (count < k) l = mid + 1;
            else r = mid - 1;
        }
        return l;
    }

    int getKCount(int[] nums, int k) {
        int count = 0;
        for (int l = 0, r = l ; r < nums.length; r++) {
            while (nums[r] - nums[l] > k) l++;
            count += r - l ;
        }
        return count;
    }
}
