package com.leo.leetcode.algorithm.q0000;

import com.leo.utils.LCUtil;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Q40 {
    public void TestOJ() {
        System.out.println(combinationSum2(LCUtil.stringToIntegerArray("[10,1,2,7,6,1,5]"), 8)); // [[1,1,6],[1,2,5],[1,7],[2,6]]
    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> out = new ArrayList<>();
        dfs(candidates, 0, target, null, out);
        return out;
    }

    void dfs(int[] candidates, int index, int target, List<Integer> path, List<List<Integer>> out) {
        if (path == null) path = new ArrayList<>();
        if (target == 0) {
            out.add(new ArrayList<>(path));
            return;
        }
        for (int i = 0; i < candidates.length - index; i++) {
            int v = candidates[index + i];
            if (v > target) break;
            if (i > 0 && candidates[index + i] == candidates[index + i - 1]) continue;
            path.add(v);
            dfs(candidates, index + i + 1, target - v, path, out);
            path.remove(path.size() - 1);
        }
    }
}
