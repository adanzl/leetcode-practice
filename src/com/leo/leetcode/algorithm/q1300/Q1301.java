package com.leo.leetcode.algorithm.q1300;

import java.util.Arrays;
import java.util.List;

import static com.leo.utils.LCUtil.stringToStringList;

/**
 * 给你一个正方形字符数组 board ，你从数组最右下方的字符 'S' 出发。
 * 你的目标是到达数组最左上角的字符 'E' ，数组剩余的部分为数字字符 1, 2, ..., 9 或者障碍 'X'。
 * 在每一步移动中，你可以向上、向左或者左上方移动，可以移动的前提是到达的格子没有障碍。
 * 一条路径的 「得分」 定义为：路径上所有数字的和。
 * 请你返回一个列表，包含两个整数：第一个整数是 「得分」 的最大值，第二个整数是得到最大得分的方案数，请把结果对 10^9 + 7 取余。
 * 如果没有任何路径可以到达终点，请返回 [0, 0] 。
 * 提示：2 <= board.length == board[i].length <= 100
 * 链接：https://leetcode-cn.com/problems/number-of-paths-with-max-score
 */
public class Q1301 {

    public static void main(String[] args) {
        // [0,0]
        System.out.println(Arrays.toString(new Q1301().pathsWithMaxScore(stringToStringList("[\"E11345\",\"X452XX\",\"3X43X4\",\"44X312\",\"2345XX\",\"1342XS\"]"))));
        // [0,0]
        System.out.println(Arrays.toString(new Q1301().pathsWithMaxScore(stringToStringList("[\"EX1\",\"XXX\",\"11S\"]"))));
        // [0,1]
        System.out.println(Arrays.toString(new Q1301().pathsWithMaxScore(stringToStringList("[\"EX\",\"XS\"]"))));
        // [0,0]
        System.out.println(Arrays.toString(new Q1301().pathsWithMaxScore(stringToStringList("[\"E11\",\"XXX\",\"11S\"]"))));
        // [7,1]
        System.out.println(Arrays.toString(new Q1301().pathsWithMaxScore(stringToStringList("[\"E23\",\"2X2\",\"12S\"]"))));
        // [4,2]
        System.out.println(Arrays.toString(new Q1301().pathsWithMaxScore(stringToStringList("[\"E12\",\"1X1\",\"21S\"]"))));
    }

    int MOD = 1_000_000_007;

    public int[] pathsWithMaxScore(List<String> board) {
        int n = board.size();
        int[][][] dp = new int[n][n][2];
        for (int i = n - 2; i >= 0; i--) {
            char c1 = board.get(n - 1).charAt(i), c2 = board.get(i).charAt(n - 1);
            if (c1 == 'X' || dp[n - 1][i + 1][0] == -1) dp[n - 1][i][0] = -1;
            else {
                dp[n - 1][i][0] = dp[n - 1][i + 1][0] + (c1 - '0');
                dp[n - 1][i][1] = 1;
            }
            if (c2 == 'X' || dp[i + 1][n - 1][0] == -1) dp[i][n - 1][0] = -1;
            else {
                dp[i][n - 1][0] = dp[i + 1][n - 1][0] + (c2 - '0');
                dp[i][n - 1][1] = 1;
            }
        }
        dp[n - 1][n - 1][1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--) {
                char c = board.get(i).charAt(j);
                if (c == 'X') dp[i][j][0] = -1;
                else {
                    boolean up = update(dp, i, j, i + 1, j);
                    up |= update(dp, i, j, i, j + 1);
                    up |= update(dp, i, j, i + 1, j + 1);
                    if (up) dp[i][j][0] += (c - '0');
                }
            }
        }
        if (dp[0][0][1] != 0) dp[0][0][0] -= ('E' - '0');
        return dp[0][0];
    }

    boolean update(int[][][] dp, int x1, int y1, int x2, int y2) {
        if (dp[x2][y2][1] == 0) return false;
        if (dp[x2][y2][0] > dp[x1][y1][0]) {
            dp[x1][y1][0] = dp[x2][y2][0];
            dp[x1][y1][1] = dp[x2][y2][1];
        } else if (dp[x2][y2][0] == dp[x1][y1][0]) {
            dp[x1][y1][1] = (dp[x1][y1][1] + dp[x2][y2][1]) % MOD;
        } else return false;
        return true;
    }
}
