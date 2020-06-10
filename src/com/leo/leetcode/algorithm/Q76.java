package com.leo.leetcode.algorithm;

import java.util.HashMap;
import java.util.Map;

import org.junit.Test;

public class Q76 {
    @Test
    public void TestOJ() {
//        System.out.println(minWindow("ADOBECODEBANC", "ABC")); // "BANC"
//        System.out.println(minWindow("ADAEBECADDABC", "ABC")); // "BECA"
//        System.out.println(minWindow("ADABC", "ABC")); // "ABC"
//        System.out.println(minWindow("ABC", "A")); // "A"
        System.out.println(minWindow("BC", "A")); // ""
//        System.out.println(minWindow("AA", "AA")); // "AA"
        System.out.println(minWindow("babb", "baba")); // ""
    }

    public String minWindow(String s, String t) {
        if (t.length() > s.length()) {
            return "";
        }
        Map<Character, Integer> mapT = new HashMap<>();
        for (int i = 0; i < t.length(); i++) {
            char v = t.charAt(i);
            int c = 1;
            if (mapT.containsKey(v)) {
                c = mapT.get(v) + 1;
            }
            mapT.put(v, c);
        }
        int find = 0, l = 0, r = 0;
        int minLen = Integer.MAX_VALUE, minL = -1, minR = -1;
        Map<Character, Integer> mapS = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            // right
            char v = s.charAt(i);
            if (mapT.containsKey(v)) {
                int c = 1;
                if (mapS.containsKey(v)) {
                    c = mapS.get(v) + 1;
                }
                if (mapT.get(v) == c) {
                    find++;
                }
                mapS.put(v, c);
            }
            if (find == mapT.size()) {
                // left
                r = i;
                if (minLen > r - l + 1) {
                    minLen = r - l + 1;
                    minL = l;
                    minR = r;
                }
                while (r - l + 1 >= t.length()) {
                    char lv = s.charAt(l);
                    l++;
                    if (mapT.containsKey(lv)) {
                        mapS.put(lv, mapS.get(lv) - 1);
                        if (mapS.get(lv) < mapT.get(lv)) {
                            find--;
                            break;
                        }
                    }
                    if (minLen > r - l + 1) {
                        minLen = r - l + 1;
                        minL = l;
                        minR = r;
                    }
                }
            }
        }

        if (minL == -1 || minR == -1) {
            return "";
        }
        return s.substring(minL, minR + 1);
    }

}
