package com.leo.leetcode.lcp;

import java.util.HashMap;
import java.util.Map;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 小扣打算去秋日市集，由于游客较多，小扣的移动速度受到了人流影响：
 * 1、小扣从 x 号站点移动至 x + 1 号站点需要花费的时间为 inc；
 * 2、小扣从 x 号站点移动至 x - 1 号站点需要花费的时间为 dec。
 * 现有 m 辆公交车，编号为 0 到 m-1。小扣也可以通过搭乘编号为 i 的公交车，从 x 号站点移动至 jump[i]*x 号站点，耗时仅为 cost[i]。小扣可以搭乘任意编号的公交车且搭乘公交次数不限。
 * 假定小扣起始站点记作 0，秋日市集站点记作 target，请返回小扣抵达秋日市集最少需要花费多少时间。由于数字较大，最终答案需要对 1000000007 (1e9 + 7) 取模。
 * 注意：小扣可在移动过程中到达编号大于 target 的站点
 * 提示：
 * 1、1 <= target <= 10^9
 * 2、1 <= jump.length, cost.length <= 10
 * 3、2 <= jump[i] <= 10^6
 * 4、1 <= inc, dec, cost[i] <= 10^6
 * 链接：https://leetcode.cn/problems/meChtZ
 */
public class LCP20 {

    public static void main(String[] args) {
        // 556489627
        System.out.println(new LCP20().busRapidTransit(954116209, 725988, 636911
                , stringToIntegerArray("[524425,158389]")
                , stringToIntegerArray("[41881,941330]")));
        // 782553489
        System.out.println(new LCP20().busRapidTransit(983423205, 448232, 963363
                , stringToIntegerArray("[38856,505823,835262,569086,958567,630647,350011,311421,898695,57358]")
                , stringToIntegerArray("[460603,941593,107678,409305,899055,915790,299351,563865,516575,747521]")));
        // 10953125
        System.out.println(new LCP20().busRapidTransit(1_000_000_000, 1, 1, stringToIntegerArray("[2]"), stringToIntegerArray("[1000000]")));
        // 33
        System.out.println(new LCP20().busRapidTransit(31, 5, 3, stringToIntegerArray("[6]"), stringToIntegerArray("[10]")));
        // 26
        System.out.println(new LCP20().busRapidTransit(612, 4, 5, stringToIntegerArray("[3,6,8,11,5,10,4]"), stringToIntegerArray("[4,7,6,3,7,6,4]")));
    }

    Map<Long, Long> mem = new HashMap<>();

    public int busRapidTransit(int target, int inc, int dec, int[] jump, int[] cost) {
        int MOD = 1_000_000_007;
        long ret = busRapidTransit((long) target, inc, dec, jump, cost);
        return (int) (ret % MOD);
    }

    public long busRapidTransit(long target, int inc, int dec, int[] jump, int[] cost) {
        if (target == 0) return 0;
        if (target == 1) return inc;
        if (mem.containsKey(target)) return Math.toIntExact(mem.get(target));
        long ret = target * inc;
        for (int j = 0; j < jump.length; j++) {
            long len = jump[j], c = cost[j];
            long q = target / len, r = target % len;
            if (r == 0) {
                ret = Math.min(ret, c + busRapidTransit(q, inc, dec, jump, cost));
            } else {
                // walk forward
                ret = Math.min(ret, c + r * inc + busRapidTransit(q, inc, dec, jump, cost));
                // walk back
                ret = Math.min(ret, busRapidTransit(q + 1, inc, dec, jump, cost) + c + (len - r) * dec);
            }
        }
        mem.put(target, ret);
        return ret;
    }

}
