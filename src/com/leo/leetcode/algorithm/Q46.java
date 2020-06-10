package com.leo.leetcode.algorithm;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Q46 {
    public void TestOJ() {
        // System.out.println(permute(new int[]{1, 2, 3, 6}));
        System.out.println(permute(new int[]{1, 2, 3,}));
    }

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> out = new ArrayList<>();
        build(nums, 0, out);
        return out;
    }

    void build(int[] nums, int offset, List<List<Integer>> out) {
        if (offset == nums.length - 1) {
            out.add(Arrays.stream(nums).boxed().collect(Collectors.toList()));
            return;
        }
        for (int i = offset; i < nums.length; i++) {
            swap(nums, offset, i);
            build(nums, offset + 1, out);
            swap(nums, offset, i);
        }
    }

    void swap(int[] nums, int l, int r) {
        int t = nums[l];
        nums[l] = nums[r];
        nums[r] = t;
    }

    // public List<List<Integer>> permute(int[] nums) {
    // List<List<Integer>> ret = new ArrayList<>();
    // ret.add(arr2List(nums));
    // doChange(ret, nums, 0);
    // return ret;
    // }
    //
    // void doChange(List<List<Integer>> out, int[] nums, int index) {
    // if (index >= nums.length) return;
    // for (int i = index; i < nums.length; i++) {
    // int j = i + 1;
    // while (j < nums.length) {
    // int[] tn = Arrays.copyOf(nums, nums.length);
    // int t = tn[i];
    // tn[i] = tn[j];
    // tn[j] = t;
    // out.add(arr2List(tn));
    // doChange(out, tn, i + 1);
    // j++;
    // }
    // }
    // }
    //
    // List<Integer> arr2List(int[] arr) {
    // List<Integer> ret = new ArrayList<>();
    // for (int i : arr) {
    // ret.add(i);
    // }
    // return ret;
    // }
}
