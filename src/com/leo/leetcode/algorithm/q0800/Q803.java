package com.leo.leetcode.algorithm.q0800;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 有一个 m x n 的二元网格，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是：
 * 一块砖直接连接到网格的顶部，或者
 * 至少有一块相邻（4个方向之一）砖块 稳定 不会掉落时
 * 给你一个数组 hits ，这是需要依次消除砖块的位置。
 * 每当消除hits[i] = (row, col) 位置上的砖块时，对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这一消除操作而掉落。
 * 一旦砖块掉落，它会立即从网格中消失（即，它不会落在其他稳定的砖块上）。
 * 返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。
 * 注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m, n <= 200
 * 4、grid[i][j] 为 0 或 1
 * 5、1 <= hits.length <= 4 * 104
 * 6、hits[i].length == 2
 * 7、0 <= xi <= m - 1
 * 8、0 <= yi <= n - 1
 * 9、所有 (xi, yi) 互不相同
 * 链接：https://leetcode-cn.com/problems/bricks-falling-when-hit
 */
public class Q803 {
    public static void main(String[] args) {
        // [0,3,0]
        System.out.println(Arrays.toString(new Q803().hitBricks(stringToInt2dArray("[[1,0,1],[1,1,1]]"), stringToInt2dArray("[[0,0],[0,2],[1,1]]"))));
        // [0,0]
        System.out.println(Arrays.toString(new Q803().hitBricks(stringToInt2dArray("[[1,0,0,0],[1,1,0,0]]"), stringToInt2dArray("[[1,1],[1,0]]"))));
        // [2]
        System.out.println(Arrays.toString(new Q803().hitBricks(stringToInt2dArray("[[1,0,0,0],[1,1,1,0]]"), stringToInt2dArray("[[1,0]]"))));
    }

    int row;
    int col;

    int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

    public int[] hitBricks(int[][] grid, int[][] hits) {
        int[] ret = new int[hits.length];
        for (int[] h : hits) {
            if (grid[h[0]][h[1]] == 1) grid[h[0]][h[1]] = 0;
            else grid[h[0]][h[1]] = 2;
        }
        row = grid.length;
        col = grid[0].length;
        int size = col * row;
        UnionNode unionNode = new UnionNode(size);
        for (int i = 0; i < grid[0].length; i++) {
            if (grid[0][i] == 1) unionNode.merge(size, getIndex(0, i));
        }
        for (int i = 1; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] != 1) continue;
                if (grid[i - 1][j] == 1) unionNode.merge(getIndex(i - 1, j), getIndex(i, j));
                if (j > 0 && grid[i][j - 1] == 1) unionNode.merge(getIndex(i, j - 1), getIndex(i, j));
            }
        }
        for (int i = hits.length - 1; i >= 0; i--) {
            int[] hit = hits[i];
            if (grid[hit[0]][hit[1]] == 2) continue;
            int ori = unionNode.getSize(size);
            if (hit[0] == 0) unionNode.merge(size, getIndex(hit[0], hit[1]));
            for (int[] d : directions) {
                int x = hit[0] + d[0], y = hit[1] + d[1];
                if (x >= 0 && x < row && y >= 0 && y < col && grid[x][y] == 1) {
                    unionNode.merge(getIndex(x, y), getIndex(hit[0], hit[1]));
                }
            }
            ret[i] = Math.max(0, unionNode.getSize(size) - ori - 1);
            grid[hit[0]][hit[1]] = 1;
        }
        return ret;
    }

    int getIndex(int x, int y) {
        return x * col + y;
    }


    static class UnionNode {
        int[] parent;
        int[] size;

        UnionNode(int size) {
            this.parent = new int[size + 1];
            this.size = new int[size + 1];
            for (int i = 0; i < size; i++) {
                this.parent[i] = i;
                this.size[i] = 1;
            }
            this.parent[size] = size;
        }

        int findRootIndex(int index) {
            if (parent[index] != index) {
                parent[index] = findRootIndex(parent[index]);
            }
            return parent[index];
        }

        void merge(int index0, int index1) {
            int r_0 = findRootIndex(index0);
            int r_1 = findRootIndex(index1);

            if (r_0 != r_1) {
                parent[r_1] = r_0;
                size[r_0] += size[r_1];
            }
        }

        int getSize(int index) {
            return size[findRootIndex(index)];
        }
    }

}
