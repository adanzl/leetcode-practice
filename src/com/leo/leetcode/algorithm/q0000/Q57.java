package com.leo.leetcode.algorithm.q0000;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.*;

/**
 * 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
 * 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
 * <p>
 * 链接：https://leetcode-cn.com/problems/insert-interval
 */
public class Q57 {

    public static void main(String[] args) {
        // [[0,0]]
        System.out.println(int2dArrayToString(new Q57().insert(stringToInt2dArray("[]"), stringToIntegerArray("[0,0]"))));
        // [[0,0],[1,5]]
        System.out.println(int2dArrayToString(new Q57().insert(stringToInt2dArray("[[1,5]]"), stringToIntegerArray("[0,0]"))));
        // [[1,2],[3,10],[12,16]]
        System.out.println(int2dArrayToString(new Q57().insert(stringToInt2dArray("[[1,2],[3,5],[6,7],[8,10],[12,16]]"), stringToIntegerArray("[4,8]"))));
        // [[1,5],[6,9]]
        System.out.println(int2dArrayToString(new Q57().insert(stringToInt2dArray("[[1,3],[6,9]]"), stringToIntegerArray("[2,5]"))));
        // [[1,2],[3,10],[12,16]]
        System.out.println(int2dArrayToString(new Q57().insert(stringToInt2dArray("[[1,2],[3,5],[6,7],[8,10],[12,16]]"), stringToIntegerArray("[4,8]"))));
    }

    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> ret = new ArrayList<>();
        boolean found = false;
        for (int[] line : intervals) {
            if (line[1] < newInterval[0]) {
                ret.add(line);
                continue;
            }
            if (line[0] > newInterval[1]) {
                if (!found) ret.add(newInterval);
                ret.add(line);
                found = true;
                continue;
            }
            if (!found) ret.add(newInterval);
            newInterval[0] = Math.min(line[0], newInterval[0]);
            newInterval[1] = Math.max(line[1], newInterval[1]);
            found = true;
        }
        if (!found) ret.add(newInterval);
        return ret.toArray(new int[0][]);
    }
}
