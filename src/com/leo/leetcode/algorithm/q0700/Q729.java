package com.leo.leetcode.algorithm.q0700;

import java.util.TreeMap;

/**
 * 实现一个 MyCalendar 类来存放你的日程安排。如果要添加的日程安排不会造成 重复预订 ，则可以存储这个新的日程安排。
 * 当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生 重复预订 。
 * 日程可以用一对整数 start 和 end 表示，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end 。
 * 实现 MyCalendar 类：
 * 1、MyCalendar() 初始化日历对象。
 * 2、boolean book(int start, int end) 如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 true 。否则，返回 false 并且不要将该日程安排添加到日历中。
 * 提示：
 * 1、0 <= start < end <= 10^9
 * 2、每个测试用例，调用 book 方法的次数最多不超过 1000 次。
 * 链接：https://leetcode-cn.com/problems/my-calendar-i
 */
public class Q729 {

    public static void main(String[] args) {
        MyCalendar myCalendar = new MyCalendar();
        System.out.println(myCalendar.book(19, 30)); // return True
        System.out.println(myCalendar.book(13, 32)); // return False
        System.out.println(myCalendar.book(20, 30)); // return False
    }

}

class MyCalendar {
    TreeMap<Integer, Integer> calendar;

    MyCalendar() {
        calendar = new TreeMap<>();
    }

    public boolean book(int start, int end) {
        Integer prev = calendar.floorKey(start), next = calendar.ceilingKey(start);
        if ((prev == null || calendar.get(prev) <= start) &&
                (next == null || end <= next)) {
            calendar.put(start, end);
            return true;
        }
        return false;
    }
}
