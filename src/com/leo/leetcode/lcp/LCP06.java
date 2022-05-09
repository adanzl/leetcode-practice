package com.leo.leetcode.lcp;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。
 * 限制：
 * 1、1 <= n <= 4
 * 1、1 <= coins[i] <= 10
 * 链接：https://leetcode.cn/problems/na-ying-bi
 */
public class LCP06 {

    public static void main(String[] args) {
        // 4
        System.out.println(new LCP06().minCount(stringToIntegerArray("[4,2,1]")));
        // 8
        System.out.println(new LCP06().minCount(stringToIntegerArray("[2,3,10]")));
    }

    public int minCount(int[] coins) {
        int ret = 0;
        for (int coin : coins) {
            ret += coin / 2 + coin % 2;
        }
        return ret;
    }
}
