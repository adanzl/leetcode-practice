package com.leo.interview;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 阿里云面试 和为零的三元组 LeetCode 15
 */
public class Interview0331 {

    public static void main(String[] args) {
        System.out.println(new Interview0331().findPair(new int[]{0, 0, 0})); // [[0, 0, 0]]
        System.out.println(new Interview0331().findPair(new int[]{0, 0})); // []
        System.out.println(new Interview0331().findPair(new int[]{-1, 0, 1, 2, -1, -4})); // [[-1, -1, 2], [-1, 0, 1]]
        System.out.println(new Interview0331().findPair(new int[]{-3, -1, 4, -2, 3, -4, 2, 1, 0})); // [[-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
        System.out.println(new Interview0331().findPair(new int[]{-1, 0, 1, 2, -1, -4})); // [[-1,-1,2],[-1,0,1]]
    }

    public List<List<Integer>> findPair(int[] nums) {
        List<List<Integer>> out = new ArrayList<>();
        if (nums.length < 3) return out;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            int v1 = nums[i];
            int l = i + 1, r = nums.length - 1;
            while (l < r) {
                int v = v1 + nums[l] + nums[r];
                if (v > 0) {
                    r--;
                } else if (v < 0) {
                    l++;
                } else {
                    List<Integer> answer = new ArrayList<>();
                    answer.add(v1);
                    answer.add(nums[l]);
                    answer.add(nums[r]);
                    out.add(answer);
                    while (l < r && nums[l] == nums[l + 1]) l++;
                    while (l < r && nums[r] == nums[r - 1]) r--;
                    l++;
                    r--;
                }
            }
        }

        return out;
    }
}
