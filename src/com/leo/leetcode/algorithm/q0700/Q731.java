package com.leo.leetcode.algorithm.q0700;

import java.util.ArrayList;
import java.util.List;

/**
 * 实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内不会导致三重预订时，则可以存储这个新的日程安排。
 * MyCalendar 有一个 book(int start, int end)方法。它意味着在 start 到 end 时间内增加一个日程安排，
 * 注意，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end。
 * 当三个日程安排有一些时间上的交叉时（例如三个日程安排都在同一时间内），就会产生三重预订。
 * 每次调用 MyCalendar.book方法时，如果可以将日程安排成功添加到日历中而不会导致三重预订，返回 true。否则，返回 false 并且不要将该日程安排添加到日历中。
 * 请按照以下步骤调用MyCalendar 类: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
 * 提示：
 * 1、每个测试用例，调用 MyCalendar.book 函数最多不超过 1000次。
 * 2、调用函数 MyCalendar.book(start, end)时， start 和 end 的取值范围为 [0, 10^9]。
 * 链接：https://leetcode-cn.com/problems/my-calendar-ii
 */
public class Q731 {

    public static void main(String[] args) {
        MyCalendarTwo myCalendar = new MyCalendarTwo();
        System.out.println(myCalendar.book(10, 20)); // returns true
        System.out.println(myCalendar.book(50, 60)); // returns true
        System.out.println(myCalendar.book(10, 40)); // returns true
        System.out.println(myCalendar.book(5, 15)); // returns false
        System.out.println(myCalendar.book(5, 10)); // returns true
        System.out.println(myCalendar.book(25, 55)); // returns true
    }

    static class MyCalendarTwo {

        List<int[]> calender;
        List<int[]> overlay;

        public MyCalendarTwo() {
            calender = new ArrayList<>();
            overlay = new ArrayList<>();
        }

        public boolean book(int start, int end) {
            for (int[] date : overlay) {
                if (date[0] < end && start < date[1]) return false;
            }
            for (int[] date : calender) {
                if (date[0] < end && start < date[1]) {
                    overlay.add(new int[]{Math.max(start, date[0]), Math.min(end, date[1])});
                }
            }
            calender.add(new int[]{start, end});
            return true;
        }

    }

}
