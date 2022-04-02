package com.leo.leetcode.algorithm.q1500;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个 互不相同 的整数数组，其中 locations[i] 表示第 i 个城市的位置。同时给你 start，finish 和 fuel 分别表示出发城市、目的地城市和你初始拥有的汽油总量
 * 每一步中，如果你在城市 i ，你可以选择任意一个城市 j ，满足  j != i 且 0 <= j < locations.length ，并移动到城市 j 。
 * 从城市 i 移动到 j 消耗的汽油量为 |locations[i] - locations[j]|，|x| 表示 x 的绝对值。
 * 请注意， fuel 任何时刻都 不能 为负，且你 可以 经过任意城市超过一次（包括 start 和 finish ）。
 * 请你返回从 start 到 finish 所有可能路径的数目。
 * 由于答案可能很大， 请将它对 10^9 + 7 取余后返回。
 * 提示：
 * 1、2 <= locations.length <= 100
 * 2、1 <= locations[i] <= 10^9
 * 3、所有 locations 中的整数 互不相同 。
 * 4、0 <= start, finish < locations.length
 * 5、1 <= fuel <= 200
 * 链接：https://leetcode-cn.com/problems/count-all-possible-routes
 */
public class Q1575 {

    public static void main(String[] args) {
        // 5
        System.out.println(new Q1575().countRoutes(stringToIntegerArray("[4,3,1]"), 1, 0, 6));
        // 0
        System.out.println(new Q1575().countRoutes(stringToIntegerArray("[5,2,1]"), 0, 2, 3));
        // 4
        System.out.println(new Q1575().countRoutes(stringToIntegerArray("[2,3,6,8,4]"), 1, 3, 5));
    }

    public int countRoutes(int[] locations, int start, int finish, int fuel) {
        int MOD = 1_000_000_007, n = locations.length, ret = 0;
        int[][] dp = new int[n][fuel + 1];
        dp[start][0] = 1;
        for (int i = 1; i <= fuel; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    if (j == k) continue;
                    int f = Math.abs(locations[k] - locations[j]);
                    if (f <= i) dp[j][i] = (dp[j][i] + dp[k][i - f]) % MOD;
                }
            }
        }
        for (int i = 0; i <= fuel; i++) ret = (ret + dp[finish][i]) % MOD;
        return ret;
    }
}
