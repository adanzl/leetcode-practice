package com.leo.leetcode.algorithm.q1800;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个浮点数 hour ，表示你到达办公室可用的总通勤时间。
 * 要到达办公室，你必须按给定次序乘坐 n 趟列车。另给你一个长度为 n 的整数数组 dist ，其中 dist[i] 表示第 i 趟列车的行驶距离（单位是千米）。
 * 每趟列车均只能在整点发车，所以你可能需要在两趟列车之间等待一段时间。
 * 例如，第 1 趟列车需要 1.5 小时，那你必须再等待 0.5 小时，搭乘在第 2 小时发车的第 2 趟列车。
 * 返回能满足你准时到达办公室所要求全部列车的 最小正整数 时速（单位：千米每小时），如果无法准时到达，则返回 -1 。
 * 生成的测试用例保证答案不超过 107 ，且 hour 的 小数点后最多存在两位数字 。
 * 提示：
 * 1、n == dist.length
 * 2、1 <= n <= 10^5
 * 3、1 <= dist[i] <= 10^5
 * 4、1 <= hour <= 10^9
 * 5、hours 中，小数点后最多存在两位数字
 * 链接：https://leetcode-cn.com/problems/minimum-speed-to-arrive-on-time
 */
public class Q1870 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q1870().minSpeedOnTime(stringToIntegerArray("[1,3,2]"), 2.7));
        // 1
        System.out.println(new Q1870().minSpeedOnTime(stringToIntegerArray("[1,3,2]"), 6));
        // -1
        System.out.println(new Q1870().minSpeedOnTime(stringToIntegerArray("[1,3,2]"), 1.9));
    }

    public int minSpeedOnTime(int[] dist, double hour) {
        int ret = -1, l = 1, r = 1_000_000_000;
        while (l <= r) {
            int mid = l + ((r - l) >> 1);
            double sum = 0;
            for (double d : dist) {
                sum = Math.ceil(sum);
                sum += d / mid;
                if (sum > hour) break;
            }
            if (sum > hour) l = mid + 1;
            else {
                ret = mid;
                r = mid - 1;
            }
        }
        return ret;
    }
}
