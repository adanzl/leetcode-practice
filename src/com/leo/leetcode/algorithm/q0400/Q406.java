package com.leo.leetcode.algorithm.q0400;

import com.leo.utils.LCUtil;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class Q406 {

    public static void main(String[] args) {
        new Q406().TestOJ();
    }

    public void TestOJ() {
        // [[1,0]]
        System.out.println(LCUtil.int2dArrayToString(reconstructQueue(LCUtil.stringToInt2dArray("[[1,0]]"))));
        // [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        System.out.println(LCUtil.int2dArrayToString(reconstructQueue(LCUtil.stringToInt2dArray("[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]"))));
    }

    /**
     * [[height, count]]
     * 1 排序：
     * # 按高度降序排列
     * # 在同一高度的人中，按 k 值的升序排列
     * 2 逐个地把它们放在输出队列中，索引等于它们的 k 值
     * <p>
     * [7,0], [7,1], [6,1], [5,0], [5,2], [4,4]
     * 再一个一个插入。
     * [7,0]
     * [7,0], [7,1]
     * [7,0], [6,1], [7,1]
     * [5,0], [7,0], [6,1], [7,1]
     * [5,0], [7,0], [5,2], [6,1], [7,1]
     * [5,0], [7,0], [5,2], [6,1], [4,4], [7,1]
     */

    private int[][] reconstructQueue(int[][] people) {
        Arrays.sort(people, (o1, o2) -> o1[0] != o2[0] ? o2[0] - o1[0] : o1[1] - o2[1]);
        List<int[]> out = new LinkedList<>();
        for (int[] v : people) {
            out.add(v[1], v);
        }
        return out.toArray(people);
    }
}
