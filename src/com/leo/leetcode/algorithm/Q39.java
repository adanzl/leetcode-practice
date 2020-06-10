package com.leo.leetcode.algorithm;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Q39 {
    @Test
    public void TestOJ() {
        System.out.println(combinationSum(new int[]{2, 3, 6, 7}, 7));
        System.out.println(combinationSum(new int[]{2, 3, 5}, 8));
    }

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> ret = new ArrayList<>();
        f(ret, new ArrayList<>(), candidates, target, 0);
        return ret;
    }

    void f(List<List<Integer>> out, List<Integer> temp, int[] candidates, int target, int offset) {
        for (int i = offset; i < candidates.length; i++) {
            int v = candidates[i];
            if (v == target) {
                temp.add(v);
                out.add(temp);
                break;
            } else if (v < target) {
                List<Integer> t = new ArrayList<>(temp);
                t.add(v);
                f(out, t, candidates, target - v, i);
            } else {
                break;
            }
        }
    }
}
