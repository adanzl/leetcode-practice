package com.leo.leetcode.algorithm.q0200;

import com.leo.utils.LCUtil;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
 * 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
 * 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
 * 提示：
 *  输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
 *  你可以假定输入的先决条件中没有重复的边。
 *  1 <= numCourses <= 10^5
 * 链接：https://leetcode-cn.com/problems/course-schedule
 */
public class Q207 {

    public static void main(String[] args) {
        new Q207().TestOJ();
    }

    public void TestOJ() {
        System.out.println(canFinish(2, LCUtil.stringToInt2dArray("[[1,0],[0,2],[2,1]]"))); // t
        System.out.println(canFinish(2, LCUtil.stringToInt2dArray("[[1,0]]"))); // t
        System.out.println(canFinish(2, LCUtil.stringToInt2dArray("[[1,0],[0,1]]"))); // f
        System.out.println(canFinish(2, LCUtil.stringToInt2dArray("[]"))); // t
        System.out.println(canFinish(4, LCUtil.stringToInt2dArray("[[0,1],[3,1],[1,3],[3,2]]"))); // f
    }

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, Set<Integer>> pMap = new HashMap<>();
        for (int[] prerequisite : prerequisites) {
            int k = prerequisite[0];
            Set<Integer> l = pMap.computeIfAbsent(k, k1 -> new HashSet<>());
            l.add(prerequisite[1]);
        }
        for (int i = 0; i < numCourses; i++) {
            if (isLoop(pMap, i, i, new HashSet<>())) {
                return false;
            }
        }
        return true;
    }

    boolean isLoop(Map<Integer, Set<Integer>> pMap, int key, int fastSuc, Set<Integer> s) {
        if (s.contains(key)) return true;
        if (key < fastSuc) return false;
        Set<Integer> l = pMap.get(key);
        if (l == null) {
            return false;
        }
        s.add(key);
        for (int k : l) {
            if (isLoop(pMap, k, fastSuc, s)) return true;
        }
        s.remove(key);
        return false;
    }
}
