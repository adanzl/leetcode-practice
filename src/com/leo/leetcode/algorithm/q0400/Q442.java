package com.leo.leetcode.algorithm.q0400;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;


import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内，且每个整数出现 一次 或 两次 。
 * 请你找出所有出现 两次 的整数，并以数组形式返回。
 * 你必须设计并实现一个时间复杂度为 O(n) 且仅使用常量额外空间的算法解决此问题。
 * 提示：
 * 1、n == nums.length
 * 2、1 <= n <= 10^5
 * 3、1 <= nums[i] <= n
 * 4、nums 中的每个元素出现 一次 或 两次
 * 链接：https://leetcode-cn.com/problems/find-all-duplicates-in-an-array
 */
public class Q442 {

    public static void main(String[] args) {
        // [2,3]
        System.out.println(new Q442().findDuplicates(stringToIntegerArray("[4,3,2,7,8,2,3,1]")));
        // [1]
        System.out.println(new Q442().findDuplicates(stringToIntegerArray("[1,1,2]")));
        // []
        System.out.println(new Q442().findDuplicates(stringToIntegerArray("[1,2]")));
    }

    public List<Integer> findDuplicates(int[] nums) {
        Set<Integer> ret = new HashSet<>();
        for (int i = 0; i < nums.length; ) {
            if (nums[i] == i + 1) {
                i++;
            } else {
                int tmp = nums[i];
                if (tmp == nums[tmp - 1]) {
                    ret.add(tmp);
                    i++;
                } else {
                    nums[i] = nums[tmp - 1];
                    nums[tmp - 1] = tmp;
                }
            }
        }
        return new ArrayList<>(ret);
    }
}
