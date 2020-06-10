package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import org.junit.Test;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Q128 {
    @Test
    public void TestOJ() {
        System.out.println(longestConsecutive(LCUtil.stringToIntegerArray("[1,3,5,2,4]"))); // 5
        System.out.println(longestConsecutive(LCUtil.stringToIntegerArray("[1,2,0,1]"))); // 3
        System.out.println(longestConsecutive(LCUtil.stringToIntegerArray("[100, 4, 200, 1, 3, 2]"))); // 4
        System.out.println(longestConsecutive(LCUtil.stringToIntegerArray("[0,0,1,-1]"))); // 3
    }

    public int longestConsecutive(int[] nums) {
        int ret = 0;
        Map<Integer, Integer> lenMap = new HashMap<>(nums.length);
        for (int v : nums) {
            if (!lenMap.containsKey(v)) {
                int lenVL = lenMap.getOrDefault(v - 1, 0);
                int lenVR = lenMap.getOrDefault(v + 1, 0);
                int len = lenVL + lenVR + 1;
                lenMap.put(v, len);
                lenMap.put(v + lenVR, len);
                lenMap.put(v - lenVL, len);
                ret = Math.max(ret, len);
            }
        }
        return ret;
    }

    public int longestConsecutive1(int[] nums) {
        int ret = 0;
        Set<Integer> num_set = new HashSet<>();
        for (int num : nums) num_set.add(num);
        for (int num : num_set) {
            if (!num_set.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;
                while (num_set.contains(currentNum + 1)) {
                    currentNum++;
                    currentStreak++;
                }
                ret = Math.max(ret, currentStreak);
            }
        }

        return ret;
    }
}
