package com.leo.leetcode.algorithm.q2000;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums ，请你找出 nums 子集 按位或 可能得到的 最大值 ，并返回按位或能得到最大值的 不同非空子集的数目 。
 * 如果数组 a 可以由数组 b 删除一些元素（或不删除）得到，则认为数组 a 是数组 b 的一个 子集 。如果选中的元素下标位置不一样，则认为两个子集 不同 。
 * 对数组 a 执行 按位或，结果等于 a[0] OR a[1] OR ... OR a[a.length - 1]（下标从 0 开始）。
 * 提示：
 * 1、1 <= nums.length <= 16
 * 2、1 <= nums[i] <= 10^5
 * 链接：https://leetcode-cn.com/problems/count-number-of-maximum-bitwise-or-subsets
 */
public class Q2044 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q2044().countMaxOrSubsets(stringToIntegerArray("[3,1]")));
        // 7
        System.out.println(new Q2044().countMaxOrSubsets(stringToIntegerArray("[2,2,2]")));
        // 6
        System.out.println(new Q2044().countMaxOrSubsets(stringToIntegerArray("[3,2,1,5]")));
    }

    public int countMaxOrSubsets(int[] nums) {
        int max = 0, ret = 0, len = nums.length * (nums.length + 1) / 2;
        List<Integer> bitCount = new ArrayList<>(len);
        bitCount.add(0);
        for (int num : nums) {
            int size = bitCount.size();
            for (int i = 0; i < size; i++) {
                int bCount = bitCount.get(i);
                int c = num | bCount;
                if (c > max) {
                    max = c;
                    ret = 1;
                } else if (c == max) {
                    ret++;
                }
                bitCount.add(c);
            }
        }
        return ret;
    }
}
