package com.leo.leetcode.algorithm.q2200;

import java.util.ArrayList;
import java.util.List;
import java.util.TreeSet;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你两个整数 m 和 n 表示一个下标从 0 开始的 m x n 网格图。同时给你两个二维整数数组 guards 和 walls ，
 * 其中 guards[i] = [row_i, coli] 且 walls[j] = [row_j, col_j] ，分别表示第 i 个警卫和第 j 座墙所在的位置。
 * 一个警卫能看到 4 个坐标轴方向（即东、南、西、北）的 所有 格子，除非他们被一座墙或者另外一个警卫 挡住 了视线。
 * 如果一个格子能被 至少 一个警卫看到，那么我们说这个格子被 保卫 了。
 * 请你返回空格子中，有多少个格子是 没被保卫 的。
 * 提示：
 * 1、1 <= m, n <= 10^5
 * 2、2 <= m * n <= 10^5
 * 3、1 <= guards.length, walls.length <= 5 * 10^4
 * 4、2 <= guards.length + walls.length <= m * n
 * 5、guards[i].length == walls[j].length == 2
 * 6、0 <= row_i, row_j < m
 * 7、0 <= col_i, col_j < n
 * 8、guards 和 walls 中所有位置 互不相同 。
 * 链接：https://leetcode-cn.com/problems/count-unguarded-cells-in-the-grid
 */
public class Q2257 {

    public static void main(String[] args) {
        // 8
        System.out.println(new Q2257().countUnguarded(6, 10, stringToInt2dArray("[[0,6],[2,2],[2,5],[1,2],[4,9],[2,9],[5,6],[4,6]]"), stringToInt2dArray("[[1,5]]")));
        // 7
        System.out.println(new Q2257().countUnguarded(4, 6, stringToInt2dArray("[[0,0],[1,1],[2,3]]"), stringToInt2dArray("[[0,1],[2,2],[1,4]]")));
        // 4
        System.out.println(new Q2257().countUnguarded(3, 3, stringToInt2dArray("[[1,1]]"), stringToInt2dArray("[[0,1],[1,0],[2,1],[1,2]]")));
    }

    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        boolean[][] guarded = new boolean[m][n];
        int ret = m * n;
        List<TreeSet<Integer>> rowSets = new ArrayList<>(), colSets = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            TreeSet<Integer> set = new TreeSet<>();
            rowSets.add(set);
            set.add(-1);
            set.add(n);
        }
        for (int i = 0; i < n; i++) {
            TreeSet<Integer> set = new TreeSet<>();
            colSets.add(set);
            set.add(-1);
            set.add(m);
        }
        for (int[] wall : walls) {
            rowSets.get(wall[0]).add(wall[1]);
            colSets.get(wall[1]).add(wall[0]);
            guarded[wall[0]][wall[1]] = true;
        }
        ret -= walls.length;
        for (int[] guard : guards) {
            TreeSet<Integer> set = rowSets.get(guard[0]);
            {
                Integer top = set.higher(guard[1]), bottom = set.lower(guard[1]);
                if (top != null && bottom != null) {
                    for (int i = bottom + 1; i < top; i++) {
                        if (!guarded[guard[0]][i]) {
                            ret--;
                            guarded[guard[0]][i] = true;
                            set.add(i);
                        }
                    }
                }
            }
            set = colSets.get(guard[1]);
            {
                Integer top = set.higher(guard[0]), bottom = set.lower(guard[0]);
                if (top != null && bottom != null) {
                    for (int i = bottom + 1; i < top; i++) {
                        if (!guarded[i][guard[1]]) {
                            ret--;
                            guarded[i][guard[1]] = true;
                            set.add(i);
                        }
                    }
                }
            }
        }
        return ret;
    }
}
