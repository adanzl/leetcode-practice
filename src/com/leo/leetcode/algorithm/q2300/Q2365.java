package com.leo.leetcode.algorithm.q2300;

import java.util.HashMap;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始的正整数数组 tasks ，表示需要 按顺序 完成的任务，其中 tasks[i] 表示第 i 件任务的 类型 。
 * 同时给你一个正整数 space ，表示一个任务完成 后 ，另一个 相同 类型任务完成前需要间隔的 最少 天数。
 * 在所有任务完成前的每一天，你都必须进行以下两种操作中的一种：
 * 1、完成 tasks 中的下一个任务
 * 2、休息一天
 * 请你返回完成所有任务所需的 最少 天数。
 * 提示：
 * 1、1 <= tasks.length <= 10^5
 * 2、1 <= tasks[i] <= 10^9
 * 3、1 <= space <= tasks.length
 * 链接：https://leetcode.cn/problems/task-scheduler-ii
 */
public class Q2365 {

    public static void main(String[] args) {
        // 9
        System.out.println(new Q2365().taskSchedulerII(stringToIntegerArray("[1,2,1,2,3,1]"), 3));
        // 6
        System.out.println(new Q2365().taskSchedulerII(stringToIntegerArray("[5,8,8,5]"), 2));
    }

    public long taskSchedulerII(int[] tasks, int space) {
        Map<Integer, Long> last = new HashMap<>();
        long ret = 0;
        for (int task : tasks) {
            long lastTs = last.getOrDefault(task, (long) Integer.MIN_VALUE);
            if (ret - lastTs < space) {
                ret = lastTs + space;
            }
            ret++;
            last.put(task, ret);
        }
        return ret;
    }
}
