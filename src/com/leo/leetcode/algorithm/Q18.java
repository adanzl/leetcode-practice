package com.leo.leetcode.algorithm;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Q18 {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> out = new ArrayList<>();

        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int v1 = nums[i];
            for (int j = i + 1; j < nums.length - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                int v2 = nums[j];
                int l = j + 1, r = nums.length - 1;
                while (l < r) {
                    int sum = v1 + v2 + nums[l] + nums[r];
                    if (sum == target) {
                        List<Integer> answer = new ArrayList<>();
                        answer.add(v1);
                        answer.add(v2);
                        answer.add(nums[l]);
                        answer.add(nums[r]);
                        out.add(answer);
                        while (l < r && nums[l] == nums[l + 1]) l++;
                        while (l < r && nums[r] == nums[r - 1]) r--;
                        l++;
                        r--;
                    } else if (sum < target) {
                        l++;
                    } else {
                        r--;
                    }
                }
            }
        }
        return out;
    }
}
