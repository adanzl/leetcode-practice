package com.leo.leetcode.algorithm.q2300;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个下标从 0 开始长度为 n 的整数数组 buses ，其中 buses[i] 表示第 i 辆公交车的出发时间。
 * 同时给你一个下标从 0 开始长度为 m 的整数数组 passengers ，其中 passengers[j] 表示第 j 位乘客的到达时间。
 * 所有公交车出发的时间互不相同，所有乘客到达的时间也互不相同。
 * 给你一个整数 capacity ，表示每辆公交车 最多 能容纳的乘客数目。
 * 每位乘客都会搭乘下一辆有座位的公交车。如果你在 y 时刻到达，公交在 x 时刻出发，满足 y <= x  且公交没有满，那么你可以搭乘这一辆公交。最早 到达的乘客优先上车。
 * 返回你可以搭乘公交车的最晚到达公交站时间。你 不能 跟别的乘客同时刻到达。
 * 注意：数组 buses 和 passengers 不一定是有序的。
 * 提示：
 * 1、n == buses.length
 * 2、m == passengers.length
 * 3、1 <= n, m, capacity <= 10^5
 * 4、2 <= buses[i], passengers[i] <= 10^9
 * 5、buses 中的元素 互不相同 。
 * 6、passengers 中的元素 互不相同 。
 * 链接：https://leetcode.cn/problems/the-latest-time-to-catch-a-bus
 *
 * 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */
public class Q2332 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q2332().latestTimeCatchTheBus(stringToIntegerArray("[2]"), stringToIntegerArray("[2]"), 2));
        // 20
        System.out.println(new Q2332().latestTimeCatchTheBus(stringToIntegerArray("[20,30,10]"), stringToIntegerArray("[19,13,26,4,25,11,21]"), 2));
        // 16
        System.out.println(new Q2332().latestTimeCatchTheBus(stringToIntegerArray("[10,20]"), stringToIntegerArray("[2,17,18,19]"), 2));
    }

    public int latestTimeCatchTheBus(int[] buses, int[] passengers, int capacity) {
        Arrays.sort(passengers);
        Arrays.sort(buses);
        Set<Integer> set = new HashSet<>();
        for (int p : passengers) set.add(p);
        int ret = 0, i0 = 0;
        for (int bus : buses) {
            int count = 0;
            for (; count < capacity && i0 < passengers.length; count++) {
                if (passengers[i0] <= bus) i0++;
                else break;
            }
            int v;
            if (count < capacity) { // not full
                v = bus;
            } else {
                v = passengers[i0 - 1];
            }
            while (set.contains(v)) v--;
            ret = Math.max(ret, v);
        }
        return ret;
    }


}
