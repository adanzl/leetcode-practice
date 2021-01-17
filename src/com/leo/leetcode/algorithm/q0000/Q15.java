package com.leo.leetcode.algorithm.q0000;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Q15 {

    public static void main(String[] args) {
        System.out.println(new Q15().threeSum(new int[]{-1, 0, 1, 2, -1, -4})); // [[-1, 0, 1],[-1, -1, 2]]
    }

    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> out = new ArrayList<>();
        if (nums.length < 3) return out;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int v1 = nums[i];
            int l = i + 1, r = nums.length - 1;
            while (l < r) {
                int t = v1 + nums[l] + nums[r];
                if (t == 0) {
                    out.add(Arrays.asList(v1, nums[l], nums[r]));
                    while (l < r && nums[l] == nums[l + 1]) l++;
                    while (l < r && nums[r] == nums[r - 1]) r--;
                    r--;
                    l++;
                } else if (t < 0) {
                    l++;
                } else {
                    r--;
                }
            }
        }
        return out;
    }
}
