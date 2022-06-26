package com.leo.leetcode.contest.q20220626;

import java.util.*;

/**
 * 链接：https://leetcode.cn/contest/sf-tech/problems/EUpcmh/
 */
public class Q1 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q1().hasCycle("1->1,1->3,2->6,3->4,3->5,3->6,4->5,4->6"));
        // true
        System.out.println(new Q1().hasCycle("1->4,2->5,3->6,3->7,4->8,5->8,5->9,6->9,6->11,7->11,8->12,9->12,9->13,10->6,10->13,10->14,11->10,11->14"));
        // false
        System.out.println(new Q1().hasCycle("1->4,2->5,3->6,3->7,4->8,5->8,5->9,6->9,6->11,7->11,8->12,9->12,9->13,10->13,10->14,11->10,11->14"));
        // true
        System.out.println(new Q1().hasCycle("1->2,2->3,3->1"));
    }

    public boolean hasCycle(String graph) {
        Map<String, List<String>> gMap = new HashMap<>();
        Map<String, Integer> cMap = new HashMap<>();
        for (String edge : graph.split(",")) {
            String[] e = edge.split("->");
            gMap.putIfAbsent(e[0], new ArrayList<>());
            gMap.putIfAbsent(e[1], new ArrayList<>());
            gMap.get(e[0]).add(e[1]);
            cMap.putIfAbsent(e[0], 0);
            cMap.put(e[1], cMap.getOrDefault(e[1], 0) + 1);
        }
        int cnt = 0;
        for (String src : cMap.keySet()) {
            if (dfs(gMap, new HashSet<>(), src)) return true;
            cnt++;
        }

        return cnt == 0;
    }

    boolean dfs(Map<String, List<String>> gMap, Set<String> path, String key) {
        path.add(key);
        List<String> nextList = gMap.get(key);
        for (String next : nextList) {
            if (path.contains(next)) return true;
            if (dfs(gMap, path, next)) return true;
        }
        path.remove(key);
        return false;
    }
}
