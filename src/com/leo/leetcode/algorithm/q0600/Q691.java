package com.leo.leetcode.algorithm.q0600;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * 我们有 n 种不同的贴纸。每个贴纸上都有一个小写的英文单词。
 * 您想要拼写出给定的字符串 target ，方法是从收集的贴纸中切割单个字母并重新排列它们。如果你愿意，你可以多次使用每个贴纸，每个贴纸的数量是无限的。
 * 返回你需要拼出 target 的最小贴纸数量。如果任务不可能，则返回 -1 。
 * 注意：在所有的测试用例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选择的，并且 target 被选择为两个随机单词的连接。
 * 提示:
 * 1、n == stickers.length
 * 2、1 <= n <= 50
 * 3、1 <= stickers[i].length <= 10
 * 4、1 <= target <= 15
 * stickers[i] 和 target 由小写英文单词组成
 * 链接：https://leetcode.cn/problems/stickers-to-spell-word
 */
public class Q691 {

    public static void main(String[] args) {
        // 3
        System.out.println(new Q691().minStickers(new String[]{"this", "island", "keep", "spring", "problem", "subject"}, "gasproper"));
        // -1
        System.out.println(new Q691().minStickers(new String[]{"notice", "possible"}, "basicbasic"));
        // 3
        System.out.println(new Q691().minStickers(new String[]{"with", "example", "science"}, "thehat"));
        // 3
        System.out.println(new Q691().minStickers(new String[]{"control", "heart", "interest", "stream", "sentence", "soil", "wonder", "them", "month", "slip", "table", "miss", "boat", "speak", "figure", "no", "perhaps", "twenty", "throw", "rich", "capital", "save", "method", "store", "meant", "life", "oil", "string", "song", "food", "am", "who", "fat", "if", "put", "path", "come", "grow", "box", "great", "word", "object", "stead", "common", "fresh", "the", "operate", "where", "road", "mean"}
                , "stoodcrease"));
    }

    Map<String, Integer> mMap = new HashMap<>();

    public int minStickers(String[] stickers, String target) {
        int[] targetCount = new int[26], stickerMarks = new int[stickers.length];
        int[][] stickerCount = new int[stickers.length][26];
        for (int i = 0; i < target.length(); i++) targetCount[target.charAt(i) - 'a']++;
        for (int i = 0; i < stickers.length; i++) {
            String sticker = stickers[i];
            for (int j = 0; j < sticker.length(); j++) stickerMarks[i] |= 1 << (sticker.charAt(j) - 'a');
            for (int j = 0; j < sticker.length(); j++)
                stickerCount[i][sticker.charAt(j) - 'a']++;
        }
        return dfs(stickerMarks, stickerCount, targetCount, 0);
    }

    int dfs(int[] stickersMark, int[][] stickersCount, int[] targetCount, int count) {
        int targetMark = 0, ret = Integer.MAX_VALUE;
        for (int i = 0; i < targetCount.length; i++) {
            if (targetCount[i] != 0) targetMark |= 1 << i;
        }
        if (targetMark == 0) return count;
        String targetKey = Arrays.toString(targetCount);
        if (mMap.containsKey(targetKey)) return mMap.get(targetKey);
        for (int i = 0; i < stickersMark.length; i++) {
            if ((stickersMark[i] & targetMark) == 0) continue;
            int[] newTargetCount = new int[26];
            for (int j = 0; j < 26; j++) newTargetCount[j] = Math.max(0, targetCount[j] - stickersCount[i][j]);
            int val = dfs(stickersMark, stickersCount, newTargetCount, count);
            if (val == -1) continue;
            ret = Math.min(ret, val + 1);
        }
        if (ret == Integer.MAX_VALUE) ret = -1;
        mMap.put(targetKey, ret);
        return ret;
    }
}
