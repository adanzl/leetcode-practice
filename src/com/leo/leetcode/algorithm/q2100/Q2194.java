package com.leo.leetcode.algorithm.q2100;

import java.util.ArrayList;
import java.util.List;

/**
 * Excel 表中的一个单元格 (r, c) 会以字符串 "<col><row>" 的形式进行表示，其中：
 * 1、<col> 即单元格的列号 c 。用英文字母表中的 字母 标识。例如，第 1 列用 'A' 表示，第 2 列用 'B' 表示，第 3 列用 'C' 表示，以此类推。
 * 2、<row> 即单元格的行号 r 。第 r 行就用 整数 r 标识。
 * 给你一个格式为 "<col1><row1>:<col2><row2>" 的字符串 s ，其中 <col1> 表示 c1 列，<row1> 表示 r1 行，<col2> 表示 c2 列，<row2> 表示 r2 行，并满足 r1 <= r2 且 c1 <= c2 。
 * 找出所有满足 r1 <= x <= r2 且 c1 <= y <= c2 的单元格，并以列表形式返回。单元格应该按前面描述的格式用 字符串 表示，并以 非递减 顺序排列（先按列排，再按行排）。
 * 提示：
 * 1、s.length == 5
 * 2、'A' <= s[0] <= s[3] <= 'Z'
 * 3、'1' <= s[1] <= s[4] <= '9'
 * 4、s 由大写英文字母、数字、和 ':' 组成
 * 链接：https://leetcode.cn/problems/cells-in-a-range-on-an-excel-sheet
 */
public class Q2194 {

    public static void main(String[] args) {
        // ["K1","K2","L1","L2"]
        System.out.println(new Q2194().cellsInRange("K1:L2"));
        // ["A1","B1","C1","D1","E1","F1"]
        System.out.println(new Q2194().cellsInRange("A1:F1"));
        // ["U7","U8","U9","V7","V8","V9","W7","W8","W9","X7","X8","X9"]
        System.out.println(new Q2194().cellsInRange("U7:X9"));
    }

    public List<String> cellsInRange(String s) {
        char c1 = s.charAt(0), c2 = s.charAt(3);
        int r1 = s.charAt(1) - '0', r2 = s.charAt(4) - '0';
        List<String> ret = new ArrayList<>();
        for (int i = c1; i <= c2; i++) {
            for (int j = r1; j <= r2; j++) {
                ret.add((char) i + "" + j);
            }
        }
        return ret;
    }
}
