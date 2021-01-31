package com.leo.leetcode.algorithm.q0300;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。
 * <p>
 * 你可以假设所有输入数组都可以得到满足题目要求的结果。
 * <p>
 * 提示：
 * <p>
 * 1、1 <= nums.length <= 5 * 10^4
 * 2、0 <= nums[i] <= 5000
 * 3、题目数据保证，对于给定的输入 nums ，总能产生满足题目要求的结果
 * <p>
 * 进阶：你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？
 * <p>
 * 链接：https://leetcode-cn.com/problems/wiggle-sort-ii
 */
public class Q324 {

    public static void main(String[] args) {
        int[] nums;
        Q324 obj = new Q324();
        // [5,6,1]
        nums = stringToIntegerArray("[5,6,1]");
        obj.wiggleSort(nums);
        System.out.println(Arrays.toString(nums));
        // [5,6,4,5]
        nums = stringToIntegerArray("[4,5,5,6]");
        obj.wiggleSort(nums);
        System.out.println(Arrays.toString(nums));
        // [3,4,2,4,2,3,1,3,1,3,1,3,1]
        nums = stringToIntegerArray("[1,4,3,4,1,2,1,3,1,3,2,3,3]");
        obj.wiggleSort(nums);
        System.out.println(Arrays.toString(nums));
        // [3,7,2,6,1,5,4]
        nums = stringToIntegerArray("[1,3,2,4,5,6,7]");
        obj.wiggleSort(nums);
        System.out.println(Arrays.toString(nums));
        // [2,3,1,3,1,2]
        nums = stringToIntegerArray("[1,3,2,2,3,1]");
        obj.wiggleSort(nums);
        System.out.println(Arrays.toString(nums));
        // [1,6,1,5,1,4]
        nums = stringToIntegerArray("[1,5,1,1,6,4]");
        obj.wiggleSort(nums);
        System.out.println(Arrays.toString(nums));

    }

    public void wiggleSort(int[] nums) {
        int[] arr = nums.clone();
        int l = 0, r = arr.length - 1, iEven = 1, iOdd = 0;
        while (l <= r) {
            int key = arr[l], pl = l, pr = r;
            while (pl < pr) {
                while (pl < pr && arr[pr] >= key) pr--;
                arr[pl] = arr[pr];
                while (pl < pr && arr[pl] <= key) pl++;
                arr[pr] = arr[pl];
            }
            arr[pl] = key;
            if (pl < arr.length / 2) l = pl + 1;
            else r = pr - 1;
        }
        int lLimit = 0, rLimit = arr.length - 1, midNum = arr[l];
        for (int i = 0; i <= rLimit; ) {
            if (arr[i] < midNum) {
                swap(arr, i, lLimit);
                lLimit++;
                i++;
            } else if (arr[i] == midNum) {
                i++;
            } else if (arr[i] > midNum) {
                swap(arr, i, rLimit);
                rLimit--;
            }
        }

        for (int i = 0; i < nums.length / 2; i++) {
            nums[iOdd] = arr[(nums.length - 1) / 2 - i];
            nums[iEven] = arr[nums.length - 1 - i];
            iEven += 2;
            iOdd += 2;
        }
        if (nums.length % 2 == 1) nums[nums.length - 1] = arr[0];
    }

    void swap(int[] arr, int i, int j) {
        int t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }
}
