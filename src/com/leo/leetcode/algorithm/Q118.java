package com.leo.leetcode.algorithm;

import java.util.ArrayList;
import java.util.List;

public class Q118 {

    public static void main(String[] args) {
        System.out.println(new Q118().generate(5)); // [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        System.out.println(new Q118().generate(0)); // []
    }

    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> out = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            List<Integer> ans = new ArrayList<>(i + 1);
            ans.add(1);
            out.add(ans);
            if (i == 0) continue;
            List<Integer> pre = out.get(i - 1);
            for (int j = 0; j < i - 1; j++) ans.add(pre.get(j) + pre.get(j + 1));
            ans.add(1);
        }
        return out;
    }
}
