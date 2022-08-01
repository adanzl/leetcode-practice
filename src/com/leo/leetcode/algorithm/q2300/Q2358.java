package com.leo.leetcode.algorithm.q2300;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个正整数数组 grades ，表示大学中一些学生的成绩。你打算将 所有 学生分为一些 有序 的非空分组，其中分组间的顺序满足以下全部条件：
 * 1、第 i 个分组中的学生总成绩 小于 第 (i + 1) 个分组中的学生总成绩，对所有组均成立（除了最后一组）。
 * 2、第 i 个分组中的学生总数 小于 第 (i + 1) 个分组中的学生总数，对所有组均成立（除了最后一组）。
 * 返回可以形成的 最大 组数。
 * 提示：
 * 1、1 <= grades.length <= 10^5
 * 2、1 <= grades[i] <= 10^5
 * 链接：https://leetcode.cn/problems/maximum-number-of-groups-entering-a-competition
 */
public class Q2358 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q2358().maximumGroups(stringToIntegerArray("[10,6,12,7,3,5]")));
        // 1
        System.out.println(new Q2358().maximumGroups(stringToIntegerArray("[8,8]")));
    }

    public int maximumGroups(int[] grades) {
        int ans = 1, n = grades.length, sum = 1;
        while (sum + ans + 1 <= n) {
            ans++;
            sum += ans;
        }
        return ans;
    }
}
