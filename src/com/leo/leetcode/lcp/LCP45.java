package com.leo.leetcode.lcp;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 「力扣挑战赛」中 N*M 大小的自行车炫技赛场的场地由一片连绵起伏的上下坡组成，场地的高度值记录于二维数组 terrain 中，场地的减速值记录于二维数组 obstacle 中。
 * 若选手骑着自行车从高度为 h1 且减速值为 o1 的位置到高度为 h2 且减速值为 o2 的相邻位置（上下左右四个方向），速度变化值为 h1-h2-o2（负值减速，正值增速）。
 * 选手初始位于坐标 position 处且初始速度为 1，请问选手可以刚好到其他哪些位置时速度依旧为 1。请以二维数组形式返回这些位置。若有多个位置则按行坐标升序排列，若有多个位置行坐标相同则按列坐标升序排列。
 * 注意： 骑行过程中速度不能为零或负值
 * 提示：
 * 1、n == terrain.length == obstacle.length
 * 2、m == terrain[i].length == obstacle[i].length
 * 3、1 <= n <= 100
 * 4、1 <= m <= 100
 * 5、0 <= terrain[i][j], obstacle[i][j] <= 100
 * 6、position.length == 2
 * 7、0 <= position[0] < n
 * 8、0 <= position[1] < m
 * 链接：https://leetcode.cn/problems/kplEvH
 */
public class LCP45 {

    public static void main(String[] args) {
        // [[0,1],[1,0],[1,1]]
        System.out.println(Arrays.deepToString(new LCP45().bicycleYard(stringToIntegerArray("[0,0]"), stringToInt2dArray("[[0,0],[0,0]]"), stringToInt2dArray("[[0,0],[0,0]]"))));
        // [[0,1]]
        System.out.println(Arrays.deepToString(new LCP45().bicycleYard(stringToIntegerArray("[1,1]"), stringToInt2dArray("[[5,0],[0,6]]"), stringToInt2dArray("[[0,6],[7,0]]"))));
        //
        System.out.println(Arrays.deepToString(new LCP45().bicycleYard(stringToIntegerArray("[2,0]"), stringToInt2dArray("[[0],[5],[10]]"), stringToInt2dArray("[[4],[3],[0]]"))));
    }

    public int[][] bicycleYard(int[] position, int[][] terrain, int[][] obstacle) {
        List<int[]> ret = new ArrayList<>();
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int n = terrain.length, m = terrain[0].length;
        List<List<Set<Integer>>> visited = new ArrayList<>(m);
        for (int i = 0; i < n; i++) {
            visited.add(new ArrayList<>(m));
            for (int j = 0; j < m; j++) {
                visited.get(i).add(new HashSet<>());
            }
        }
        visited.get(position[0]).get(position[1]).add(1);
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{position[0], position[1], 1});
        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0 && !q.isEmpty()) {
                int[] cur = q.poll();
                for (int[] dir : dirs) {
                    int x = cur[0] + dir[0], y = cur[1] + dir[1];
                    if (x < 0 || y < 0 || x >= n || y >= m) continue;
                    int v = cur[2] + terrain[cur[0]][cur[1]] - terrain[x][y] - obstacle[x][y];
                    if (v <= 0 || visited.get(x).get(y).contains(v)) continue;
                    q.offer(new int[]{x, y, v});
                    visited.get(x).get(y).add(v);
                    if (v == 1) ret.add(new int[]{x, y});
                }
            }
        }
        ret.sort((o1, o2) -> o1[0] != o2[0] ? o1[0] - o2[0] : o1[1] - o2[1]);
        return ret.toArray(new int[0][]);
    }

}
