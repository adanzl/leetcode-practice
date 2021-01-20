package com.leo.leetcode.algorithm.q1200;

import static com.leo.utils.LCUtil.stringToIntegerArray;
import static com.leo.utils.LCUtil.stringToListListInt;

import java.util.*;

public class Q1203 {

    public static void main(String[] args) {
        // [0,2,1]
        System.out.println(Arrays.toString(new Q1203().sortItems(3, 1,
                stringToIntegerArray("[-1,-1,0]"), stringToListListInt("[[],[0,2],[0]]"))));
        // [3,5,9,6,1,2,7,0,4,8]
        System.out.println(Arrays.toString(new Q1203().sortItems(10, 4,
                stringToIntegerArray("[2,2,2,1,0,1,3,2,0,1]"), stringToListListInt("[[7,6,2,5,3],[],[],[],[7],[],[],[],[],[]]"))));
        // [6,3,4,1,5,2,0,7]
        System.out.println(Arrays.toString(new Q1203().sortItems(8, 2,
                stringToIntegerArray("[-1,-1,1,0,0,1,0,-1]"), stringToListListInt("[[],[6],[5],[6],[3,6],[],[],[]]"))));
        // [3,2,4,1,0]
        System.out.println(Arrays.toString(new Q1203().sortItems(5, 5,
                stringToIntegerArray("[2,0,-1,3,0]"), stringToListListInt("[[2,1,3],[2,4],[],[],[]]"))));
        // []
        System.out.println(Arrays.toString(new Q1203().sortItems(8, 2,
                stringToIntegerArray("[-1,-1,1,0,0,1,0,-1]"), stringToListListInt("[[],[6],[5],[6],[3],[],[4],[]]"))));
    }

    // 组子任务
    Map<Integer, List<Integer>> groupSubTask;
    // 组依赖数
    int[] groupParent;
    Map<Integer, List<Integer>> groupParentOf;
    // 父任务数量
    int[] taskParent;
    // 孩子任务列表
    Map<Integer, List<Integer>> taskParentOf;

    public int[] sortItems(int n, int m, int[] group, List<List<Integer>> beforeItems) {
        int[] ret = new int[n];
        groupSubTask = new HashMap<>(); // 子任务
        groupParent = new int[m + n]; // 几个爹
        groupParentOf = new HashMap<>(); // 是谁的爹
        taskParent = new int[n]; // 几个爹
        taskParentOf = new HashMap<>(); // 是谁的爹
        for (int i = 0; i < group.length; i++) if (group[i] == -1) group[i] = m++;
        for (int i = 0; i < group.length; i++) {
            int g = group[i];
            if (!groupSubTask.containsKey(g)) groupSubTask.put(g, new ArrayList<>());
            groupSubTask.get(g).add(i);
            for (int before : beforeItems.get(i)) {
                int gBefore = group[before];
                if (gBefore != g) {
                    ++groupParent[g];
                    if (!groupParentOf.containsKey(gBefore)) groupParentOf.put(gBefore, new ArrayList<>());
                    groupParentOf.get(gBefore).add(g);
                }
                if (!taskParentOf.containsKey(before)) taskParentOf.put(before, new ArrayList<>());
                taskParentOf.get(before).add(i);
            }
            taskParent[i] = beforeItems.get(i).size();
        }
        int iOut = 0;
        while (!groupSubTask.isEmpty()) {
            int iGroup = -1, pre = iOut;
            for (Iterator<Map.Entry<Integer, List<Integer>>> it = groupSubTask.entrySet().iterator(); it.hasNext(); ) {
                Map.Entry<Integer, List<Integer>> item = it.next();
                if (groupParent[item.getKey()] != 0) continue;
                iGroup = item.getKey();
                iOut = handleGroup(ret, iOut, item.getValue());
                it.remove();
                if (pre == iOut) break;
                List<Integer> subGroup = groupParentOf.get(iGroup);
                if (subGroup != null) for (int g : subGroup) groupParent[g]--;
            }
            if (iGroup == -1 || pre == iOut) break;
        }
        return iOut == n ? ret : new int[0];
    }

    int handleGroup(int[] ret, int iOut, List<Integer> groupSubTask) {
        int count = 0;
        while (true) {
            int iTask = -1;
            for (int subTask : groupSubTask) {
                if (taskParent[subTask] != 0) continue;
                iTask = subTask;
                ret[iOut + count++] = subTask;
                taskParent[subTask]--;
                if (taskParentOf.containsKey(subTask)) for (int pTask : taskParentOf.get(subTask)) taskParent[pTask]--;
            }
            if (iTask == -1) break;
        }
        return count == groupSubTask.size() ? count + iOut : iOut;
    }
}
