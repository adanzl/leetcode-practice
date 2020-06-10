package com.leo.leetcode.algorithm;

import java.util.ArrayList;
import java.util.List;

public class Q78 {
    public void TestOJ() {
        System.out.println(subsets(new int[]{1, 2, 3}));
    }

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ret = new ArrayList<>();
        ret.add(new ArrayList<>());
        for (int num : nums) {
            buildSet(ret, num);
        }

        return ret;
    }

    void buildSet(List<List<Integer>> out, int v) {
        int limit = out.size();
        for (int i = 0; i < limit; i++) {

            List<Integer> newNode = new ArrayList<>(out.get(i));
            newNode.add(v);
            out.add(newNode);
        }
    }
}
