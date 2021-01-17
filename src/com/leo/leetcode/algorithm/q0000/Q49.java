package com.leo.leetcode.algorithm.q0000;

import java.util.*;

public class Q49 {
    public void TestOJ() {
        groupAnagrams(new String[]{"eat", "tea", "tan", "ate", "nat", "bat"});
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> ret = new ArrayList<>();
        Map<String, List<String>> cMap = new HashMap<>();
        for (String s : strs) {
            String code = getCode(s);
            if (cMap.containsKey(code)) {
                List<String> l = cMap.get(code);
                l.add(s);
            } else {
                List<String> l = new ArrayList<>();
                l.add(s);
                cMap.put(code, l);
                ret.add(l);
            }
        }
        return ret;
    }

    String getCode(String str) {
        char[] c = str.toCharArray();
        Arrays.sort(c);
        return String.valueOf(c);
    }
}
