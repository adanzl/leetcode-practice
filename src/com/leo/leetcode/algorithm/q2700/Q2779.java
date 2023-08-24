package com.leo.leetcode.algorithm.q2700;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始的整数数组 nums 和一个 非负 整数 k 。
 * 在一步操作中，你可以执行下述指令：
 * 1、在范围 [0, nums.length - 1] 中选择一个 此前没有选过 的下标 i 。
 * 2、将 nums[i] 替换为范围 [nums[i] - k, nums[i] + k] 内的任一整数。
 * 数组的 美丽值 定义为数组中由相等元素组成的最长子序列的长度。
 * 对数组 nums 执行上述操作任意次后，返回数组可能取得的 最大 美丽值。
 * 注意：你 只 能对每个下标执行 一次 此操作。
 * 数组的 子序列 定义是：经由原数组删除一些元素（也可能不删除）得到的一个新数组，且在此过程中剩余元素的顺序不发生改变。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i], k <= 10^5
 * 链接：https://leetcode.cn/problems/maximum-beauty-of-an-array-after-applying-operation/
 */
public class Q2779 {

    public int maximumBeauty(int[] nums, int k) {
        int ans = 0;
        int l = 0, r = 0;
        Arrays.sort(nums);
        while (r < nums.length) {
            while (l < r && nums[r] - nums[l] > k * 2) l++;
            ans = Math.max(ans, r - l + 1);
            r++;
        }
        return ans;
    }

    public static void main(String[] args) {
        // 3
        System.out.println(new Q2779().maximumBeauty(stringToIntegerArray("[48,93,96,19]"), 24));
        // 3
        System.out.println(new Q2779().maximumBeauty(stringToIntegerArray("[4,6,1,2]"), 2));
        // 4
        System.out.println(new Q2779().maximumBeauty(stringToIntegerArray("[1,1,1,1]"), 10));
    }
}
