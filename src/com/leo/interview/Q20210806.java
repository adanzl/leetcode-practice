package com.leo.interview;

import java.util.HashSet;
import java.util.Set;

public class Q20210806 {


    public static void main(String[] args) {
        //  4
//        System.out.println(new Q20210806().calc(5, 17));
        //  19
//        System.out.println(new Q20210806().calc(5, 100000));
        for (int i = 5; i < 100; i++) {
            System.out.print(new Q20210806().calc(5, i));
        }
    }

    int calc(int start, int end) {
        if(start == end) return 0;
        Set<Integer> s = new HashSet<>();
        s.add(start);
        return func(s, end, 0);
    }

    int func(Set<Integer> s, int dest, int dept) {
        Set<Integer> nextSet = new HashSet<>();
        for (int item : s) {
            if (item - 1 == dest || item + 1 == dest || item * 2 == dest) return dept + 1;
            nextSet.add(item - 1);
            nextSet.add(item + 1);
            nextSet.add(item * 2);
        }
        return func(nextSet, dest, dept + 1);
    }
}
