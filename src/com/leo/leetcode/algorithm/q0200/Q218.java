package com.leo.leetcode.algorithm.q0200;

import static com.leo.utils.LCUtil.stringToInt2dArray;

import java.util.*;

/**
 * 城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的 天际线 。
 * 每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：
 * 1、lefti 是第 i 座建筑物左边缘的 x 坐标。
 * 2、righti 是第 i 座建筑物右边缘的 x 坐标。
 * 3、heighti 是第 i 座建筑物的高度。
 * 天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。
 * 关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。
 * 注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；
 * 三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]
 * 提示：
 * 1、1 <= buildings.length <= 10^4
 * 2、0 <= lefti < righti <= 2^31 - 1
 * 3、1 <= heighti <= 2^31 - 1
 * 4、buildings 按 lefti 非递减排序
 * 链接：https://leetcode-cn.com/problems/the-skyline-problem
 */
public class Q218 {

    public static void main(String[] args) {
        // [[0, 3], [1, 0]]
        System.out.println(new Q218().getSkyline(stringToInt2dArray("[[0,1,3]]")));
        // [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
        System.out.println(new Q218().getSkyline(stringToInt2dArray("[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]")));
        // [[0,3],[5,0]]
        System.out.println(new Q218().getSkyline(stringToInt2dArray("[[0,2,3],[2,5,3]]")));
    }

    public List<List<Integer>> getSkyline(int[][] buildings) {
        List<List<Integer>> ret = new ArrayList<>();
        Queue<int[]> all = new PriorityQueue<>(Math.max(buildings.length >> 1, 1), (o1, o2) -> o1[0] != o2[0] ? o1[0] - o2[0] : o1[1] - o2[1]);
        TreeMap<Integer, Integer> heigths = new TreeMap<>((o1, o2) -> o2 - o1);
        for (int[] building : buildings) {
            all.add(new int[]{building[0], -building[2]});
            all.add(new int[]{building[1], building[2]});
        }
        while (!all.isEmpty()) {
            int[] p = all.poll();
            if (p[1] < 0) {
                // left point
                if (heigths.isEmpty() || heigths.firstKey() < -p[1]) {
                    ret.add(Arrays.asList(p[0], -p[1]));
                }
                heigths.put(-p[1], heigths.getOrDefault(-p[1], 0) + 1);
            } else {
                // right point
                if (heigths.get(p[1]) == 1) heigths.remove(p[1]);
                else heigths.put(p[1], heigths.get(p[1]) - 1);
                if (heigths.isEmpty() || heigths.firstKey() < p[1]) {
                    ret.add(Arrays.asList(p[0], heigths.isEmpty() ? 0 : heigths.firstKey()));
                }
            }
        }
        return ret;
    }

}
