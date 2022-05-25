package com.leo.leetcode.algorithm.q2200;

import com.leo.utils.TestCase;

import java.util.Stack;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 作为国王的统治者，你有一支巫师军队听你指挥。
 * 给你一个下标从 0 开始的整数数组 strength ，其中 strength[i] 表示第 i 位巫师的力量值。
 * 对于连续的一组巫师（也就是这些巫师的力量值是 strength 的 子数组），总力量 定义为以下两个值的 乘积 ：
 * 1、巫师中 最弱 的能力值。
 * 2、组中所有巫师的个人力量值 之和 。
 * 请你返回 所有 巫师组的 总 力量之和。由于答案可能很大，请将答案对 109 + 7 取余 后返回。
 * 子数组 是一个数组里 非空 连续子序列。
 * 提示：
 * 1、1 <= strength.length <= 10^5
 * 2、1 <= strength[i] <= 10^9
 * 链接：https://leetcode.cn/problems/sum-of-total-strength-of-wizards
 */
public class Q2281 {

    public static void main(String[] args) {
        TestCase tc = new TestCase("resources/algorithm/q2200/Q2281/Case001.txt");
        // 121473332
        System.out.println(new Q2281().totalStrength(stringToIntegerArray(tc.getData(0))));
        // 44
        System.out.println(new Q2281().totalStrength(stringToIntegerArray("[1,3,1,2]")));
        // 213
        System.out.println(new Q2281().totalStrength(stringToIntegerArray("[5,4,6]")));
        // 1
        System.out.println(new Q2281().totalStrength(stringToIntegerArray("[1]")));
    }

    // https://mp.weixin.qq.com/s?__biz=MzI2NzQ3OTQ1Mw==&mid=2247485030&idx=1&sn=b648c8a3c8a9b8fce625765fb345d233&chksm=eaff7694dd88ff825dd71a9b740dcba6711f192220c718361382b70534718b0d98936b5514c4&token=1764672036&lang=zh_CN#rd
    public int totalStrength(int[] strength) {
        int n = strength.length, MOD = 1_000_000_007;
        long ret = 0;
        int[] lPreMin = new int[n], rPreMin = new int[n];
        // 求前缀和数组，和左右两个三角形前缀和数组
        long[] preSum = new long[n + 1], lTriangle = new long[n + 1], rTriangle = new long[n + 1];
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && strength[i] <= strength[stack.peek()]) stack.pop();
            lPreMin[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
            preSum[i + 1] = (preSum[i] + strength[i]) % MOD;
            lTriangle[i + 1] = (lTriangle[i] + (long) strength[i] * (i + 1));
            rTriangle[i + 1] = (rTriangle[i] + (long) strength[i] * (n - i));
        }
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && strength[i] < strength[stack.peek()]) stack.pop();
            rPreMin[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
            int l = lPreMin[i], r = rPreMin[i];
            // 求左右三角形的面积
            long lSum = (getSum(lTriangle, 0, n) - getSum(lTriangle, 0, l + 1) - getSum(lTriangle, i + 1, n) - getSum(preSum, l + 1, i + 1) * (l + 1)) % MOD;
            long rSum = (getSum(rTriangle, 0, n) - getSum(rTriangle, 0, i) - getSum(rTriangle, r, n) - getSum(preSum, i, r) * (n - r)) % MOD;
            long longSum = (lSum * (r - i) + rSum * (i - l) - (long) (r - i) * (i - l) * strength[i] % MOD + MOD) % MOD;
            ret = (ret + longSum * strength[i]) % MOD;
        }
        return (int) ret;
    }

    long getSum(long[] preSum, int l, int r) {
        return preSum[r] - preSum[l];
    }

}
