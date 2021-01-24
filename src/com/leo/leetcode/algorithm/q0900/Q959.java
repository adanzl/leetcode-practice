package com.leo.leetcode.algorithm.q0900;

/**
 * 在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。
 * （请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。
 * 返回区域的数目。
 * 提示：
 * 1、1 <= grid.length == grid[0].length <= 30
 * 2、grid[i][j] 是 '/'、'\'、或 ' '。
 * <p>
 * 链接：https://leetcode-cn.com/problems/regions-cut-by-slashes
 */
public class Q959 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q959().regionsBySlashes(new String[]{" /", "/ "}));
        // 1
        System.out.println(new Q959().regionsBySlashes(new String[]{" /", "  "}));
        // 4
        System.out.println(new Q959().regionsBySlashes(new String[]{"\\/", "/\\"}));
        // 5
        System.out.println(new Q959().regionsBySlashes(new String[]{"/\\", "\\/"}));
        // 3
        System.out.println(new Q959().regionsBySlashes(new String[]{"//", "/ "}));
    }

    int[] parent;
    int count;

    public int regionsBySlashes(String[] grid) {
        int nLine = grid.length;
        count = nLine * nLine * 4;
        parent = new int[count];
        for (int i = 0; i < count; i++) parent[i] = i;
        for (int i = 0; i < grid.length; i++) {
            String line = grid[i];
            for (int j = 0; j < line.length(); j++) {
                int oIndex = 4 * (i * nLine + j), rIndex = oIndex + 4, dIndex = oIndex + nLine * 4;
                char c = line.charAt(j);
                if (c == ' ') {
                    merge(oIndex, oIndex + 1);
                    merge(oIndex, oIndex + 2);
                    merge(oIndex, oIndex + 3);
                } else if (c == '\\') {
                    merge(oIndex, oIndex + 1);
                    merge(oIndex + 2, oIndex + 3);
                } else if (c == '/') {
                    merge(oIndex, oIndex + 3);
                    merge(oIndex + 1, oIndex + 2);
                }
                if (i < grid.length - 1) {
                    merge(oIndex + 2, dIndex);
                }
                if (j < line.length() - 1) {
                    merge(oIndex + 1, rIndex + 3);
                }
            }
        }
        return count;
    }

    int find(int x) {
        return parent[x] == x ? x : (parent[x] = find(parent[x]));
    }

    void merge(int i0, int i1) {
        int r0 = find(i0), r1 = find(i1);
        if (r0 == r1) return;
        parent[r1] = r0;
        count--;
    }
}
