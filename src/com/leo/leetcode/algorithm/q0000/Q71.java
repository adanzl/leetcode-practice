package com.leo.leetcode.algorithm.q0000;

import java.util.Stack;

public class Q71 {
    public static void main(String[] args) {
        System.out.println(new Q71().simplifyPath("/home/")); // "/home"
        System.out.println(new Q71().simplifyPath("/../")); // "/"
        System.out.println(new Q71().simplifyPath("/home//foo/")); // "/home/foo"
        System.out.println(new Q71().simplifyPath("/a/./b/../../c/")); // "/c"
        System.out.println(new Q71().simplifyPath("/a/../../b/../c//.//")); // "/c"
        System.out.println(new Q71().simplifyPath("/a//b////c/d//././/..")); // "/a/b/c"
        System.out.println(new Q71().simplifyPath("")); // "/"
    }

    public String simplifyPath(String path) {
        Stack<String> s = new Stack<>();
        String[] arr = path.split("/");
        StringBuilder out = new StringBuilder();
        for (String str : arr) {
            if (str.equals("") || str.equals(".")) continue;
            if (str.equals("..")) {
                if (!s.empty()) s.pop();
            } else s.push(str);
        }
        while (!s.empty()) {
            String str = s.pop();
            out.insert(0, str);
            out.insert(0, "/");
        }
        if (out.length() == 0) out.append("/");
        return out.toString();
    }
}
