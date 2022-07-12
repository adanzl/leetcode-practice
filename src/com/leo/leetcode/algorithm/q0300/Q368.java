package com.leo.leetcode.algorithm.q0300;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
 * 1、answer[i] % answer[j] == 0 ，或
 * 2、answer[j] % answer[i] == 0
 * 如果存在多个有效解子集，返回其中任何一个均可。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、1 <= nums[i] <= 2 * 10^9
 * 3、nums 中的所有整数 互不相同
 * 链接：https://leetcode.cn/problems/largest-divisible-subset
 */
public class Q368 {

    public static void main(String[] args) {
        // [1,2]
        System.out.println(new Q368().largestDivisibleSubset(stringToIntegerArray("[1,2,3]")));
        // [1,2,4,8]
        System.out.println(new Q368().largestDivisibleSubset(stringToIntegerArray("[1,2,4,8]")));
        // [9,18,90,180,360,720]
        System.out.println(new Q368().largestDivisibleSubset(stringToIntegerArray("[9,18,54,90,108,180,360,540,720]")));
    }

    public List<Integer> largestDivisibleSubset(int[] nums) {
        List<Integer> res = new ArrayList<>();
        Arrays.sort(nums);
        int n = nums.length, max = 0, maxIdx = -1;
        int[] pre = new int[n], dp = new int[n];
        Arrays.fill(pre, -1);
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            dp[i] = 1;
            for (int j = i - 1; j >= 0; j--) {
                if (num % nums[j] == 0) {
                    if (dp[j] + 1 > dp[i]) {
                        dp[i] = dp[j] + 1;
                        pre[i] = j;
                    }
                }
            }
            if (dp[i] > max) {
                max = dp[i];
                maxIdx = i;
            }
        }
        while (maxIdx >= 0) {
            res.add(nums[maxIdx]);
            maxIdx = pre[maxIdx];
        }
        Collections.reverse(res);
        return res;
    }
}
