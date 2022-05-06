package com.leo.leetcode.algorithm.q0700;

import java.util.HashSet;
import java.util.Set;

/**
 * 给你一个字符串 jewels 代表石头中宝石的类型，另有一个字符串 stones 代表你拥有的石头。
 * stones 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
 * 字母区分大小写，因此 "a" 和 "A" 是不同类型的石头。
 * 提示：
 * 1、1 <= jewels.length, stones.length <= 50
 * 2、jewels 和 stones 仅由英文字母组成
 * 3、jewels 中的所有字符都是 唯一的
 * 链接：https://leetcode-cn.com/problems/jewels-and-stones
 */
public class Q771 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q771().numJewelsInStones("aA", "aAAbbbb"));
        // 0
        System.out.println(new Q771().numJewelsInStones("z", "ZZ"));
    }

    public int numJewelsInStones(String jewels, String stones) {
        Set<Character> set = new HashSet<>();
        int ret = 0;
        for (char c : jewels.toCharArray()) set.add(c);
        for (char c : stones.toCharArray()) {
            if (set.contains(c)) ret++;
        }
        return ret;
    }
}
