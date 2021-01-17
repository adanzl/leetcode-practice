package com.leo.leetcode.algorithm.q0000;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
 * 说明：解集不能包含重复的子集。
 * 链接：https://leetcode-cn.com/problems/subsets-ii/
 */
public class Q90 {

    public static void main(String[] args) {
        System.out.println(new Q90().subsetsWithDup(new int[]{1, 2, 2})); // [[],[1],[1,2],[1,2,2],[2],[2,2]]
    }

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> out = new ArrayList<>();
        for (int i = 0; i <= nums.length; i++) {
            buildAnswer(nums, 0, i, new LinkedList<>(), out);
        }
        return out;
    }

    void buildAnswer(int[] nums, int offset, int count, LinkedList<Integer> ans, List<List<Integer>> out) {
        if (count == 0) {
            out.add(new ArrayList<>(ans));
            return;
        }
        for (int i = offset; i < nums.length; ) {
            ans.add(nums[i]);
            buildAnswer(nums, i + 1, count - 1, ans, out);
            ans.removeLast();
            i++;
            while (i > 0 && i < nums.length && nums[i] == nums[i - 1]) i++;
        }
    }
}
