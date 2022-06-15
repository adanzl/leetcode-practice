package com.leo.leetcode.algorithm.q2100;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始的数组 nums ，该数组由 n 个正整数组成。
 * 如果满足下述条件，则数组 nums 是一个 交替数组 ：
 * 1、nums[i - 2] == nums[i] ，其中 2 <= i <= n - 1 。
 * 2、nums[i - 1] != nums[i] ，其中 1 <= i <= n - 1 。
 * 在一步 操作 中，你可以选择下标 i 并将 nums[i] 更改 为 任一 正整数。
 * 返回使数组变成交替数组的 最少操作数 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/minimum-operations-to-make-the-array-alternating
 */

public class Q2170 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q2170().minimumOperations(stringToIntegerArray("[3,1,3,2,4,3]")));
        // 2
        System.out.println(new Q2170().minimumOperations(stringToIntegerArray("[1,2,2,2,2]")));
    }

    public int minimumOperations(int[] nums) {
        int n = nums.length, len1 = (n >> 1) + (n & 1), len2 = n >> 1;
        int[][] flag1 = new int[100001][2], flag2 = new int[1000001][2];
        for (int i = 0; i < 100001; i++) flag1[i][0] = flag2[i][0] = i;
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            if ((i & 1) == 0) flag1[num][1]++;
            else flag2[num][1]++;
        }
        Arrays.sort(flag1, (a, b) -> b[1] - a[1]);
        Arrays.sort(flag2, (a, b) -> b[1] - a[1]);
        int ret = 0;
        if (flag1[0][0] != flag2[0][0]) ret += len1 - flag1[0][1] + len2 - flag2[0][1];
        else ret += Math.min(len1 - flag1[0][1] + len2 - flag2[1][1], len1 - flag1[1][1] + len2 - flag2[0][1]);
        return ret;
    }
}
