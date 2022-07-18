package com.leo.leetcode.algorithm.q2300;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始的数组 nums ，数组中的元素都是 正 整数。请你选出两个下标 i 和 j（i != j），且 nums[i] 的数位和 与 nums[j] 的数位和相等。
 * 请你找出所有满足条件的下标 i 和 j ，找出并返回 nums[i] + nums[j] 可以得到的 最大值 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/max-sum-of-a-pair-with-equal-sum-of-digits
 */
public class Q2342 {

    public static void main(String[] args) {
        // 54
        System.out.println(new Q2342().maximumSum(stringToIntegerArray("[18,43,36,13,7]")));
        // -1
        System.out.println(new Q2342().maximumSum(stringToIntegerArray("[10,12,19,14]")));
    }

    public int maximumSum(int[] nums) {
        Map<Integer, List<Integer>> nMap = new HashMap<>();
        int ret = -1;
        for (int num : nums) {
            int nSum = 0, nn = num;
            while (nn != 0) {
                nSum += nn % 10;
                nn /= 10;
            }
            nMap.putIfAbsent(nSum, new ArrayList<>());
            nMap.get(nSum).add(num);
        }
        for (List<Integer> l : nMap.values()) {
            if (l.size() <= 1) continue;
            l.sort((a, b) -> b - a);
            int v = l.get(0) + l.get(1);
            ret = Math.max(ret, v);
        }

        return ret;
    }
}
