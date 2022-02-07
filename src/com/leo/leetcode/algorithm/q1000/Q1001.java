package com.leo.leetcode.algorithm.q1000;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 在大小为 n x n 的网格 grid 上，每个单元格都有一盏灯，最初灯都处于 关闭 状态。
 * 给你一个由灯的位置组成的二维数组lamps ，其中 lamps[i] = [row_i, col_i] 表示 打开 位于 grid[row_i][col_i] 的灯。
 * 即便同一盏灯可能在 lamps 中多次列出，不会影响这盏灯处于 打开 状态。
 * 当一盏灯处于打开状态，它将会照亮 自身所在单元格 以及同一 行 、同一 列 和两条 对角线 上的 所有其他单元格 。
 * 另给你一个二维数组 queries ，其中 queries[j] = [row_j, col_j] 。
 * 对于第 j 个查询，如果单元格 [row_j, col_j] 是被照亮的，则查询结果为 1 ，否则为 0 。在第 j 次查询之后 [按照查询的顺序] ，
 * 关闭 位于单元格 grid[row_j][col_j] 上及相邻 8 个方向上（与单元格 grid[row_i][col_i] 共享角或边）的任何灯。
 * 返回一个整数数组 ans 作为答案， ans[j] 应等于第 j 次查询queries[j]的结果，1 表示照亮，0 表示未照亮。
 * 提示：
 * 1、1 <= n <= 10^9
 * 2、0 <= lamps.length <= 20000
 * 3、0 <= queries.length <= 20000
 * 4、lamps[i].length == 2
 * 5、0 <= row_i, col_i < n
 * 6、queries[j].length == 2
 * 7、0 <= row_j, col_j < n
 * <p>
 * 链接：https://leetcode-cn.com/problems/grid-illumination
 */

public class Q1001 {

    public static void main(String[] args) {
        // [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1]
        System.out.println(Arrays.toString(new Q1001().gridIllumination(
                100
                , stringToInt2dArray("[[7,55],[53,61],[2,82],[67,85],[81,75],[38,91],[68,0],[60,43],[40,19],[12,75],[26,2],[24,89],[42,81],[60,58],[77,72],[33,24],[19,93],[7,16],[58,54],[78,57],[97,49],[65,16],[42,75],[90,50],[89,34],[76,97],[58,23],[62,47],[94,28],[88,65],[3,87],[81,10],[12,81],[44,81],[54,92],[90,54],[17,54],[27,82],[48,15],[8,46],[4,99],[15,13],[90,77],[2,87],[18,33],[52,90],[4,95],[57,61],[31,22],[32,8],[49,26],[24,65],[88,55],[88,38],[64,76],[94,76],[59,12],[41,46],[80,28],[38,36],[65,67],[75,37],[56,97],[83,57],[2,4],[44,43],[71,90],[62,40],[79,94],[81,11],[96,34],[38,11],[22,3],[54,96],[78,33],[54,54],[79,98],[1,28],[0,32],[37,11]]")
                , stringToInt2dArray("[[24,84],[95,68],[80,35],[31,53],[69,45],[85,29],[87,25],[42,47],[7,59],[99,3],[31,70],[64,62],[44,91],[55,25],[15,52],[95,33],[21,29],[61,34],[93,34],[79,27],[30,86],[52,0],[18,10],[5,1],[40,21],[11,48],[55,94],[22,42],[81,0],[39,43],[5,25],[43,29],[45,47],[83,93],[77,70],[22,63],[30,73],[18,48],[39,88],[91,47]]")))
        );
        // [1,0]
        System.out.println(Arrays.toString(new Q1001().gridIllumination(6, stringToInt2dArray("[[1,1]]"), stringToInt2dArray("[[2,0],[1,0]]"))));
        // [1,0]
        System.out.println(Arrays.toString(new Q1001().gridIllumination(5, stringToInt2dArray("[[0,0],[4,4]]"), stringToInt2dArray("[[1,1],[1,0]]"))));
        // [1,1]
        System.out.println(Arrays.toString(new Q1001().gridIllumination(5, stringToInt2dArray("[[0,0],[4,4]]"), stringToInt2dArray("[[1,1],[1,1]]"))));
        // [1,1,0]
        System.out.println(Arrays.toString(new Q1001().gridIllumination(5, stringToInt2dArray("[[0,0],[0,4]]"), stringToInt2dArray("[[0,4],[0,1],[1,4]]"))));
    }

    Map<Integer, Set<Integer>> wLightMap = new HashMap<>(), hLightMap = new HashMap<>(), x0LightMap = new HashMap<>(), x1LightMap = new HashMap<>();

    public int[] gridIllumination(int n, int[][] lamps, int[][] queries) {

        for (int[] l : lamps) {
            int x = l[0], y = l[1], m = x - y;
            int posHash = posHas(x, y);
            wLightMap.putIfAbsent(x, new HashSet<>());
            hLightMap.putIfAbsent(y, new HashSet<>());
            x0LightMap.putIfAbsent(m, new HashSet<>());
            x1LightMap.putIfAbsent(x + y, new HashSet<>());
            wLightMap.get(x).add(posHash);
            hLightMap.get(y).add(posHash);
            x0LightMap.get(m).add(posHash);
            x1LightMap.get(x + y).add(posHash);
        }
        int[] ret = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            ret[i] = query(queries[i]) ? 1 : 0;
        }
        return ret;
    }

    boolean query(int[] q) {
        int x = q[0], y = q[1], m = x - y;
        boolean ret = !wLightMap.getOrDefault(x, new HashSet<>()).isEmpty()
                || !hLightMap.getOrDefault(y, new HashSet<>()).isEmpty()
                || !x0LightMap.getOrDefault(m, new HashSet<>()).isEmpty()
                || !x1LightMap.getOrDefault(x + y, new HashSet<>()).isEmpty();
        lightOff(x, y);
        lightOff(x, y + 1);
        lightOff(x, y - 1);
        lightOff(x + 1, y);
        lightOff(x + 1, y + 1);
        lightOff(x + 1, y - 1);
        lightOff(x - 1, y);
        lightOff(x - 1, y + 1);
        lightOff(x - 1, y - 1);
        return ret;
    }

    void lightOff(int x, int y) {
        int p = posHas(x, y);
        int m = x - y;
        wLightMap.getOrDefault(x, new HashSet<>()).remove(p);
        hLightMap.getOrDefault(y, new HashSet<>()).remove(p);
        x0LightMap.getOrDefault(m, new HashSet<>()).remove(p);
        x1LightMap.getOrDefault(x + y, new HashSet<>()).remove(p);
    }

    int posHas(int x, int y) {
        return Objects.hash(x, y);
    }
}
