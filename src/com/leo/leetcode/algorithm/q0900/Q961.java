package com.leo.leetcode.algorithm.q0900;

import java.util.HashSet;
import java.util.Set;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组 nums ，该数组具有以下属性：
 * 1、nums.length == 2 * n.
 * 2、nums 包含 n + 1 个 不同的 元素
 * 3、nums 中恰有一个元素重复 n 次
 * 找出并返回重复了 n 次的那个元素。
 * 提示：
 * 1、2 <= n <= 5000
 * 2、nums.length == 2 * n
 * 3、0 <= nums[i] <= 10^4
 * 4、nums 由 n + 1 个 不同的 元素组成，且其中一个元素恰好重复 n 次
 * 链接：https://leetcode.cn/problems/n-repeated-element-in-size-2n-array
 */
public class Q961 {

    public static void main(String[] args) {
        //
        System.out.println(new Q961().repeatedNTimes(stringToIntegerArray("[2,6,2,1]")));
        // 3
        System.out.println(new Q961().repeatedNTimes(stringToIntegerArray("[1,2,3,3]")));
        // 2
        System.out.println(new Q961().repeatedNTimes(stringToIntegerArray("[2,1,2,5,3,2]")));
        // 5
        System.out.println(new Q961().repeatedNTimes(stringToIntegerArray("[5,1,5,2,5,3,5,4]")));
    }

    public int repeatedNTimes(int[] nums) {
        Set<Integer> found = new HashSet<>();
        for (int num : nums) {
            if (!found.add(num)) return num;
        }
        return -1;
    }
}
