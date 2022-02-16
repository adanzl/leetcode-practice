package com.leo.leetcode.algorithm.q1300;

import java.util.Arrays;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 公司里有 n 名员工，每个员工的 ID 都是独一无二的，编号从 0 到 n - 1。公司的总负责人通过 headID 进行标识。
 * 在 manager 数组中，每个员工都有一个直属负责人，其中 manager[i] 是第 i 名员工的直属负责人。对于总负责人，manager[headID] = -1。
 * 题目保证从属关系可以用树结构显示。
 * 公司总负责人想要向公司所有员工通告一条紧急消息。他将会首先通知他的直属下属们，然后由这些下属通知他们的下属，直到所有的员工都得知这条紧急消息。
 * 第 i 名员工需要 informTime[i] 分钟来通知它的所有直属下属（也就是说在 informTime[i] 分钟后，他的所有直属下属都可以开始传播这一消息）。
 * 返回通知所有员工这一紧急消息所需要的 分钟数 。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、0 <= headID < n
 * 3、manager.length == n
 * 4、0 <= manager[i] < n
 * 5、manager[headID] == -1
 * 6、informTime.length == n
 * 7、0 <= informTime[i] <= 1000
 * 8、如果员工 i 没有下属，informTime[i] == 0 。
 * 9、题目 保证 所有员工都可以收到通知。
 * 链接：https://leetcode-cn.com/problems/time-needed-to-inform-all-employees
 */
public class Q1376 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q1376().numOfMinutes(1, 0, stringToIntegerArray("[-1]"), stringToIntegerArray("[0]")));
        // 1
        System.out.println(new Q1376().numOfMinutes(6, 2, stringToIntegerArray("[2,2,-1,2,2,2]"), stringToIntegerArray("[0,0,1,0,0,0]")));
        // 21
        System.out.println(new Q1376().numOfMinutes(7, 6, stringToIntegerArray("[1,2,3,4,5,6,-1]"), stringToIntegerArray("[0,6,5,4,3,2,1]")));
        // 3
        System.out.println(new Q1376().numOfMinutes(15, 0, stringToIntegerArray("[-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]"), stringToIntegerArray("[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]")));
        // 1076
        System.out.println(new Q1376().numOfMinutes(4, 2, stringToIntegerArray("[3,3,-1,2]"), stringToIntegerArray("[0,0,162,914]")));
    }

    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        int ret = 0;
        int[] times = new int[n];
        Arrays.fill(times, -1);
        for (int i = 0; i < n; i++) {
            ret = Math.max(ret, findTime(times, manager, informTime, i));
        }
        return ret;
    }

    int findTime(int[] times, int[] manager, int[] informTime, int n) {
        int time = times[n];
        if (time >= 0) return time;
        int m = manager[n];
        if (m == -1) {
            times[n] = 0;
            return 0;
        }
        time = findTime(times, manager, informTime, m) + informTime[m];
        times[n] = time;
        return time;
    }
}
