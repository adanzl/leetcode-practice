package com.leo.leetcode.algorithm.q1900;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums 。如果 nums 的一个子集中，所有元素的乘积可以表示为一个或多个 互不相同的质数 的乘积，那么我们称它为 好子集 。
 * 比方说，如果 nums = [1, 2, 3, 4] ：
 * [2, 3] ，[1, 2, 3] 和 [1, 3] 是 好 子集，乘积分别为 6 = 2*3 ，6 = 2*3 和 3 = 3 。
 * [1, 4] 和 [4] 不是 好 子集，因为乘积分别为 4 = 2*2 和 4 = 2*2 。
 * 请你返回 nums 中不同的 好 子集的数目对 10^9 + 7 取余 的结果。
 * nums 中的 子集 是通过删除 nums 中一些（可能一个都不删除，也可能全部都删除）元素后剩余元素组成的数组。如果两个子集删除的下标不同，那么它们被视为不同的子集。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 30
 * 链接：https://leetcode-cn.com/problems/the-number-of-good-subsets
 */
public class Q1994 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q1994().numberOfGoodSubsets(stringToIntegerArray("[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]")));
        // 8
        System.out.println(new Q1994().numberOfGoodSubsets(stringToIntegerArray("[1,1,1,2]")));
        // 5368
        System.out.println(new Q1994().numberOfGoodSubsets(stringToIntegerArray("[5,10,1,26,24,21,24,23,11,12,27,4,17,16,2,6,1,1,6,8,13,30,24,20,2,19]")));
        // 19
        System.out.println(new Q1994().numberOfGoodSubsets(stringToIntegerArray("[18,28,2,17,29,30,15,9,12]")));
        // 6
        System.out.println(new Q1994().numberOfGoodSubsets(stringToIntegerArray("[1,2,3,4]")));
        // 6
        System.out.println(new Q1994().numberOfGoodSubsets(stringToIntegerArray("[1,2,3]")));
        // 2
        System.out.println(new Q1994().numberOfGoodSubsets(stringToIntegerArray("[1,2]")));
        // 5
        System.out.println(new Q1994().numberOfGoodSubsets(stringToIntegerArray("[4,2,3,15]")));
        // 3
        System.out.println(new Q1994().numberOfGoodSubsets(stringToIntegerArray("[2,3]")));
    }

    public int numberOfGoodSubsets(int[] nums) {
        List<Integer> primeSigns = new ArrayList<>();
        List<Integer> ans = new ArrayList<>();
        int countOne = 0, MOD = 1000000007, ret;
        for (int num : nums) {
            int prime = primeSign(num);
            if (prime != 0) primeSigns.add(prime);
            if (num == 1) countOne++;
        }
        ans.add(0);
        for (Integer primeSign : primeSigns) {
            goodSubsets(ans, primeSign);
        }
        ret = ans.size() - (int)Math.pow(2, countOne);
        return ret % MOD;
    }

    int primeSign(int num) {
        if (num == 1) return 1;
        int[] prime = new int[]{2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
        int ret = 0;
        for (int i = 0; i < prime.length; ) {
            int p = prime[i];
            if (num % p == 0) {
                num /= p;
                if ((ret & 1 << (p - 1)) != 0) return 0;
                ret |= (1 << (p - 1));
            } else {
                i++;
            }
        }
        return ret;
    }


    void goodSubsets(List<Integer> ans, int v) {
        int limit = ans.size();
        for (int i = 0; i < limit; i++) {
            int pre = ans.get(i);
            if ((pre & v) == 0 || v == 1) {
                ans.add(pre | v);
            }
        }
    }
}
