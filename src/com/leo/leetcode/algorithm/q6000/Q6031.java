package com.leo.leetcode.algorithm.q6000;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始的整数数组 nums 和两个整数 key 和 k 。K 近邻下标 是 nums 中的一个下标 i ，并满足至少存在一个下标 j 使得 |i - j| <= k 且 nums[j] == key 。
 * 以列表形式返回按 递增顺序 排序的所有 K 近邻下标。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、1 <= nums[i] <= 1000
 * 3、key 是数组 nums 中的一个整数
 * 4、1 <= k <= nums.length
 * 链接：https://leetcode-cn.com/problems/find-all-k-distant-indices-in-an-array
 */

public class Q6031 {

    public static void main(String[] args) {
        // [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
        System.out.println(new Q6031().findKDistantIndices(stringToIntegerArray("[734,228,636,204,552,732,686,461,973,874,90,537,939,986,855,387,344,939,552,389,116,93,545,805,572,306,157,899,276,479,337,219,936,416,457,612,795,221,51,363,667,112,686,21,416,264,942,2,127,47,151,277,603,842,586,630,508,147,866,434,973,216,656,413,504,360,990,228,22,368,660,945,99,685,28,725,673,545,918,733,158,254,207,742,705,432,771,578,549,228,766,998,782,757,561,444,426,625,706,946]")
                , 939, 34));
        // [1,2,3,4,5,6]
        System.out.println(new Q6031().findKDistantIndices(stringToIntegerArray("[3,4,9,1,3,9,5]"), 9, 1));
        // [0,1,2,3,4]
        System.out.println(new Q6031().findKDistantIndices(stringToIntegerArray("[2,2,2,2,2]"), 2, 2));
    }

    public List<Integer> findKDistantIndices(int[] nums, int key, int k) {
        List<Integer> ret = new ArrayList<>();
        int left = -1, right = nums.length - 1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == key) {
                for (int j = Math.max(left + 1, i - k); j <= Math.min(i + k, right); j++) {
                    if (j < nums.length) {
                        ret.add(j);
                        left = Math.max(left, j);
                    }
                }
            }
        }
        return ret;
    }
}
