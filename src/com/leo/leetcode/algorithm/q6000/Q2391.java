package com.leo.leetcode.algorithm.q6000;

import static com.leo.utils.LCUtil.stringToIntegerArray;
import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 给你一个下标从 0 开始的字符串数组 garbage ，其中 garbage[i] 表示第 i 个房子的垃圾集合。
 * garbage[i] 只包含字符 'M' ，'P' 和 'G' ，但可能包含多个相同字符，每个字符分别表示一单位的金属、纸和玻璃。垃圾车收拾 一 单位的任何一种垃圾都需要花费 1 分钟。
 * 同时给你一个下标从 0 开始的整数数组 travel ，其中 travel[i] 是垃圾车从房子 i 行驶到房子 i + 1 需要的分钟数。
 * 城市里总共有三辆垃圾车，分别收拾三种垃圾。每辆垃圾车都从房子 0 出发，按顺序 到达每一栋房子。但它们 不是必须 到达所有的房子。
 * 任何时刻只有 一辆 垃圾车处在使用状态。当一辆垃圾车在行驶或者收拾垃圾的时候，另外两辆车 不能 做任何事情。
 * 请你返回收拾完所有垃圾需要花费的 最少 总分钟数。
 * 提示：
 * 1、2 <= garbage.length <= 105
 * 2、garbage[i] 只包含字母 'M' ，'P' 和 'G' 。
 * 3、1 <= garbage[i].length <= 10
 * 4、travel.length == garbage.length - 1
 * 5、1 <= travel[i] <= 100
 * 链接：https://leetcode.cn/problems/minimum-amount-of-time-to-collect-garbage
 */
public class Q2391 {

    public static void main(String[] args) {
        // 21
        System.out.println(new Q2391().garbageCollection(stringToStringArray("[\"G\",\"P\",\"GP\",\"GG\"]"), stringToIntegerArray("[2,4,3]")));
        // 37
        System.out.println(new Q2391().garbageCollection(stringToStringArray("[\"MMM\",\"PGM\",\"GP\"]"), stringToIntegerArray("[3,10]")));
    }

    public int garbageCollection(String[] garbage, int[] travel) {
        int ans = 0, n = garbage.length, end0 = -1, end1 = -1, end2 = -1;
        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j < garbage[i].length(); j++) {
                char c = garbage[i].charAt(j);
                if (c == 'P' && end0 == -1) end0 = i;
                if (c == 'M' && end1 == -1) end1 = i;
                if (c == 'G' && end2 == -1) end2 = i;
            }
            ans += garbage[i].length();
        }
        int[] preSum = new int[n + 1];
        for (int i = 1; i < n; i++) preSum[i + 1] = preSum[i] + travel[i - 1];
        if (end0 != -1) ans += preSum[end0 + 1];
        if (end1 != -1) ans += preSum[end1 + 1];
        if (end2 != -1) ans += preSum[end2 + 1];
        return ans;
    }
}
