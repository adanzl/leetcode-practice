package com.leo.leetcode.algorithm;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class Q20 {
    public boolean isValid(String s) {
        Map<Character, Character> charMap = new HashMap<>();
        charMap.put('[', ']');
        charMap.put('{', '}');
        charMap.put('(', ')');
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char v = s.charAt(i);
            if (' ' == v) continue;
            if (charMap.containsKey(v)) {
                stack.push(v);
            } else {
                if (stack.empty()) return false;
                char c = stack.pop();
                if (charMap.get(c) != v) {
                    return false;
                }
            }
        }

        return stack.empty();
    }
}
