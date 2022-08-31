package com.leo.leetcode.algorithm.q6000;

import java.util.*;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个长度为 n 的整数数组 nums ，和一个长度为 m 的整数数组 queries 。
 * 返回一个长度为 m 的数组 answer ，其中 answer[i] 是 nums 中 元素之和小于等于 queries[i] 的 子序列 的 最大 长度 。
 * 子序列 是由一个数组删除某些元素（也可以不删除）但不改变剩余元素顺序得到的一个数组。
 * 提示：
 * 1、n == nums.length
 * 2、m == queries.length
 * 3、1 <= n, m <= 1000
 * 4、1 <= nums[i], queries[i] <= 10^6
 * 链接：https://leetcode.cn/problems/longest-subsequence-with-limited-sum
 */
public class Q2389 {

    public static void main(String[] args) {
        // [2,3,4]
        System.out.println(Arrays.toString(new Q2389().answerQueries(stringToIntegerArray("[4,5,2,1]"), stringToIntegerArray("[3,10,21]"))));
        // [0]
        System.out.println(Arrays.toString(new Q2389().answerQueries(stringToIntegerArray("[2,3,4,5]"), stringToIntegerArray("[1]"))));
    }

    public int[] answerQueries(int[] nums, int[] queries) {
        Arrays.sort(nums);
        int n = nums.length, m = queries.length;
        long[] preSum = new long[n + 1];
        for (int i = 0; i < n; i++) preSum[i + 1] = preSum[i] + nums[i];
        int[] ans = new int[m];
        for (int i = 0; i < m; i++) {
            int l = 0, r = n;
            while (l <= r) {
                int mid = l + (r - l) / 2;
                if (preSum[mid] <= queries[i]) {
                    ans[i] = mid;
                    l = mid + 1;
                } else r = mid - 1;
            }
        }
        return ans;
    }


}
