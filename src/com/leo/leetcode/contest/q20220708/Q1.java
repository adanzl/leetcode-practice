package com.leo.leetcode.contest.q20220708;

import com.leo.utils.LCUtil;

import java.util.Arrays;
import java.util.Comparator;
import java.util.TreeMap;

/**
 * 假设有若干信号发射源定时发送信号， signals[i] = [start, end) 表示第 i 个信号发射源运作的开始时间 start 和停止时间 end 。
 * 若调度员的接收设备同一时刻仅能接收一个发射源发出的信号，请判断调度员能否收到所有发射源的完整信号。
 * 注意：只有接收了一个信号源从开始到结束的所有信号才算完整信号。
 * 提示：
 * 1、0 <= signals.length <= 10^4
 * 2、signals[i].length == 2
 * 3、0 <= start_i < end_i <= 10^6
 * 链接：https://leetcode.cn/contest/zj-future2022/problems/WYKGLO/
 */
public class Q1 {

    public static void main(String[] args) {
        // false
        System.out.println(new Q1().canReceiveAllSignals(LCUtil.stringToInt2dArray("[[6,15],[13,20],[6,17]]")));
        // false
        System.out.println(new Q1().canReceiveAllSignals(LCUtil.stringToInt2dArray("[[0,40],[10,15],[20,30]]")));
    }

    public boolean canReceiveAllSignals(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        TreeMap<Integer, Integer> treeMap = new TreeMap<>();
        for (int[] ints : intervals) {
            Integer k = treeMap.floorKey(ints[0]);
            if (null != k && treeMap.get(k) > ints[0]) return false;
            treeMap.put(ints[0], ints[1]);
        }
        return true;
    }
}
