package com.leo.leetcode.algorithm.q2200;

import java.util.*;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 现有编号从 0 到 n - 1 的 n 个背包。给你两个下标从 0 开始的整数数组 capacity 和 rocks 。
 * 第 i 个背包最大可以装 capacity[i] 块石头，当前已经装了 rocks[i] 块石头。
 * 另给你一个整数 additionalRocks ，表示你可以放置的额外石头数量，石头可以往 任意 背包中放置。
 * 请你将额外的石头放入一些背包中，并返回放置后装满石头的背包的 最大 数量。
 * 提示：
 * 1、n == capacity.length == rocks.length
 * 2、1 <= n <= 5 * 10^4
 * 3、1 <= capacity[i] <= 10^9
 * 4、0 <= rocks[i] <= capacity[i]
 * 5、1 <= additionalRocks <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-bags-with-full-capacity-of-rocks
 */
public class Q2279 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q2279().maximumBags(stringToIntegerArray("[2,3,4,5]"), stringToIntegerArray("[1,2,4,4]"), 2));
        // 3
        System.out.println(new Q2279().maximumBags(stringToIntegerArray("[10,2,2]"), stringToIntegerArray("[2,2,0]"), 100));
    }

    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        int n = capacity.length, ret = 0;
        int[] remain = new int[n];
        for (int i = 0; i < n; i++) {
            remain[i] = capacity[i] - rocks[i];
        }
        Arrays.sort(remain);
        for (int num : remain) {
            if (additionalRocks < num) break;
            ret++;
            additionalRocks -= num;
        }
        return ret;
    }
}
