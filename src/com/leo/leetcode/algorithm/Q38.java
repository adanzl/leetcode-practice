package com.leo.leetcode.algorithm;

import org.junit.Test;

public class Q38 {
    @Test
    public void TestOJ() {
        System.out.println(countAndSay(4));

    }

    public String countAndSay(int n) {
        String out = "1";
        while (n-- > 1) {
            out = say(out);
        }
        return out;
    }

    String say(String word) {
        char c = word.charAt(0);
        int count = 1;
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < word.length(); i++) {
            if (c == word.charAt(i)) {
                count++;
            } else {
                sb.append(count).append(c);
                count = 1;
                c = word.charAt(i);
            }
        }
        sb.append(count).append(c);
        return sb.toString();
    }

}
