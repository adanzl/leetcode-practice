package com.leo.leetcode.algorithm.q1900;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

import static com.leo.utils.LCUtil.stringToChar2dArray;
import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个 m x n 的迷宫矩阵 maze （下标从 0 开始），矩阵中有空格子（用 '.' 表示）和墙（用 '+' 表示）。
 * 同时给你迷宫的入口 entrance ，用 entrance = [entrance_row, entrance_col] 表示你一开始所在格子的行和列。
 * 每一步操作，你可以往 上，下，左 或者 右 移动一个格子。你不能进入墙所在的格子，你也不能离开迷宫。你的目标是找到离 entrance 最近 的出口。
 * 出口 的含义是 maze 边界 上的 空格子。entrance 格子 不算 出口。
 * 请你返回从 entrance 到最近出口的最短路径的 步数 ，如果不存在这样的路径，请你返回 -1 。
 * 提示：
 * 1、maze.length == m
 * 2、maze[i].length == n
 * 3、1 <= m, n <= 100
 * 4、maze[i][j] 要么是 '.' ，要么是 '+' 。
 * 5、entrance.length == 2
 * 6、0 <= entrance_row < m
 * 7、0 <= entrance_col < n
 * 8、entrance 一定是空格子。
 * 链接：https://leetcode-cn.com/problems/nearest-exit-from-entrance-in-maze
 */
public class Q1926 {
    public static void main(String[] args) {
        // 2
        System.out.println(new Q1926().nearestExit(
                stringToChar2dArray("[[\"+\",\"+\",\"+\"],[\".\",\".\",\".\"],[\"+\",\"+\",\"+\"]]"),
                stringToIntegerArray("[1,0]")));
        // 1
        System.out.println(new Q1926().nearestExit(
                stringToChar2dArray("[[\"+\",\"+\",\".\",\"+\"],[\".\",\".\",\".\",\"+\"],[\"+\",\"+\",\"+\",\".\"]]"),
                stringToIntegerArray("[1,2]")));
        // -1
        System.out.println(new Q1926().nearestExit(
                stringToChar2dArray("[[\".\",\"+\"]]"),
                stringToIntegerArray("[0,0]")));
    }

    char[][] maze;
    int w, h;
    boolean[][] visited;
    final Queue<int[]> q = new ArrayDeque<>();

    public int nearestExit(char[][] maze, int[] entrance) {
        this.maze = maze;
        w = maze.length;
        h = maze[0].length;
        int ret = 1;
        visited = new boolean[w][h];

        q.add(entrance);
        visited[entrance[0]][entrance[1]] = true;
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

    boolean visit(int x, int y) {
        if (x < 0 || x >= w || y < 0 || y >= h || visited[x][y] || maze[x][y] == '+') return false;
        if (x == 0 || x == w - 1 || y == 0 || y == h - 1) return true;
        visited[x][y] = true;
        q.add(new int[]{x, y});
        return false;
    }
}
