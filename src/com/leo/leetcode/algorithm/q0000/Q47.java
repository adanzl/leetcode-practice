package com.leo.leetcode.algorithm.q0000;

import com.leo.utils.LCUtil;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Q47 {

    public void TestOJ() {
        System.out.println(permuteUnique(LCUtil.stringToIntegerArray("[1,1,2]")));
    }

    public List<List<Integer>> permuteUnique(int[] nums) {
        boolean[] usedMap = new boolean[nums.length];
        Arrays.sort(nums);
        Arrays.fill(usedMap, false);
        List<List<Integer>> out = new ArrayList<>();
        dfs(nums, usedMap, null, out);
        return out;
    }

    void dfs(int[] nums, boolean[] usedMap, List<Integer> result, List<List<Integer>> out) {

        if (result == null) result = new ArrayList<>();
        if (result.size() == nums.length) {
            out.add(new ArrayList<>(result));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (usedMap[i]) continue;
            if (i > 0 && nums[i] == nums[i - 1] && !usedMap[i - 1]) continue;
            result.add(nums[i]);
            usedMap[i] = true;
            dfs(nums, usedMap, result, out);
            usedMap[i] = false;
            result.remove(result.size() - 1);
        }
    }
}
