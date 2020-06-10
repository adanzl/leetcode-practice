package com.leo.leetcode.algorithm;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Q990 {
    public static void main(String[] args) {
        System.out.println(new Q990().equationsPossible1(new String[]{"a==b", "b!=c", "c==a"})); // false
        System.out.println(new Q990().equationsPossible2(new String[]{"a==b", "e==c", "b==c", "a!=e"})); // false
        System.out.println(new Q990().equationsPossible(new String[]{"a!=a"})); // false
        System.out.println(new Q990().equationsPossible(new String[]{"a==b", "b!=a"})); // false
        System.out.println(new Q990().equationsPossible(new String[]{"c==c", "f!=a", "f==b", "b==c"})); // true
        System.out.println(new Q990().equationsPossible(new String[]{"b==a", "a==b"})); // true
        System.out.println(new Q990().equationsPossible(new String[]{"a==b", "b==c", "a==c"})); // true
        System.out.println(new Q990().equationsPossible(new String[]{"c==c", "b==d", "x!=z"})); // true
    }

    // 方法1:
    public boolean equationsPossible1(String[] equations) {
        Map<Character, Set<Character>> equalMap = new HashMap<>();
        for (String exp : equations) {
            if (exp.charAt(1) != '=') continue;
            char v1 = exp.charAt(0);
            char v2 = exp.charAt(3);
            Set<Character> s;
            if (equalMap.containsKey(v1)) {
                s = equalMap.get(v1);
            } else {
                s = new HashSet<>();
                equalMap.put(v1, s);
            }
            s.add(v1);
            s.add(v2);
            if (equalMap.containsKey(v2)) s.addAll(equalMap.get(v2));
            equalMap.put(v2, s);
        }
        for (String exp : equations) {
            if (exp.charAt(1) == '=') continue;
            char v1 = exp.charAt(0);
            char v2 = exp.charAt(3);
            if (v1 == v2) return false;
            if ((equalMap.containsKey(v1) && equalMap.get(v1).contains(v2))
                    || (equalMap.containsKey(v2) && equalMap.get(v2).contains(v1)))
                return false;
        }
        return true;
    }

    // 方法2：
    public static class MaskNode {
        int v;

        MaskNode(int v) {
            this.v = v;
        }
    }

    public boolean equationsPossible2(String[] equations) {
        MaskNode[] equalMap = new MaskNode[26];
        for (String exp : equations) {
            if (exp.charAt(1) != '=') continue;
            char v1 = exp.charAt(0);
            char v2 = exp.charAt(3);
            MaskNode s = equalMap[v1 - 'a'];
            if (s == null) {
                s = new MaskNode(0);
                equalMap[v1 - 'a'] = s;
            }
            s.v |= (1 << (v1 - 'a'));
            s.v |= (1 << (v2 - 'a'));
            if (equalMap[v2 - 'a'] != null) s.v |= equalMap[v2 - 'a'].v;
            equalMap[v2 - 'a'] = s;
        }
        for (String exp : equations) {
            if (exp.charAt(1) == '=') continue;
            char v1 = exp.charAt(0);
            char v2 = exp.charAt(3);
            if (v1 == v2) return false;
            if ((equalMap[v1 - 'a'] != null && (equalMap[v1 - 'a'].v & 1 << (v2 - 'a')) != 0)
                    || (equalMap[v2 - 'a'] != null && (equalMap[v2 - 'a'].v & 1 << (v1 - 'a')) != 0))
                return false;
        }
        return true;
    }

    // 方法3：
    public boolean equationsPossible(String[] equations) {
        int[] eMap = new int[26];
        for (int i = 0; i < eMap.length; i++) eMap[i] = i;
        for (String exp : equations) {
            if (exp.charAt(1) != '=') continue;
            char v1 = exp.charAt(0);
            char v2 = exp.charAt(3);
            eMap[findRoot(eMap, v1 - 'a')] = findRoot(eMap, v2 - 'a');
        }
        for (String exp : equations) {
            if (exp.charAt(1) == '=') continue;
            char v1 = exp.charAt(0);
            char v2 = exp.charAt(3);
            if (v1 == v2 || findRoot(eMap, v1 - 'a') == findRoot(eMap, v2 - 'a')) return false;
        }
        return true;
    }

    int findRoot(int[] eMap, int num) {
        int index = num;
        while (eMap[index] != index) {
            eMap[index] = eMap[eMap[index]]; // 隔级设置树根，很超纲，速度优化用
            index = eMap[index];
        }
        return index;
    }
}
