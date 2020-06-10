package com.leo.leetcode.lcci;

public class Q0105 {

    public static void main(String[] args) {
        System.out.println(new Q0105().oneEditAway("dine", "ne")); // false
        System.out.println(new Q0105().oneEditAway("dinitrophenylhydrazine", "phenylhydrazine")); // false
        System.out.println(new Q0105().oneEditAway("pales", "pla")); // false
        System.out.println(new Q0105().oneEditAway("pale", "ple")); // true
    }

    public boolean oneEditAway(String first, String second) {
        char[] str1 = first.toCharArray(), str2 = second.toCharArray();
        int[][] dp = new int[str1.length + 1][];
        for (int i = 0; i < dp.length; i++) dp[i] = new int[str2.length + 1];
        for (int i = 1; i < str1.length + 1; i++) dp[i][0] = i;
        for (int i = 1; i < str2.length + 1; i++) dp[0][i] = i;
        for (int i = 1; i <= str1.length; i++) {
            for (int j = 1; j <= str2.length; j++) {
                dp[i][j] = str1[i - 1] == str2[j - 1] ? dp[i - 1][j - 1] : dp[i - 1][j - 1] + 1;
                dp[i][j] = Math.min(dp[i - 1][j] + 1, dp[i][j]);
                dp[i][j] = Math.min(dp[i][j - 1] + 1, dp[i][j]);
            }
        }
        return dp[str1.length][str2.length] <= 1;
    }
}
