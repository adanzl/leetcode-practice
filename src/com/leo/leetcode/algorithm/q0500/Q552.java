package com.leo.leetcode.algorithm.q0500;

/**
 * 可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
 * 1、'A'：Absent，缺勤
 * 2、'L'：Late，迟到
 * 3、'P'：Present，到场
 * 如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
 * 1、按 总出勤 计，学生缺勤（'A'）严格 少于两天。
 * 2、学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。
 * 给你一个整数 n ，表示出勤记录的长度（次数）。请你返回记录长度为 n 时，可能获得出勤奖励的记录情况 数量 。答案可能很大，所以返回对 10^9 + 7 取余 的结果。
 * 提示：1 <= n <= 10^5
 * 链接：https://leetcode.cn/problems/student-attendance-record-ii
 */
public class Q552 {

    public static void main(String[] args) {
        // 8
        System.out.println(new Q552().checkRecord(2));
        // 3
        System.out.println(new Q552().checkRecord(1));
        // 183236316
        System.out.println(new Q552().checkRecord(10101));
    }

    public int checkRecord(int n) {
        int MOD = 1_000_000_007;
        long ret = 0;
        long[][] dp = new long[][]{{0, 1, 1, 0}, {1, 0, 0, 0}};
        // A[0]-A[1]
        // A: 0
        // P: 1
        // L: 2
        // LL: 3
        for (int i = 1; i < n; i++) {
            long[][] newDp = new long[2][4];
            newDp[0][1] = (dp[0][1] + dp[0][2] + dp[0][3]) % MOD; // P
            newDp[0][2] = (dp[0][1]) % MOD; // L
            newDp[0][3] = (dp[0][2]) % MOD; // LL
            newDp[1][0] = (dp[0][1] + dp[0][2] + dp[0][3]) % MOD; // A
            newDp[1][1] = (dp[1][0] + dp[1][1] + dp[1][2] + dp[1][3]) % MOD; // P
            newDp[1][2] = (dp[1][0] + dp[1][1]) % MOD; // L
            newDp[1][3] = (dp[1][2]) % MOD; // LL
            dp = newDp;
        }
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 4; j++) {
                ret = (ret + dp[i][j]) % MOD;
            }
        }
        return (int) (ret % MOD);
    }
}
