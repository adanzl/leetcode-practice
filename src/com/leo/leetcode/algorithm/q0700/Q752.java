package com.leo.leetcode.algorithm.q0700;

import java.util.*;

import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。
 * 每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
 * 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
 * 列表 deadEnds 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
 * 字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。
 * 提示：
 * 1、1 <= deadEnds.length <= 500
 * 2、deadEnds[i].length == 4
 * 3、target.length == 4
 * 4、target 不在 deadEnds 之中
 * 5、target 和 deadEnds[i] 仅由若干位数字组成
 * 链接：https://leetcode-cn.com/problems/open-the-lock
 */
public class Q752 {

    public static void main(String[] args) {
        // -1
        System.out.println(new Q752().openLock(stringToStringArray("[\"0000\"]"), "8888"));
        // 6
        System.out.println(new Q752().openLock(stringToStringArray("[\"0201\",\"0101\",\"0102\",\"1212\",\"2002\"]"), "0202"));
        // 1
        System.out.println(new Q752().openLock(stringToStringArray("[\"8888\"]"), "0009"));
        // -1
        System.out.println(new Q752().openLock(stringToStringArray("[\"8887\",\"8889\",\"8878\",\"8898\",\"8788\",\"8988\",\"7888\",\"9888\"]"), "8888"));
    }

    public int openLock(String[] deadEnds, String target) {
        Set<String> deadSet = new HashSet<>(Arrays.asList(deadEnds));
        if(deadSet.contains("0000")) return -1;
        Set<String> visited = new HashSet<>();
        int ret = 0;
        Queue<String> q = new ArrayDeque<>();
        q.add("0000");
        visited.add("0000");
        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0 && !q.isEmpty()) {
                String word = q.poll();
//                System.out.print("-" + word);
                if (word.equals(target)) return ret;
                for (String next : nextCode(word)) {
                    if (!deadSet.contains(next) && !visited.contains(next)) {
                        q.add(next);
                        visited.add(next);
                    }
                }
            }
//            System.out.print("[" + ret +"]");
            ret++;
        }
        return -1;
    }

    List<String> nextCode(String code) {
        List<String> ret = new ArrayList<>();
        char[] str = code.toCharArray();
        for (int i = 0; i < str.length; i++) {
            char c = str[i];
            str[i] = (char) ((c - '0' + 11) % 10 + '0');
            ret.add(new String(str));
            str[i] = (char) ((c - '0' + 9) % 10 + '0');
            ret.add(new String(str));
            str[i] = c;
        }
        return ret;
    }
}
