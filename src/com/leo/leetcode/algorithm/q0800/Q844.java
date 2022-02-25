package com.leo.leetcode.algorithm.q0800;

/**
 * 给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。
 * 注意：如果对空文本输入退格字符，文本继续为空。
 * 提示：
 * 1、1 <= s.length, t.length <= 200
 * 2、s 和 t 只含有小写字母以及字符 '#'
 * 进阶： 你可以用 O(n) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？
 * 链接：https://leetcode-cn.com/problems/backspace-string-compare
 */
public class Q844 {

    public static void main(String[] args) {
        // false
        System.out.println(new Q844().backspaceCompare("bbbextm", "bbb#extm"));
        // true
        System.out.println(new Q844().backspaceCompare("n", "b#n"));
        // false
        System.out.println(new Q844().backspaceCompare("bxj##tw", "bxj###tw"));
        // true
        System.out.println(new Q844().backspaceCompare("ab##", "c#d#"));
        // true
        System.out.println(new Q844().backspaceCompare("ab#c", "ad#c"));
        // false
        System.out.println(new Q844().backspaceCompare("a#c", "b"));
    }

    public boolean backspaceCompare(String s, String t) {
        int i0 = s.length() - 1, i1 = t.length() - 1;
        while (i0 >= 0 && i1 >= 0) {
            char c0, c1;
            int b0 = 0, b1 = 0;
            do {
                if (i0 < 0) {
                    c0 = ' ';
                    break;
                }
                c0 = s.charAt(i0--);
                if (c0 == '#') b0++;
                else b0--;
            } while (b0 >= 0);
            do {
                if (i1 < 0) {
                    c1 = ' ';
                    break;
                }
                c1 = t.charAt(i1--);
                if (c1 == '#') b1++;
                else b1--;
            } while (b1 >= 0);
            if (c0 != c1) return false;
        }
        if (i0 >= 0) {
            int b = 0;
            do {
                if (s.charAt(i0) == '#') b++;
                else b--;
            } while (b >= 0 && --i0 >= 0);
        }
        if (i1 >= 0) {
            int b = 0;
            do {
                if (t.charAt(i1) == '#') b++;
                else b--;
            } while (b >= 0 && --i1 >= 0);
        }
        return i0 < 0 && i1 < 0;
    }
}
