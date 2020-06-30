package com.leo.leetcode.algorithm;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

/**
 * 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
 * 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
 * 说明:
 * 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
 * 链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
 */
public class Q17 {
    public static void main(String[] args) {
        System.out.println(new Q17().letterCombinations("23")); // ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    }

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
