package com.leo.leetcode.algorithm.q2200;

import java.util.*;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一棵 树（即一个连通、无向、无环图），根节点是节点 0 ，这棵树由编号从 0 到 n - 1 的 n 个节点组成。
 * 用下标从 0 开始、长度为 n 的数组 parent 来表示这棵树，其中 parent[i] 是节点 i 的父节点，由于节点 0 是根节点，所以 parent[0] == -1 。
 * 另给你一个字符串 s ，长度也是 n ，其中 s[i] 表示分配给节点 i 的字符。
 * 请你找出路径上任意一对相邻节点都没有分配到相同字符的 最长路径 ，并返回该路径的长度。
 * 提示：
 * 1、n == parent.length == s.length
 * 2、1 <= n <= 10^5
 * 3、对所有 i >= 1 ，0 <= parent[i] <= n - 1 均成立
 * 4、parent[0] == -1
 * 5、parent 表示一棵有效的树
 * 6、s 仅由小写英文字母组成
 * 链接：https://leetcode-cn.com/problems/longest-path-with-different-adjacent-characters
 */
public class Q2246 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q2246().longestPath(stringToIntegerArray("[-1,0,0,1,1,2]"), "abacbe"));
        // 5
        System.out.println(new Q2246().longestPath(stringToIntegerArray("[-1,0,0,1,1,2]"), "abccbe"));
        // 2
        System.out.println(new Q2246().longestPath(stringToIntegerArray("[-1,0,1]"), "aab"));
        // 3
        System.out.println(new Q2246().longestPath(stringToIntegerArray("[-1,0,0,0]"), "aabc"));
    }

    int max = 0;

    public int longestPath(int[] parent, String s) {
        List<List<Integer>> children = new ArrayList<>();
        for (int i = 0; i < parent.length; i++) children.add(new ArrayList<>());
        for (int i = 0; i < parent.length; i++) {
            if (parent[i] == -1) continue;
            children.get(parent[i]).add(i); // idx, len
        }
        dfs(children, s, 0);
        return max;
    }

    int dfs(List<List<Integer>> children, String s, int idx) {
        int ret = 0, max1 = 0, max2 = 0;
        char c = s.charAt(idx);
        for (int child : children.get(idx)) {
            int len = dfs(children, s, child) + 1;
            if (c == s.charAt(child)) continue;
            if (max1 < len) {
                max2 = max1;
                max1 = len;
            } else if (max2 < len) {
                max2 = len;
            }
            ret = Math.max(ret, len);
        }
        max = Math.max(max, 1 + max1 + max2);
        return ret;
    }
}
