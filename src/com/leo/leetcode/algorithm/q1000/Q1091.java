package com.leo.leetcode.algorithm.q1000;

import java.util.ArrayDeque;
import java.util.Queue;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。
 * 二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：
 * 路径途经的所有单元格都的值都是 0 。
 * 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
 * 畅通路径的长度 是该路径途经的单元格总数。
 * 提示：
 * 1、n == grid.length
 * 2、n == grid[i].length
 * 3、1 <= n <= 100
 * 4、grid[i][j] 为 0 或 1
 * 链接：https://leetcode-cn.com/problems/shortest-path-in-binary-matrix
 */
public class Q1091 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q1091().shortestPathBinaryMatrix(stringToInt2dArray("[[0,1],[1,0]]")));
        // 1
        System.out.println(new Q1091().shortestPathBinaryMatrix(stringToInt2dArray("[[0]]")));
        // 4
        System.out.println(new Q1091().shortestPathBinaryMatrix(stringToInt2dArray("[[0,0,0],[1,1,0],[1,1,0]]")));
        // -1
        System.out.println(new Q1091().shortestPathBinaryMatrix(stringToInt2dArray("[[1,0,0],[1,1,0],[1,1,0]]")));
        // -1
        System.out.println(new Q1091().shortestPathBinaryMatrix(stringToInt2dArray("[[0,1,0],[1,1,0],[1,1,0]]")));
    }

    Queue<int[]> q;
    boolean[][] visited;
    int[][] grid;
    int w, h;

    public int shortestPathBinaryMatrix(int[][] grid) {
        if (grid[0][0] == 1) return -1;
        int ret = 2;
        w = grid.length;
        h = grid[0].length;
        if (w == 1 && h == 1) return 1;
        this.grid = grid;
        q = new ArrayDeque<>();
        visited = new boolean[w][h];
        q.offer(new int[]{0, 0});
        visited[0][0] = true;
        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0 && !q.isEmpty()) {
                int[] p = q.poll();
                int x = p[0], y = p[1];
                if (visit(x, y - 1) && x == w - 1 && y - 1 == h - 1) return ret;
                if (visit(x, y + 1) && x == w - 1 && y + 1 == h - 1) return ret;
                if (visit(x - 1, y) && x - 1 == w - 1 && y == h - 1) return ret;
                if (visit(x - 1, y - 1) && x - 1 == w - 1 && y - 1 == h - 1) return ret;
                if (visit(x - 1, y + 1) && x - 1 == w - 1 && y + 1 == h - 1) return ret;
                if (visit(x + 1, y) && x + 1 == w - 1 && y == h - 1) return ret;
                if (visit(x + 1, y - 1) && x + 1 == w - 1 && y - 1 == h - 1) return ret;
                if (visit(x + 1, y + 1) && x + 1 == w - 1 && y + 1 == h - 1) return ret;
            }
            ret++;
        }
        return -1;
    }

    boolean visit(int x, int y) {
        if (x < 0 || x >= w || y < 0 || y >= h || visited[x][y] || grid[x][y] == 1) return false;
        visited[x][y] = true;
        q.offer(new int[]{x, y});
        return true;
    }
}
