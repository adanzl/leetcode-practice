package com.leo.leetcode.algorithm.q1700;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。
 * 请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。
 * 返回分配方案中尽可能 最小 的 最大工作时间 。
 * 提示：
 * 1、1 <= k <= jobs.length <= 12
 * 2、1 <= jobs[i] <= 10^7
 * 链接：https://leetcode.cn/problems/find-minimum-time-to-finish-all-jobs/
 */
public class Q1723 {
    static List<List<Integer>> subsets = new ArrayList<>();

    static {
        for (int i = 0; i < 1 << 13; i++) {
            subsets.add(new ArrayList<>());
            int s = i;
            while (s > 0) {
                subsets.get(i).add(s);
                s = (s - 1) & i;
            }
        }
    }

    private int bitLength(int n) {
        int c = 0;
        while (n > 0) {
            ++c;
            n >>= 1;
        }
        return c;
    }

    public int minimumTimeRequired(int[] jobs, int k) {
        // 数位dp
        int n = jobs.length;
        // 预处理每种状态的开销
        int[] sm = new int[1 << n];
        for (int i = 1; i < 1 << n; i++) {
            int low_bit = i & -i;
            sm[i] += sm[i - low_bit] + jobs[bitLength(low_bit) - 1];
        }
        // dp[i][j] 前i个人，完成状态j的工作分配的做小开销
        // 转移方程 dp[i][j] 第i个人完成了状态s，其他人完成了状态j-s，枚举s，取最小值
        int[] dp = sm.clone();
        for (int i = 1; i < k; i++) {
            for (int j = (1 << n) - 1; j > 0; j--) {
                for (int s : subsets.get(j)) { // 遍历二进制子集
                    int v = dp[j ^ s];
                    if (sm[s] > v) v = sm[s];  //  不要用 max 和 min，那样会有额外的函数调用开销
                    if (v < dp[j]) dp[j] = v;
                }
            }
        }
        return dp[dp.length - 1];
    }

    public static void main(String[] args) {
        // 11
        System.out.println(new Q1723().minimumTimeRequired(stringToIntegerArray("[1, 2, 4, 7, 8]"), 2));
        // 3
        System.out.println(new Q1723().minimumTimeRequired(stringToIntegerArray("[3, 2, 3]"), 3));
        // 9899456
        System.out.println(new Q1723().minimumTimeRequired(stringToIntegerArray("[9899456, 8291115, 9477657, 9288480, 5146275, 7697968, 8573153, 3582365, 3758448, 9881935, 2420271, 4542202]"), 9));
    }
}
