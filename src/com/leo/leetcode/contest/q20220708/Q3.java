package com.leo.leetcode.contest.q20220708;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 某区域地图记录在 k 二维数组 area，其中 0 表示空地，1 表示快递分发点。
 * 若希望选取一个地点设立中转站，使得中转站至各快递分发点的「曼哈顿距离」总和最小。请返回这个 最小 的距离总和。
 * 注意：
 * 1、曼哈顿距离：distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|
 * 2、所有位置均可作为快递中转站的设立点。
 * 提示:
 * 1、m == area.length
 * 2、n == area[i].length
 * 3、1 <= m, n <= 200
 * 4、area[i][j] == 0 或 1.
 * 5、area 中 至少 有两个快递分发点
 * 链接：https://leetcode.cn/contest/zj-future2022/problems/kflZMc/
 */
public class Q3 {

    public static void main(String[] args) {
        // 5
        System.out.println(new Q3().buildTransferStation(stringToInt2dArray("[[0,1,0,0,0],[0,0,0,0,1],[0,0,1,0,0]]")));
        // 4
        System.out.println(new Q3().buildTransferStation(stringToInt2dArray("[[1,1],[1,1]]")));
    }

    public int buildTransferStation(int[][] area) {
        int m = area.length, n = area[0].length;
        List<Integer> points = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (area[i][j] == 1) points.add(i * n + j);
            }
        }
        int ret = Integer.MAX_VALUE;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int d = 0, v1 = i * n + j;
                for (int p : points) {
                    d += Math.abs(p / n - v1 / n) + Math.abs(p % n - v1 % n);
                }
                ret = Math.min(ret, d);
            }
        }
        return ret;
    }
}
