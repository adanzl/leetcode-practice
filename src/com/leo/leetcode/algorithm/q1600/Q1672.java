package com.leo.leetcode.algorithm.q1600;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个 m x n 的整数网格 accounts ，其中 accounts[i][j] 是第 i 位客户在第 j 家银行托管的资产数量。返回最富有客户所拥有的 资产总量 。
 * 客户的 资产总量 就是他们在各家银行托管的资产数量之和。最富有客户就是 资产总量 最大的客户。
 * 提示：
 * 1、m == accounts.length
 * 2、n == accounts[i].length
 * 3、1 <= m, n <= 50
 * 4、1 <= accounts[i][j] <= 100
 * 链接：https://leetcode-cn.com/problems/richest-customer-wealth
 */
public class Q1672 {

    public static void main(String[] args) {
        // 6
        System.out.println(new Q1672().maximumWealth(stringToInt2dArray("[[1,2,3],[3,2,1]]")));
        // 10
        System.out.println(new Q1672().maximumWealth(stringToInt2dArray("[[1,5],[7,3],[3,5]]")));
        // 17
        System.out.println(new Q1672().maximumWealth(stringToInt2dArray("[[2,8,7],[7,1,3],[1,9,5]]")));
        //
        System.out.println(new Q1672().maximumWealth(stringToInt2dArray("[]")));
    }

    public int maximumWealth(int[][] accounts) {
        int ret = 0;
        for (int[] account : accounts) {
            int sum = 0;
            for (int v : account) sum += v;
            ret = Math.max(ret, sum);
        }
        return ret;
    }
}
