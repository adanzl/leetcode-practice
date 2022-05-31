package com.leo.leetcode.lcof2;

import java.util.*;

/**
 * 现有一种使用英语字母的外星文语言，这门语言的字母顺序与英语顺序不同。
 * 给定一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。
 * 请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中 任意一种 顺序即可。
 * 字符串 s 字典顺序小于 字符串 t 有两种情况：
 * 1、在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。
 * 2、如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t 。
 * 提示：
 * 1、1 <= words.length <= 100
 * 2、1 <= words[i].length <= 100
 * 3、words[i] 仅由小写英文字母组成
 * 注意：本题与主站 269 题相同： https://leetcode-cn.com/problems/alien-dictionary/
 * 链接：https://leetcode.cn/problems/Jf1JuT
 */
public class Q114 {

    public static void main(String[] args) {
        // ""
        System.out.println(new Q114().alienOrder(new String[]{"abc", "ab"}));
        // "abcd"
        System.out.println(new Q114().alienOrder(new String[]{"ab", "adc"}));
        // "z"
        System.out.println(new Q114().alienOrder(new String[]{"z"}));
        // "wertf"
        System.out.println(new Q114().alienOrder(new String[]{"wrt", "wrf", "er", "ett", "rftt"}));
        // "zx"
        System.out.println(new Q114().alienOrder(new String[]{"z", "x"}));
        // ""
        System.out.println(new Q114().alienOrder(new String[]{"z", "x", "z"}));
    }

    public String alienOrder(String[] words) {
        Queue<Integer> q = new ArrayDeque<>();
        int[][] G = new int[26][26];
        int[] iDegree = new int[26];
        Arrays.fill(iDegree, -1);
        int cIn = 0, n = words.length;
        for (String word : words) {
            for (char c : word.toCharArray()) {
                iDegree[c - 'a'] = 0;
            }
        }
        for (int i = 1; i < n; i++) {
            String s1 = words[i - 1], s2 = words[i];
            boolean bGet = false;
            for (int j = 0; j < Math.min(s1.length(), s2.length()); j++) {
                int from = s1.charAt(j) - 'a', to = s2.charAt(j) - 'a';
                if (from != to) {
                    if (G[from][to] == 0) {
                        iDegree[to]++;
                        cIn++;
                    }
                    G[from][to] = 1;
                    bGet = true;
                    break;
                }
            }
            if (!bGet && s1.length() > s2.length()) return "";
        }
        for (int i = 0; i < 26; i++) if (iDegree[i] == 0) q.add(i);
        StringBuilder ret = new StringBuilder();
        while (!q.isEmpty()) {
            int c = q.poll();
            ret.append((char) (c + 'a'));
            for (int i = 0; i < 26; i++) {
                if (G[c][i] == 1) {
                    G[c][i] = 0;
                    iDegree[i]--;
                    if (iDegree[i] == 0) q.add(i);
                    cIn--;
                }
            }
        }
        if (cIn > 0) return "";
        return ret.toString();
    }
}
