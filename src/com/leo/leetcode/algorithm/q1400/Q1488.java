package com.leo.leetcode.algorithm.q1400;

import java.util.*;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 你的国家有无数个湖泊，所有湖泊一开始都是空的。当第 n 个湖泊下雨的时候，那么它就会装满水。如果第 n 个湖泊是 满的 ，这个湖泊会发生 洪水 。
 * 你的目标是避免任意一个湖泊发生洪水。
 * 给你一个整数数组 rains ，其中：
 * 1、rains[i] > 0 表示第 i 天时，第 rains[i] 个湖泊会下雨。
 * 2、rains[i] == 0 表示第 i 天没有湖泊会下雨，你可以选择 一个 湖泊并 抽干 这个湖泊的水。
 * 请返回一个数组 ans ，满足：
 * 1、ans.length == rains.length
 * 2、如果 rains[i] > 0 ，那么ans[i] == -1 。
 * 3、如果 rains[i] == 0 ，ans[i] 是你第 i 天选择抽干的湖泊。
 * 如果有多种可行解，请返回它们中的 任意一个 。如果没办法阻止洪水，请返回一个 空的数组 。
 * 请注意，如果你选择抽干一个装满水的湖泊，它会变成一个空的湖泊。但如果你选择抽干一个空的湖泊，那么将无事发生（详情请看示例 4）。
 * 提示：
 * 1、1 <= rains.length <= 10^5
 * 2、0 <= rains[i] <= 10^9
 * 链接：https://leetcode-cn.com/problems/avoid-flood-in-the-city
 */
public class Q1488 {

    public static void main(String[] args) {
        // [-1,69,1,1,-1]
        System.out.println(Arrays.toString(new Q1488().avoidFlood(stringToIntegerArray("[69,0,0,0,69]"))));
        // [-1,-1,-1,-1]
        System.out.println(Arrays.toString(new Q1488().avoidFlood(stringToIntegerArray("[1,2,3,4]"))));
        // [-1,-1,2,1,-1,-1]
        System.out.println(Arrays.toString(new Q1488().avoidFlood(stringToIntegerArray("[1,2,0,0,2,1]"))));
        // []
        System.out.println(Arrays.toString(new Q1488().avoidFlood(stringToIntegerArray("[1,2,0,1,2]"))));
    }

    public int[] avoidFlood(int[] rains) {
        int[] ans = new int[rains.length];
        Map<Integer, Integer> countData = new HashMap<>();
        TreeSet<Integer> emptyLake = new TreeSet<>();
        for (int i = 0; i < rains.length; i++) {
            if (rains[i] == 0) emptyLake.add(i);
            else {
                ans[i] = -1;
                if (countData.containsKey(rains[i])) {
                    Integer idx = emptyLake.ceiling(countData.get(rains[i]));
                    if (idx == null) return new int[0];
                    ans[idx] = rains[i];
                    emptyLake.remove(idx);
                }
                countData.put(rains[i], i);
            }
        }
        while (!emptyLake.isEmpty()) {
            Integer idx = emptyLake.pollFirst();
            if (null != idx) ans[idx] = 1;
        }
        return ans;
    }
}
