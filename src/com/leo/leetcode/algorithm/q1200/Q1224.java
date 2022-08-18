package com.leo.leetcode.algorithm.q1200;

import java.util.HashMap;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个正整数数组 nums，请你帮忙从该数组中找出能满足下面要求的 最长 前缀，并返回该前缀的长度：
 * 从前缀中 恰好删除一个 元素后，剩下每个数字的出现次数都相同。
 * 如果删除这个元素后没有剩余元素存在，仍可认为每个数字都具有相同的出现次数（也就是 0 次）。
 * 提示：
 * 1、2 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/maximum-equal-frequency
 */
public class Q1224 {

    public static void main(String[] args) {
        // 8
        System.out.println(new Q1224().maxEqualFreq(stringToIntegerArray("[10,2,8,9,3,8,1,5,2,3,7,6]")));
        // 7
        System.out.println(new Q1224().maxEqualFreq(stringToIntegerArray("[1,1,1,2,2,2,3,3,3]")));
        // 9
        System.out.println(new Q1224().maxEqualFreq(stringToIntegerArray("[1,2,3,4,5,6,7,8,9]")));
        // 7
        System.out.println(new Q1224().maxEqualFreq(stringToIntegerArray("[2,2,1,1,5,3,3,5]")));
        // 6
        System.out.println(new Q1224().maxEqualFreq(stringToIntegerArray("[1,1,1,1,1,1]")));
        // 2
        System.out.println(new Q1224().maxEqualFreq(stringToIntegerArray("[1,1]")));
        // 2
        System.out.println(new Q1224().maxEqualFreq(stringToIntegerArray("[1,2]")));
        // 13
        System.out.println(new Q1224().maxEqualFreq(stringToIntegerArray("[1,1,1,2,2,2,3,3,3,4,4,4,5]")));
    }

    public int maxEqualFreq(int[] nums) {
        int ret = 0;
        Map<Integer, Integer> cMap = new HashMap<>(), countMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i], preCount = countMap.getOrDefault(num, 0), count = preCount + 1;
            countMap.put(num, preCount + 1);
            int preC = cMap.getOrDefault(preCount, 0);
            if (preC == 1) cMap.remove(preCount);
            else if (preC != 0) cMap.put(preCount, preC - 1);
            cMap.put(count, cMap.getOrDefault(count, 0) + 1);
            if (cMap.size() == 2) {
                Object[] ks = cMap.keySet().toArray();
                int k1 = (int) ks[0], k2 = (int) ks[1];
                if ((k1 == 1 && cMap.get(k1) == 1)
                        || (k2 == 1 && cMap.get(k2) == 1)
                        || (Math.abs(k1 - k2) == 1 && cMap.get(Math.max(k1, k2)) == 1))
                    ret = i + 1;
            } else if (cMap.size() == 1) {
                if ((int) cMap.keySet().toArray()[0] == 1 || (int) cMap.values().toArray()[0] == 1)
                    ret = i + 1;
            }
        }
        return ret;
    }
}
