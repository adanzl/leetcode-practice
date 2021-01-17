package com.leo.leetcode.algorithm.q0000;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
 * 使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
 * 注意：
 * 答案中不可以包含重复的四元组。
 * 链接：https://leetcode-cn.com/problems/4sum
 */
public class Q18 {
    public static void main(String[] args) {
        System.out.println(new Q18().fourSum(new int[]{1, 0, -1, 0, -2, 2}, 0)); // [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    }

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
