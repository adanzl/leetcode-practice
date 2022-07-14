package com.leo.leetcode.algorithm.q0400;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。
 * 如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该序列为等差序列。
 * 1、例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。
 * 2、再例如，[1, 1, 2, 5, 7] 不是等差序列。
 * 数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。
 * 例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
 * 题目数据保证答案是一个 32-bit 整数。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、-2^31 <= nums[i] <= 2^31 - 1
 * 链接：https://leetcode.cn/problems/arithmetic-slices-ii-subsequence
 */
public class Q446 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q446().numberOfArithmeticSlices(stringToIntegerArray("[0,2000000000,-294967296]")));
        // 16
        System.out.println(new Q446().numberOfArithmeticSlices(stringToIntegerArray("[7,7,7,7,7]")));
        // 7
        System.out.println(new Q446().numberOfArithmeticSlices(stringToIntegerArray("[2,4,6,8,10]")));
    }

    public int numberOfArithmeticSlices(int[] nums) {
        int n = nums.length, ret = 0;
        List<Map<Long, Integer>> mMap = new ArrayList<>(n); // endIdx-dela-count
        for (int i = 0; i < n; i++) {
            Map<Long, Integer> curMap = new HashMap<>();
            mMap.add(curMap);
            for (int j = 0; j < i; j++) {
                Map<Long, Integer> preMap = mMap.get(j);
                long dela = (long) nums[i] - nums[j];
                int cnt = preMap.getOrDefault(dela, 0);
                ret += cnt;
                curMap.put(dela, curMap.getOrDefault(dela, 0) + cnt + 1);
            }
        }
        return ret;
    }
}
