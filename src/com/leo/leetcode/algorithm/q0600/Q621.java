package com.leo.leetcode.algorithm.q0600;

import java.util.Arrays;

/**
 * 给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。
 * 任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。
 * 然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
 * 你需要计算完成所有任务所需要的 最短时间 。
 * <p>
 * 提示：
 * 1、1 <= task.length <= 104
 * 2、tasks[i] 是大写英文字母
 * 3、n 的取值范围为 [0, 100]
 * <p>
 * 链接：https://leetcode-cn.com/problems/task-scheduler
 */
public class Q621 {
    public static void main(String[] args) {
        // 8
        System.out.println(new Q621().leastInterval(new char[]{'A', 'A', 'A', 'B', 'B', 'B'}, 2));
        // 1
        System.out.println(new Q621().leastInterval(new char[]{'A'}, 2));
    }

    private int leastInterval(char[] tasks, int n) {
        int[] flag = new int[26];
        for (char c : tasks) flag[c - 'A']++;
        Arrays.sort(flag);
        int count = (flag[25] - 1) * n;
        for (int i = 24; i >= 0; i--) {
            if (flag[i] == flag[25]) count -= flag[25] - 1;
            else count -= flag[i];
            if (count < 0) return tasks.length;
        }
        return count + tasks.length;
    }
}
