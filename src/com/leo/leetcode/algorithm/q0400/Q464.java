package com.leo.leetcode.algorithm.q0400;

import java.util.HashMap;
import java.util.Map;

/**
 * 在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和 达到或超过 100 的玩家，即为胜者。
 * 如果我们将游戏规则改为 “玩家 不能 重复使用整数” 呢？
 * 例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。
 * 给定两个整数 maxChoosableInteger （整数池中可选择的最大数）和 desiredTotal（累计和），若先出手的玩家是否能稳赢则返回 true ，否则返回 false 。假设两位玩家游戏时都表现 最佳 。
 * 提示:
 * 1、1 <= maxChoosableInteger <= 20
 * 2、0 <= desiredTotal <= 300
 * 链接：https://leetcode.cn/problems/can-i-win
 */
public class Q464 {

    public static void main(String[] args) {
        // false
        System.out.println(new Q464().canIWin(5, 50));
        // false
        System.out.println(new Q464().canIWin(10, 11));
        // true
        System.out.println(new Q464().canIWin(10, 0));
        // true
        System.out.println(new Q464().canIWin(10, 1));
    }

    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        if(maxChoosableInteger > desiredTotal) return true;
        if(maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal) return false;
        Map<Integer, Map<Integer, Boolean>> mem = new HashMap<>();
        return canWin(mem, maxChoosableInteger, 0, desiredTotal);
    }

    boolean canWin(Map<Integer, Map<Integer, Boolean>> mem, int len, int mark, int desiredTotal) {
        if (desiredTotal <= 0) return false;
        if (mem.containsKey(mark) && mem.get(mark).containsKey(desiredTotal)) return mem.get(mark).get(desiredTotal);
        mem.putIfAbsent(mark, new HashMap<>());
        for (int i = 0; i < len; i++) {
            int mask = (1 << i);
            if ((mark & mask) == 0) {
                if (!canWin(mem, len, mark | mask, desiredTotal - (i + 1))) {
                    mem.get(mark).put(desiredTotal, true);
                    return true;
                }
            }
        }
        mem.get(mark).put(desiredTotal, false);
        return false;
    }

}
