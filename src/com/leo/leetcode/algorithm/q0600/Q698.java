package com.leo.leetcode.algorithm.q0600;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
 * 提示：
 * 1、1 <= k <= len(nums) <= 16
 * 2、0 < nums[i] < 10000
 * 3、每个元素的频率在 [1,4] 范围内
 * 链接：https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/
 */
public class Q698 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q698().canPartitionKSubsets1(stringToIntegerArray("[4,3,2,3,5,2,1]"), 4));
        // false
        System.out.println(new Q698().canPartitionKSubsets1(stringToIntegerArray("[2,2,2,2,3,4,5]"), 4));
        // true
        System.out.println(new Q698().canPartitionKSubsets1(stringToIntegerArray("[129,17,74,57,1421,99,92,285,1276,218,1588,215,369,117,153,22]"), 3));
        // false
        System.out.println(new Q698().canPartitionKSubsets(stringToIntegerArray("[1,2,3,4]"), 3));
    }

    public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum = 0, n = nums.length;
        for (int num : nums) sum += num;
        if (sum % k != 0) return false;
        int target = sum / k;
        Arrays.sort(nums);
        if (nums[n - 1] > target) return false;
        return backtrace(nums, target, new int[k], 0, new boolean[n], 0);
    }

    // 回溯
    boolean backtrace(int[] nums, int target, int[] buckets, int bIdx, boolean[] used, int idx) {
        if (bIdx == buckets.length) return true;
        for (int i = buckets[bIdx] == 0 ? 0 : idx; i < nums.length; i++) {
            if (used[i]) continue;
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;
            int bucket = buckets[bIdx] + nums[i];
            if (bucket > target) return false;
            used[i] = true;
            buckets[bIdx] += nums[i];
            if (backtrace(nums, target, buckets, bucket == target ? bIdx + 1 : bIdx, used, i + 1)) return true;
            buckets[bIdx] -= nums[i];
            used[i] = false;
        }
        return false;
    }

    // DP
    public boolean canPartitionKSubsets1(int[] nums, int k) {
        int sum = 0, n = nums.length, size = 1 << n;
        for (int num : nums) sum += num;
        if (sum % k != 0) return false;
        int target = sum / k;
        Arrays.sort(nums);
        if (nums[n - 1] > target) return false;
        boolean[] dp = new boolean[size]; // dp[i] 表示状态i是满足target的合法划分，就是多个和为target的分组，加一个小于target的组
        int[] sums = new int[size];
        dp[0] = true;
        for (int i = 0; i < size; i++) {
            if (!dp[i]) continue;
            for (int j = 0; j < n; j++) {
                if (((1 << j) & i) != 0) continue;
                int next = i | (1 << j);
                if (dp[next]) continue;
                if (sums[i] % target + nums[j] <= target) {
                    dp[next] = true;
                    sums[next] = sums[i] + nums[j];
                } else break;
            }
        }
        return dp[size - 1];
    }

}
