package com.leo.leetcode.algorithm.q2200;

import static com.leo.utils.LCUtil.stringToChar2dArray;

/**
 * 一个括号字符串是一个 非空 且只包含 '(' 和 ')' 的字符串。如果下面 任意 条件为 真 ，那么这个括号字符串就是 合法的 。
 * 1、字符串是 () 。
 * 2、字符串可以表示为 AB（A 连接 B），A 和 B 都是合法括号序列。
 * 3、字符串可以表示为 (A) ，其中 A 是合法括号序列。
 * 给你一个 m x n 的括号网格图矩阵 grid 。网格图中一个 合法括号路径 是满足以下所有条件的一条路径：
 * 1、路径开始于左上角格子 (0, 0) 。
 * 2、路径结束于右下角格子 (m - 1, n - 1) 。
 * 3、路径每次只会向 下 或者向 右 移动。
 * 4、路径经过的格子组成的括号字符串是 合法 的。
 * 如果网格图中存在一条 合法括号路径 ，请返回 true ，否则返回 false 。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 100
 * 4、grid[i][j] 要么是 '(' ，要么是 ')' 。
 * 链接：https://leetcode-cn.com/problems/check-if-there-is-a-valid-parentheses-string-path
 */
public class Q2267 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q2267().hasValidPath(stringToChar2dArray("[[\"(\",\"(\",\"(\"],[\")\",\"(\",\")\"],[\"(\",\"(\",\")\"],[\"(\",\"(\",\")\"]]")));
        // false
        System.out.println(new Q2267().hasValidPath(stringToChar2dArray("[[\")\",\")\"],[\"(\",\"(\"]]")));
    }

    public boolean hasValidPath(char[][] grid) {
        boolean[][][] visited = new boolean[grid.length][grid[0].length][200];
        return dfs(grid, 0, 0, 0, visited);
    }

    boolean dfs(char[][] grid, int i, int j, int cLeft, boolean[][][] visited) {
        if (i >= grid.length || j >= grid[0].length) return false;
        if (cLeft > grid.length - i + grid[0].length - j - 1) return false;
        if (visited[i][j][cLeft]) return false;
        visited[i][j][cLeft] = true;
        if (grid[i][j] == '(') cLeft++;
        else {
            if (cLeft == 0) return false;
            cLeft--;
        }
        if (i == grid.length - 1 && j == grid[0].length - 1) return cLeft == 0;
        return dfs(grid, i + 1, j, cLeft, visited) || dfs(grid, i, j + 1, cLeft, visited);
    }
}
