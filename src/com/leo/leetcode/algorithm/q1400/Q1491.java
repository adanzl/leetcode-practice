package com.leo.leetcode.algorithm.q1400;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一个整数数组salary，数组里每个数都是 唯一的，其中 salary[i] 是第i个员工的工资。
 * 请你返回去掉最低工资和最高工资以后，剩下员工工资的平均值。
 * 提示：
 * 1、3 <= salary.length <= 100
 * 2、10^3<= salary[i] <= 10^6
 * 3、salary[i]是唯一的。
 * 4、与真实值误差在10^-5 以内的结果都将视为正确答案。
 *
 * 链接：https://leetcode-cn.com/problems/average-salary-excluding-the-minimum-and-maximum-salary
 */
public class Q1491 {
    public static void main(String[] args) {
        // 41111.1
        System.out.println(new Q1491().average(stringToIntegerArray("[48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]")));
        // 2500.0
        System.out.println(new Q1491().average(stringToIntegerArray("[4000,3000,1000,2000]")));
        // 2000.0
        System.out.println(new Q1491().average(stringToIntegerArray("[1000,2000,3000]")));
        // 3500.0
        System.out.println(new Q1491().average(stringToIntegerArray("[6000,5000,4000,3000,2000,1000]")));
        // 4750.0
        System.out.println(new Q1491().average(stringToIntegerArray("[8000,9000,2000,3000,6000,1000]")));
    }

    public double average(int[] salary) {
        int min = Math.min(salary[0], salary[1]), max = Math.max(salary[0], salary[1]);
        double ret = 0;
        for (int i = 2; i < salary.length; i++) {
            int v = salary[i];
            if(v > max) {
                ret += max;
                max = v;
                continue;
            }
            if (v < min) {
                ret += min;
                min = v;
                continue;
            }
            ret += v;
        }
        return ret / (salary.length - 2);
    }
}
