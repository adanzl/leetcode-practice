package com.leo.leetcode.algorithm.q2200;

import java.util.HashMap;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始的整数数组 tasks ，其中 tasks[i] 表示任务的难度级别。在每一轮中，你可以完成 2 个或者 3 个 相同难度级别 的任务。
 * 返回完成所有任务需要的 最少 轮数，如果无法完成所有任务，返回 -1 。
 * 提示：
 * 1、1 <= tasks.length <= 10^5
 * 2、1 <= tasks[i] <= 10^9
 * 链接：https://leetcode-cn.com/problems/minimum-rounds-to-complete-all-tasks
 */
public class Q2244 {

    public static void main(String[] args) {
        // 4
        System.out.println(new Q2244().minimumRounds(stringToIntegerArray("[2,2,3,3,2,4,4,4,4,4]")));
        // -1
        System.out.println(new Q2244().minimumRounds(stringToIntegerArray("[2,3,3]")));
    }

    public int minimumRounds(int[] tasks) {
        Map<Integer, Integer> cMap = new HashMap<>();
        int ret = 0;
        for (int task : tasks) {
            cMap.put(task, cMap.getOrDefault(task, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : cMap.entrySet()) {
            int c = entry.getValue();
            if (c < 2) return -1;
            ret += c / 3;
            if (c % 3 != 0) ret++;
        }
        return ret;
    }
}
