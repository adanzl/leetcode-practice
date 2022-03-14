package com.leo.leetcode.algorithm.q2200;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始的整数数组 nums ，它表示一个 栈 ，其中 nums[0] 是栈顶的元素。
 * 每一次操作中，你可以执行以下操作 之一 ：
 * 如果栈非空，那么 删除 栈顶端的元素。
 * 如果存在 1 个或者多个被删除的元素，你可以从它们中选择任何一个，添加 回栈顶，这个元素成为新的栈顶元素。
 * 同时给你一个整数 k ，它表示你总共需要执行操作的次数。
 * 请你返回 恰好 执行 k 次操作以后，栈顶元素的 最大值 。如果执行完 k 次操作以后，栈一定为空，请你返回 -1 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i], k <= 10^9
 * 链接：https://leetcode-cn.com/problems/maximize-the-topmost-element-after-k-moves
 */
public class Q2202 {
    public static void main(String[] args) {
        // 2
        System.out.println(new Q2202().maximumTop(stringToIntegerArray("[0,1,2]"), 2));
        // 94
        System.out.println(new Q2202().maximumTop(stringToIntegerArray("[35,43,23,86,23,45,84,2,18,83,79,28,54,81,12,94,14,0,0,29,94,12,13,1,48,85,22,95,24,5,73,10,96,97,72,41,52,1,91,3,20,22,41,98,70,20,52,48,91,84,16,30,27,35,69,33,67,18,4,53,86,78,26,83,13,96,29,15,34,80,16,49]")
                , 15));
        // 1
        System.out.println(new Q2202().maximumTop(stringToIntegerArray("[0,1,2]"), 3));
        // -1
        System.out.println(new Q2202().maximumTop(stringToIntegerArray("[2]"), 1));
        // 0
        System.out.println(new Q2202().maximumTop(stringToIntegerArray("[0]"), 100000));
        // 3
        System.out.println(new Q2202().maximumTop(stringToIntegerArray("[3]"), 0));
        // 76
        System.out.println(new Q2202().maximumTop(stringToIntegerArray("[68,76,53,73,85,87,58,24,48,59,38,80,38,65,90,38,45,22,3,28,11]")
                , 1));
        // 96
        System.out.println(new Q2202().maximumTop(stringToIntegerArray("[73,63,62,16,95,92,93,52,89,36,75,79,67,60,42,93,93,74,94,73,35,86,96]")
                , 59));
        // 92
        System.out.println(new Q2202().maximumTop(stringToIntegerArray("[31,15,92,84,19,92,55]"), 4));
        // 96
        System.out.println(new Q2202().maximumTop(stringToIntegerArray("[73,63,62,16,95,92,93,52,89,36,75,79,67,60,42,93,93,74,94,73,35,86,96]"), 59));
        // 95
        System.out.println(new Q2202().maximumTop(stringToIntegerArray("[9,95,68,24,99]"), 5));
        // 99
        System.out.println(new Q2202().maximumTop(stringToIntegerArray("[99,95,68,24,18]"), 69));
        // 5
        System.out.println(new Q2202().maximumTop(stringToIntegerArray("[5,2,2,4,0,6]"), 4));

    }

    public int maximumTop(int[] nums, int k) {
        if (nums.length == 1) return (k & 1) == 0 ? nums[0] : -1;
        if (k <= 1) return nums[k];
        int size = Math.min(nums.length, k - 1);
        int[] arr = new int[size];
        System.arraycopy(nums, 0, arr, 0, size);
        Arrays.sort(arr);
        int v1 = arr[arr.length - 1], v2 = k <= nums.length - 1 ? nums[k] : -1;
        return Math.max(v1, v2);
    }
}
