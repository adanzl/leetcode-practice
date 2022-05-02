package com.leo.leetcode.algorithm.q6000;

import static com.leo.utils.LCUtil.stringToIntegerArray;

import java.util.*;

/**
 * 给你一个整数数组 nums 和两个整数 k 和 p ，找出并返回满足要求的不同的子数组数，要求子数组中最多 k 个可被 p 整除的元素。
 * 如果满足下述条件之一，则认为数组 nums1 和 nums2 是 不同 数组：
 * 1、两数组长度 不同 ，或者
 * 2、存在 至少 一个下标 i 满足 nums1[i] != nums2[i] 。
 * 子数组 定义为：数组中的连续元素组成的一个 非空 序列。
 * 提示：
 * 1、1 <= nums.length <= 200
 * 2、1 <= nums[i], p <= 200
 * 3、1 <= k <= nums.length
 * 链接：https://leetcode-cn.com/problems/k-divisible-elements-subarrays
 */
public class Q2261 {

    public static void main(String[] args) {
        // 15
        System.out.println(new Q2261().countDistinct(stringToIntegerArray("[1,9,8,7,19]"), 1, 6));
        // 10
        System.out.println(new Q2261().countDistinct(stringToIntegerArray("[1,2,3,4]"), 4, 1));
        // 11
        System.out.println(new Q2261().countDistinct(stringToIntegerArray("[2,3,3,2,2]"), 2, 2));
    }

    public int countDistinct(int[] nums, int k, int p) {
        int n = nums.length;
        int[] preScore = new int[n + 1];
        for (int i = 1; i <= n; i++) preScore[i] = preScore[i - 1] + (nums[i - 1] % p == 0 ? 1 : 0);
        Map<String, Integer> cMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            StringBuilder key = new StringBuilder();
            key.append(nums[i]);
            for (int j = i; j < n; j++) {
                if (i != j) key.append("_").append(nums[j]);
                if (cMap.containsKey(key.toString())) continue;
                int count = preScore[j + 1] - preScore[i];
                if (count > k) continue;
                cMap.put(key.toString(), count);
            }
        }
        return cMap.size() ;
    }
}
