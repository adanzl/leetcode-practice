package com.leo.leetcode.algorithm.q1000;

import com.leo.utils.LCUtil;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;

/**
 * 在一个 10^6 x 10^6 的网格中，每个网格上方格的坐标为 (x, y) 。
 * 现在从源方格 source = [sx, sy] 开始出发，意图赶往目标方格 target = [tx, ty] 。
 * 数组 blocked 是封锁的方格列表，其中每个 blocked[i] = [xi, yi] 表示坐标为 (xi, yi) 的方格是禁止通行的。
 * 每次移动，都可以走到网格中在四个方向上相邻的方格，只要该方格 不 在给出的封锁列表 blocked 上。同时，不允许走出网格。
 * 只有在可以通过一系列的移动从源方格 source 到达目标方格 target 时才返回 true。否则，返回 false。
 * 提示：
 * 1、0 <= blocked.length <= 200
 * 2、blocked[i].length == 2
 * 3、0 <= xi, yi < 10^6
 * 4、source.length == target.length == 2
 * 5、0 <= sx, sy, tx, ty < 10^6
 * 6、source != target
 * 7、题目数据保证 source 和 target 不在封锁列表内
 * <p>
 * 链接：https://leetcode-cn.com/problems/escape-a-large-maze
 */
public class Q1036 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q1036().isEscapePossible(
                LCUtil.stringToInt2dArray("[[100005,100073],[100006,100074],[100007,100075],[100008,100076],[100009,100077],[100010,100078],[100011,100079],[100012,100080],[100013,100081],[100014,100082],[100015,100083],[100016,100084],[100017,100085],[100018,100086],[100019,100087],[100020,100088],[100021,100089],[100022,100090],[100023,100091],[100024,100092],[100025,100091],[100026,100090],[100027,100089],[100028,100088],[100029,100087],[100030,100086],[100031,100085],[100032,100084],[100033,100083],[100034,100082],[100035,100081],[100036,100080],[100037,100079],[100038,100078],[100039,100077],[100040,100076],[100041,100075],[100042,100074],[100043,100073],[100044,100072],[100043,100071],[100042,100070],[100041,100069],[100040,100068],[100039,100067],[100038,100066],[100037,100065],[100036,100064],[100035,100063],[100034,100062],[100033,100061],[100032,100060],[100031,100059],[100030,100058],[100029,100057],[100028,100056],[100027,100055],[100026,100054],[100025,100053],[100024,100052],[100023,100053],[100022,100054],[100021,100055],[100020,100056],[100019,100057],[100018,100058],[100017,100059],[100016,100060],[100015,100061],[100014,100062],[100013,100063],[100012,100064],[100011,100065],[100010,100066],[100009,100067],[100008,100068],[100007,100069],[100006,100070],[100005,100071]]"),
                LCUtil.stringToIntegerArray("[100024,100072]"),
                LCUtil.stringToIntegerArray("[999994,999990]")
        ));
        // false
        System.out.println(new Q1036().isEscapePossible(
                LCUtil.stringToInt2dArray("[[100059,100063],[100060,100064],[100061,100065],[100062,100066],[100063,100067],[100064,100068],[100065,100069],[100066,100070],[100067,100071],[100068,100072],[100069,100073],[100070,100074],[100071,100075],[100072,100076],[100073,100077],[100074,100078],[100075,100079],[100076,100080],[100077,100081],[100078,100082],[100079,100083],[100080,100082],[100081,100081],[100082,100080],[100083,100079],[100084,100078],[100085,100077],[100086,100076],[100087,100075],[100088,100074],[100089,100073],[100090,100072],[100091,100071],[100092,100070],[100093,100069],[100094,100068],[100095,100067],[100096,100066],[100097,100065],[100098,100064],[100099,100063],[100098,100062],[100097,100061],[100096,100060],[100095,100059],[100094,100058],[100093,100057],[100092,100056],[100091,100055],[100090,100054],[100089,100053],[100088,100052],[100087,100051],[100086,100050],[100085,100049],[100084,100048],[100083,100047],[100082,100046],[100081,100045],[100080,100044],[100079,100043],[100078,100044],[100077,100045],[100076,100046],[100075,100047],[100074,100048],[100073,100049],[100072,100050],[100071,100051],[100070,100052],[100069,100053],[100068,100054],[100067,100055],[100066,100056],[100065,100057],[100064,100058],[100063,100059],[100062,100060],[100061,100061],[100060,100062]]"),
                LCUtil.stringToIntegerArray("[100079,100063]"),
                LCUtil.stringToIntegerArray("[999948,999967]")
        ));
        // false
        System.out.println(new Q1036().isEscapePossible(
                LCUtil.stringToInt2dArray("[[0,1],[1,0]]"),
                LCUtil.stringToIntegerArray("[0,0]"),
                LCUtil.stringToIntegerArray("[0,2]")
        ));
        // true
        System.out.println(new Q1036().isEscapePossible(
                LCUtil.stringToInt2dArray("[]"),
                LCUtil.stringToIntegerArray("[0,0]"),
                LCUtil.stringToIntegerArray("[999999,999999]")
        ));
    }

    // 压缩矩阵
    Map<Integer, Integer> xMap = new HashMap<>();
    Map<Integer, Integer> yMap = new HashMap<>();
    int width, height;

    public boolean isEscapePossible(int[][] blocked, int[] source, int[] target) {
        int[][] points = new int[blocked.length + 2][2];
        System.arraycopy(blocked, 0, points, 0, blocked.length);
        points[blocked.length] = source;
        points[blocked.length + 1] = target;

        width = this.buildMap(points, xMap, 0);
        height = this.buildMap(points, yMap, 1);
        int[][] parent = new int[width][height];
        boolean[][] visited = new boolean[width][height];
        for (int[] pos : blocked) parent[xMap.get(pos[0])][yMap.get(pos[1])] = -1;
        int sourceX = xMap.get(source[0]), sourceY = yMap.get(source[1]);
        int targetX = xMap.get(target[0]), targetY = yMap.get(target[1]);
        return walk(parent, visited, sourceX, sourceY, targetX, targetY);
    }

    int buildMap(int[][] points, Map<Integer, Integer> iMap, int id) {
        Arrays.sort(points, Comparator.comparingInt(o -> o[id]));
        int idx = 1, pre = 0;
        iMap.put(0, 0);
        for (int[] b : points) {
            if (pre == b[id]) continue;
            if (b[id] - pre != 1) idx++;
            iMap.put(b[id], idx);
            pre = b[id];
            idx++;
        }
        if (!iMap.containsKey(999999)) iMap.put(999999, idx++);
        return idx;
    }

    boolean walk(int[][] parent, boolean[][] visited, int x, int y, int targetX, int targetY) {
        if (x < 0 || y < 0 || x >= width || y >= height || parent[x][y] == -1 || visited[x][y]) {
            return false;
        }
        if (x == targetX && y == targetY) return true;
        visited[x][y] = true;
        if (walk(parent, visited, x - 1, y, targetX, targetY)) return true;
        if (walk(parent, visited, x + 1, y, targetX, targetY)) return true;
        if (walk(parent, visited, x, y - 1, targetX, targetY)) return true;
        if (walk(parent, visited, x, y + 1, targetX, targetY)) return true;
        visited[x][y] = false;
        parent[x][y] = -1;
        return false;
    }

}
