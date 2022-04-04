package com.leo.leetcode.algorithm.q0800;

import java.util.Arrays;
import java.util.Comparator;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 你有 n 个工作和 m 个工人。给定三个数组： difficulty, profit 和 worker ，其中:
 * 1、difficulty[i] 表示第 i 个工作的难度，profit[i] 表示第 i 个工作的收益。
 * 3、worker[i] 是第 i 个工人的能力，即该工人只能完成难度小于等于 worker[i] 的工作。
 * 4、每个工人 最多 只能安排 一个 工作，但是一个工作可以 完成多次 。
 * 举个例子，如果 3 个工人都尝试完成一份报酬为 $1 的同样工作，那么总收益为 $3 。如果一个工人不能完成任何工作，他的收益为 $0 。
 * 返回 在把工人分配到工作岗位后，我们所能获得的最大利润 。
 * 提示:
 * 1、n == difficulty.length
 * 2、n == profit.length
 * 3、m == worker.length
 * 4、1 <= n, m <= 104
 * 5、1 <= difficulty[i], profit[i], worker[i] <= 105
 * 链接：https://leetcode-cn.com/problems/most-profit-assigning-work
 */
public class Q826 {

    public static void main(String[] args) {
        // 100
        System.out.println(new Q826().maxProfitAssignment(stringToIntegerArray("[2,4,6,8,10]"), stringToIntegerArray("[10,20,30,40,50]"), stringToIntegerArray("[4,5,6,7]")));
        // 0
        System.out.println(new Q826().maxProfitAssignment(stringToIntegerArray("[85,47,57]"), stringToIntegerArray("[24,66,99]"), stringToIntegerArray("[40,25,25]")));
    }

    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        int len = difficulty.length, ret = 0;
        int[][] data = new int[len][3];
        for (int i = 0; i < len; i++) {
            data[i][0] = difficulty[i];
            data[i][1] = profit[i];
        }
        Arrays.sort(data, Comparator.comparingInt(o -> o[0]));
        data[0][2] = data[0][1];
        for (int i = 1; i < len; i++) data[i][2] = Math.max(data[i - 1][2], data[i][1]);
        for (int w : worker) {
            int l = 0, r = len - 1, idx = -1;
            while (l <= r) {
                int mid = (l + r) >> 1;
                if (data[mid][0] <= w) {
                    l = mid + 1;
                    idx = mid;
                } else r = mid - 1;
            }
            if (idx == -1) continue;
            ret += data[idx][2];
        }
        return ret;
    }
}
