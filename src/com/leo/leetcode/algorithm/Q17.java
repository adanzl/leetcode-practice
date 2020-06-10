package com.leo.leetcode.algorithm;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class Q17 {
    public List<String> letterCombinations(String digits) {

        HashMap<Character, String[]> charMap = new HashMap<>();
        charMap.put('2', new String[]{"a", "b", "c"});
        charMap.put('3', new String[]{"d", "e", "f"});
        charMap.put('4', new String[]{"g", "h", "i"});
        charMap.put('5', new String[]{"j", "k", "l"});
        charMap.put('6', new String[]{"m", "n", "o"});
        charMap.put('7', new String[]{"p", "q", "r", "s"});
        charMap.put('8', new String[]{"t", "u", "v"});
        charMap.put('9', new String[]{"w", "x", "y", "z"});
        String[] ret = new String[]{};
        for (int i = 0; i < digits.length(); i++) {
            char v = digits.charAt(i);
            if (!charMap.containsKey(v)) continue;
            String[] list = charMap.get(v);
            ret = multiArray(ret, list);
        }
        return Arrays.asList(ret);
    }

    String[] multiArray(String[] a1, String[] a2) {
        if (a1.length == 0) return a2;
        String[] ret = new String[a1.length * a2.length];
        for (int i = 0; i < a1.length; i++) {
            for (int j = 0; j < a2.length; j++) {
                ret[i * a2.length + j] = a1[i] + a2[j];
            }
        }
        return ret;
    }
}
