package com.leo.leetcode.algorithm.q0500;


import com.leo.utils.LCUtil;

import java.util.Arrays;
import java.util.List;


/**
 * 给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。
 *
 * 提示：
 * 1、2 <= timePoints <= 2 * 10^4
 * 2、timePoints[i] 格式为 "HH:MM"
 *
 * 链接：https://leetcode-cn.com/problems/minimum-time-difference/
 */
public class Q539 {

    public static void main(String[] args) {
        // 60
        System.out.println(new Q539().findMinDifference(LCUtil.stringToStringList("[\"01:01\",\"02:01\"]")));
        // 1
        System.out.println(new Q539().findMinDifference(LCUtil.stringToStringList("[\"23:59\",\"00:00\"]")));
        // 0
        System.out.println(new Q539().findMinDifference(LCUtil.stringToStringList("[\"00:00\",\"23:58\",\"00:00\"]")));
        // 1
        System.out.println(new Q539().findMinDifference(LCUtil.stringToStringList("[\"00:00\",\"23:58\",\"23:57\",\"00:01\"]")));
    }

    public int findMinDifference(List<String> timePoints) {
        int len = timePoints.size();
        int[] values = new int[len];
        for (int i = 0; i < len; i++) {
            String str0 = timePoints.get(i);
            values[i] = (str0.charAt(0) * 10 + str0.charAt(1)) * 60 + (str0.charAt(3) * 10 + str0.charAt(4));
        }
        Arrays.sort(values);
        int ret = Integer.MAX_VALUE;
        for (int i = 0; i < len; i++) {
            int v0 = values[i];
            int v1 = values[(i + 1) % len];
            if (v1 < v0) v1 += 24 * 60;
            ret = Math.min(ret, (v1 - v0));
        }
        return ret;
    }
}
