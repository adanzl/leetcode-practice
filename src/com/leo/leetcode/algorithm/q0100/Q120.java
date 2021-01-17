package com.leo.leetcode.algorithm.q0100;

import com.leo.utils.LCUtil;

import java.util.List;

/**
 * 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
 * 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
 * 说明：
 * 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
 * 链接：https://leetcode-cn.com/problems/triangle
 */
public class Q120 {
    public static void main(String[] args) {
        // -63
        System.out.println(new Q120().minimumTotal(LCUtil.stringToListListInt("[[-7],[-2,1],[-5,-5,9],[-4,-5,4,4],[-6,-6,2,-1,-5],[3,7,8,-3,7,-9],[-9,-1,-9,6,9,0,7],[-7,0,-6,-8,7,1,-4,9],[-3,2,-6,-9,-7,-6,-9,4,0],[-8,-6,-3,-9,-2,-6,7,-5,0,7],[-9,-1,-2,4,-2,4,4,-1,2,-5,5],[1,1,-6,1,-2,-4,4,-2,6,-6,0,6],[-3,-3,-6,-2,-6,-2,7,-9,-5,-7,-5,5,1]]")));
        System.out.println(new Q120().minimumTotal(LCUtil.stringToListListInt("[[-1],[-2,-3]]"))); // -4
        System.out.println(new Q120().minimumTotal(LCUtil.stringToListListInt("[[2],[3,4],[6,5,7],[4,1,8,3]]"))); // 11
        System.out.println(new Q120().minimumTotal(LCUtil.stringToListListInt("[[]]"))); // 0
        System.out.println(new Q120().minimumTotal(LCUtil.stringToListListInt("[]"))); // 0

    }

    public int minimumTotal(List<List<Integer>> triangle) {
        if (triangle.size() == 0 || triangle.get(0).size() == 0) return 0;
        int[] marks = new int[triangle.size()];
        marks[0] = triangle.get(0).get(0);
        for (int i = 1; i < triangle.size(); i++) {
            marks[i] = marks[i - 1] + triangle.get(i).get(i);
            for (int j = i - 1; j > 0; j--) marks[j] = Math.min(marks[j], marks[j - 1]) + triangle.get(i).get(j);
            marks[0] += triangle.get(i).get(0);
        }
        int out = Integer.MAX_VALUE;
        for (int v : marks) out = Math.min(out, v);
        return out;
    }
}
