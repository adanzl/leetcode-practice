package com.leo.leetcode.algorithm.q1200;

import static com.leo.utils.LCUtil.stringToListListInt;

import java.util.*;

/**
 * 给你一个字符串  s，以及该字符串中的一些「索引对」数组  pairs，其中  pairs[i] =  [a, b]  表示字符串中的两个索引（编号从 0 开始）。
 * 你可以 任意多次交换 在  pairs  中任意一对索引处的字符。
 * 返回在经过若干次交换后，s  可以变成的按字典序最小的字符串。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、0 <= pairs.length <= 10^5
 * 3、0 <= pairs[i][0], pairs[i][1] < s.length
 * 4、s 中只含有小写英文字母
 * <p>
 * 链接：https://leetcode-cn.com/problems/smallest-string-with-swaps
 */
public class Q1202 {

    public static void main(String[] args) {
        // "abcd"
        System.out.println(new Q1202().smallestStringWithSwaps("dcab", stringToListListInt("[[0,3],[1,2],[0,2]]")));
        // "bacd"
        System.out.println(new Q1202().smallestStringWithSwaps("dcab", stringToListListInt("[[0,3],[1,2]]")));
        // "abc"
        System.out.println(new Q1202().smallestStringWithSwaps("cba", stringToListListInt("[[0,1],[1,2]]")));
    }

    int[] parent;

    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        char[] str = s.toCharArray();
        parent = new int[str.length];
        int[] index = new int[str.length];
        for (int i = 0; i < str.length; i++) parent[i] = i;
        for (List<Integer> p : pairs) merge(p.get(0), p.get(1));
        Map<Integer, List<Character>> dMap = new HashMap<>();
        for (int i = 0; i < parent.length; i++) {
            int p = find(i);
            if (!dMap.containsKey(p)) dMap.put(p, new ArrayList<>());
            dMap.get(p).add(str[i]);
        }
        for (Map.Entry<Integer, List<Character>> entry : dMap.entrySet()) {
            entry.getValue().sort(Comparator.comparingInt(o -> o));
        }
        for(int i = 0; i<str.length; i++) {
            int g = find(i);
            str[i] = dMap.get(g).get(index[g]++);
        }

        return new String(str);
    }

    int find(int x) {
        return parent[x] == x ? x : (parent[x] = find(parent[x]));
    }

    void merge(int i0, int i1) {
        int r0 = find(i0), r1 = find(i1);
        if (r0 != r1) parent[r1] = r0;
    }

}
