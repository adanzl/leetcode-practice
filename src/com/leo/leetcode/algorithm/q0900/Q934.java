package com.leo.leetcode.algorithm.q0900;

import java.util.ArrayDeque;
import java.util.Queue;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）
 * 现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。
 * 返回必须翻转的 0 的最小数目。（可以保证答案至少是 1 。）
 * 提示：
 * 1、2 <= A.length == A[0].length <= 100
 * 2、A[i][j] == 0 或 A[i][j] == 1
 * 链接：https://leetcode-cn.com/problems/shortest-bridge
 */
public class Q934 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q934().shortestBridge(stringToInt2dArray("[[0,1],[1,0]]")));
        // 2
        System.out.println(new Q934().shortestBridge(stringToInt2dArray("[[0,1,0],[0,0,0],[0,0,1]]")));
        // 1
        System.out.println(new Q934().shortestBridge(stringToInt2dArray("[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]")));
    }

    int w, h;
    int[][] grid;
    final Queue<int[]> q = new ArrayDeque<>();
    boolean[][] visited;

    public int shortestBridge(int[][] grid) {
        int v = 1, ret = 0;
        this.grid = grid;
        w = grid.length;
        h = grid[0].length;
        visited = new boolean[w][h];
        for (int i = 0; i < w; i++) {
            for (int j = 0; j < h; j++) {
                if (grid[i][j] == 1 && !visited[i][j])
                    dfs(i, j, v++);
            }
        }
        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0 && !q.isEmpty()) {
                int[] p = q.poll();
                int x = p[0], y = p[1];
                if (visit(x - 1, y)) return ret;
                if (visit(x + 1, y)) return ret;
                if (visit(x, y - 1)) return ret;
                if (visit(x, y + 1)) return ret;
            }
            ret++;
        }
        return -1;
    }

    boolean dfs(int x, int y, int v) {
        if (x < 0 || x >= w || y < 0 || y >= h || visited[x][y]) return false;
        if (grid[x][y] == 0) return true;
        visited[x][y] = true;
        grid[x][y] = v;
        boolean bEdge = dfs(x - 1, y, v);
        bEdge |= dfs(x + 1, y, v);
        bEdge |= dfs(x, y - 1, v);
        bEdge |= dfs(x, y + 1, v);
        if (v == 1 && bEdge) q.add(new int[]{x, y});
        return false;
    }

    boolean visit(int x, int y) {
        if (x < 0 || x >= w || y < 0 || y >= h) return false;
        if (grid[x][y] == 2) return true;
        if (visited[x][y]) return false;
        visited[x][y] = true;
        q.add(new int[]{x, y});
        return false;
    }
}
