package com.leo.leetcode.contest.q20220708;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 某连锁店开设了若干门店，门店间允许进行商品借调以应对暂时性的短缺。本月商品借调的情况记于数组 distributions，其中 distributions[i] = [from,to,num]，表示从 from 门店调配了 num 件商品给 to 门店。
 * 若要使得每一个门店最终借出和借入的商品数量相同，请问至少还需要进行多少次商品调配。
 * 注意：一次商品调配以三元组 [from, to, num] 表示，并有 from ≠ to 且 num > 0。
 * 提示：
 * 1、1 <= distributions.length <= 8
 * 2、distributions[i].length == 3
 * 3、0 <= from_i, to_i < 12
 * 4、from_i != to_i
 * 5、1 <= num_i <= 100
 * 链接：https://leetcode.cn/contest/zj-future2022/problems/NBCXIp/
 */
public class Q4 {

    public static void main(String[] args) {
        // 8
        System.out.println(new Q4().minTransfers(stringToInt2dArray("[[1,8,1],[1,0,21],[2,8,10],[3,9,20],[4,10,61],[5,11,61],[6,1,59],[7,0,60]]")));
        // 3
        System.out.println(new Q4().minTransfers(stringToInt2dArray("[[0,1,1],[1,2,1],[2,3,4],[3,4,5]]")));
        // 3
        System.out.println(new Q4().minTransfers(stringToInt2dArray("[[0,2,4],[1,2,4],[3,4,5]]")));
        // 1
        System.out.println(new Q4().minTransfers(stringToInt2dArray("[[0,1,5],[1,2,10],[2,0,5],[2,1,1]]")));
        // 0
        System.out.println(new Q4().minTransfers(stringToInt2dArray("[[0,1,5],[1,4,5],[4,0,5]]")));
    }
    // 二进制划分，状态DP
    public int minTransfers(int[][] distributions) {
        int n = 12, m = 1 << n;
        int[] remain = new int[n + 1];
        for (int[] distribution : distributions) {
            remain[distribution[0]] -= distribution[2];
            remain[distribution[1]] += distribution[2];
        }
        int[] dp = new int[m];
        for (int i = 1; i < m; i++) {
            int sum = 0;
            for (int j = 0; j < n; j++) {
                if ((i >> j & 1) != 0) sum += remain[j];
            }
            if (sum != 0) {
                dp[i] = Integer.MAX_VALUE / 2;
            } else {
                dp[i] = Integer.bitCount(i) - 1;
                // j = (j - 1) & i 快速子划分，dp[j] + dp[j ^ i]求补集
                for (int j = (i - 1) & i; j > 0; j = (j - 1) & i) {
                    dp[i] = Math.min(dp[i], dp[j] + dp[j ^ i]);
                }
            }
        }
        return dp[m - 1];
    }
}
