package com.leo.leetcode.lcci;

/**
 * 你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。
 * 你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。
 * 提示：
 * 1、0 < shorter <= longer
 * 2、0 <= k <= 100000
 * 链接：https://leetcode.cn/problems/coin-lcci/
 */
public class Q0811 {

    public static void main(String[] args) {
        System.out.println(new Q0811().waysToChange(10)); // 4
        System.out.println(new Q0811().waysToChange(5)); // 2
    }

    public int waysToChange(int n) {
        long[] marks = new long[n + 1];
        marks[0] = 1;
        int[] coins = new int[]{1, 5, 10, 25};
        for (int c : coins) {
            for (int i = c; i <= n; i++) {
                marks[i] += marks[i - c];
            }
        }
        return (int) (marks[n] % 1000000007);
    }
}
