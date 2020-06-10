package com.leo.leetcode.algorithm;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Q15 {
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
                    List<Integer> answer = new ArrayList<>();
                    answer.add(v1);
                    answer.add(nums[l]);
                    answer.add(nums[r]);
                    out.add(answer);
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
