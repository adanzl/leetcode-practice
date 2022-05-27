package com.leo.leetcode.lcci;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 有个内含单词的超大文本文件，给定任意两个不同的单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?
 * 提示： words.length <= 100000
 * 链接：https://leetcode.cn/problems/find-closest-lcci
 */
public class Q17_11 {

    public static void main(String[] args) {
        // 1
        System.out.println(new Q17_11().findClosest(stringToStringArray("[\"I\",\"am\",\"a\",\"student\",\"from\",\"a\",\"university\",\"in\",\"a\",\"city\"]"), "a", "student"));
    }

    public int findClosest(String[] words, String word1, String word2) {
        List<Integer> list1 = new ArrayList<>(), list2 = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(word1)) list1.add(i);
            else if (words[i].equals(word2)) list2.add(i);
        }
        int ret = Integer.MAX_VALUE;
        for (int idx : list1) {
            int idx2 = getIdx(list2, list2.size() - 1, idx);
            if (idx2 > 0) ret = Math.min(ret, Math.abs(list2.get(idx2 - 1) - idx));
            if (idx2 < list2.size()) ret = Math.min(ret, Math.abs(list2.get(idx2) - idx));
        }
        return ret;
    }

    int getIdx(List<Integer> list, int r, int target) {
        int l = 0;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (list.get(mid) < target) l = mid + 1;
            else r = mid - 1;
        }
        return l;
    }
}
