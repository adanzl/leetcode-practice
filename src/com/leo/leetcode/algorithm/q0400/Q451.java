package com.leo.leetcode.algorithm.q0400;

import java.util.*;

/**
 * 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
 * 链接：https://leetcode-cn.com/problems/sort-characters-by-frequency/
 */
public class Q451 {
    public static void main(String[] args) {
        // "eert"
        System.out.println(new Q451().frequencySort("tree"));
        // "aaaccc"
        System.out.println(new Q451().frequencySort("cccaaa"));
        // "bbAa"
        System.out.println(new Q451().frequencySort("Aabb"));
    }

    public String frequencySort(String s) {
        Map<Character, Integer> m = new HashMap<>();
        StringBuilder ret = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            m.put(c, m.getOrDefault(c, 0) + 1);
        }
        PriorityQueue<int[]> q = new PriorityQueue<>((o1, o2) -> o2[1] - o1[1]);
        for (Map.Entry<Character, Integer> it : m.entrySet()) {
            q.add(new int[]{it.getKey(), it.getValue()});
        }
        while (!q.isEmpty()) {
            int[] p = q.poll();
            while (p[1]-- > 0) {
                ret.append((char) p[0]);
            }
        }
        return ret.toString();
    }
}
