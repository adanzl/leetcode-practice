package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Q207 {

    public static void main(String[] args) {
        new Q207().TestOJ();
    }

    public void TestOJ() {
        System.out.println(canFinish(2, LCUtil.stringToInt2dArray("[[1,0]]"))); // t
        System.out.println(canFinish(2, LCUtil.stringToInt2dArray("[[1,0],[0,1]]"))); // f
        System.out.println(canFinish(2, LCUtil.stringToInt2dArray("[]"))); // t
        System.out.println(canFinish(4, LCUtil.stringToInt2dArray("[[0,1],[3,1],[1,3],[3,2]]"))); // f
    }

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, Set<Integer>> pMap = new HashMap<>();
        for (int[] prerequisite : prerequisites) {
            int k = prerequisite[0];
            Set<Integer> l = pMap.computeIfAbsent(k, k1 -> new HashSet<>());
            l.add(prerequisite[1]);
        }

        for (int i = 0; i < numCourses; i++) {
            if (isLoop(pMap, i, i, new HashSet<>())) {
                return false;
            }
        }

        return true;
    }

    boolean isLoop(Map<Integer, Set<Integer>> pMap, int key, int fastSuc, Set<Integer> s) {
        if (s.contains(key)) return true;
        if (key < fastSuc) return false;
        Set<Integer> l = pMap.get(key);
        if (l == null) {
            return false;
        }
        s.add(key);
        for (int k : l) {
            if (isLoop(pMap, k, fastSuc, s)) return true;
        }
        s.remove(key);
        return false;
    }
}
