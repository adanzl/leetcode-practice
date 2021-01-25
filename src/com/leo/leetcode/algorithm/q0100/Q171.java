package com.leo.leetcode.algorithm.q0100;

/**
 * 给定一个Excel表格中的列名称，返回其相应的列序号。
 * 例如，
 * A -> 1
 * B -> 2
 * C -> 3
 * ...
 * Z -> 26
 * AA -> 27
 * AB -> 28
 * ...
 * <p>
 * 链接：https://leetcode-cn.com/problems/excel-sheet-column-number
 */
public class Q171 {
    public static void main(String[] args) {
        // 1
        System.out.println(new Q171().titleToNumber("A"));
        // 28
        System.out.println(new Q171().titleToNumber("AB"));
        // 701
        System.out.println(new Q171().titleToNumber("ZY"));
    }

    public int titleToNumber(String s) {
        int base = 26, ret = 0;
        for (char c : s.toCharArray()) {
            ret = ret * base + (c > 'A' ? c - 'A' : c - 'a' + 1);
        }
        return ret;
    }
}
