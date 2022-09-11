package com.leo.leetcode.algorithm.q2300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

import java.util.*;

/**
 * 给你一个下标从 0 开始的整数数组 nums ，判断是否存在 两个 长度为 2 的子数组且它们的 和 相等。注意，这两个子数组起始位置的下标必须 不相同 。
 * 如果这样的子数组存在，请返回 true，否则返回 false 。
 * 子数组 是一个数组中一段连续非空的元素组成的序列。
 * 提示：
 * 1、2 <= nums.length <= 1000
 * 2、-10^9 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/find-subarrays-with-equal-sum
 */
public class Q2395 {
    public static void main(String[] args) {
        // true
        System.out.println(new Q2395().findSubarrays(stringToIntegerArray("[4,2,4]")));
        // false
        System.out.println(new Q2395().findSubarrays(stringToIntegerArray("[1,2,3,4,5]")));
        // true
        System.out.println(new Q2395().findSubarrays(stringToIntegerArray("[0,0,0]")));
    }

    public boolean findSubarrays(int[] nums) {
        Set<Integer> cMap = new HashSet<>();
        int n = nums.length;
        for (int i = 1; i < n; i++) {
            int v = nums[i - 1] + nums[i];
            if (cMap.contains(v)) return true;
            cMap.add(v);
        }
        return false;
    }
}
