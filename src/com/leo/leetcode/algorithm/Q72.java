package com.leo.leetcode.algorithm;

import org.junit.Test;

import java.util.HashMap;
import java.util.Map;

public class Q72 {
    @Test
    public void TestOJ() {
        System.out.println(minDistance("horse", "ros")); // 3
        System.out.println(minDistance("intention", "execution")); // 5
        System.out.println(minDistance("dinitrophenylhydrazine", "benzalphenylhydrazone")); // 7
    }

    public int minDistance(String word1, String word2) {
        return dp(new HashMap<>(), word1, word2, word1.length() - 1, word2.length() - 1);
    }

    int dp(Map<String, Integer> memMap, String w1, String w2, int i1, int i2) {
        String k = i1 + "_" + i2;
        if (memMap.containsKey(k)) return memMap.get(k);
        int ret = 0;
        if (i1 < 0) return i2 + 1;
        if (i2 < 0) return i1 + 1;
        if (w1.charAt(i1) == w2.charAt(i2)) {
            ret = dp(memMap, w1, w2, i1 - 1, i2 - 1); // same
        } else {
            ret = Math.min(dp(memMap, w1, w2, i1 - 1, i2) // w1 del
                    , Math.min(dp(memMap, w1, w2, i1, i2 - 1) // w1 add
                            , dp(memMap, w1, w2, i1 - 1, i2 - 1))) + 1; // w1 modify
        }
        memMap.put(k, ret);
        return ret;
    }

}
