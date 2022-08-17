package com.leo.leetcode.algorithm.q2300;

import java.util.HashMap;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始的整数数组 nums 。如果 i < j 且 j - i != nums[j] - nums[i] ，那么我们称 (i, j) 是一个 坏数对 。
 * 请你返回 nums 中 坏数对 的总数目。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/count-number-of-bad-pairs
 */
public class Q2364 {

    public static void main(String[] args) {
        // 5
        System.out.println(new Q2364().countBadPairs(stringToIntegerArray("[4,1,3,3]")));
        // 0
        System.out.println(new Q2364().countBadPairs(stringToIntegerArray("[1,2,3,4,5]")));
        // 5
        System.out.println(new Q2364().countBadPairs(stringToIntegerArray("[1,2,3,4,5,1]")));
    }

    public long countBadPairs(int[] nums) {
        long ret = 0, sum = 0;
        Map<Integer, Integer> m = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int v = nums[i] - i;
            ret += sum - m.getOrDefault(v, 0);
            sum++;
            m.put(v, m.getOrDefault(v, 0) + 1);
        }
        return ret;
    }
}
