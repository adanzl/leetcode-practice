package com.leo.leetcode.algorithm;

import java.util.ArrayList;
import java.util.List;

public class Q830 {

    public static void main(String[] args) {
        System.out.println(new Q830().largeGroupPositions("aaa")); // [[0,2]]
        System.out.println(new Q830().largeGroupPositions("abbxxxxzzy")); // [[3,6]]
        System.out.println(new Q830().largeGroupPositions("abc")); // []
        System.out.println(new Q830().largeGroupPositions("abcdddeeeeaabbbcd")); // [[3,5],[6,9],[12,14]]
        System.out.println(new Q830().largeGroupPositions("aba")); // []
    }

    public List<List<Integer>> largeGroupPositions(String s) {
        char[] str = s.toCharArray();
        List<List<Integer>> ret = new ArrayList<>();
        if (s.length() == 0) return ret;
        int start = 0, count = 1;
        for (int i = 1; i < s.length(); i++) {
            if (str[i - 1] != str[i]) {
                if (count >= 3) {
                    List<Integer> ans = new ArrayList<>();
                    ans.add(start);
                    ans.add(i - 1);
                    ret.add(ans);
                }
                start = i;
                count = 1;
            } else {
                ++count;
            }
        }
        if (count >= 3) {
            List<Integer> ans = new ArrayList<>();
            ans.add(start);
            ans.add(str.length - 1);
            ret.add(ans);
        }
        return ret;
    }
}
