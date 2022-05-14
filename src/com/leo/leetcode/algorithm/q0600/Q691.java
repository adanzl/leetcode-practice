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
        //
        System.out.println(new Q691().minStickers(new String[]{"and", "pound", "force", "human", "fair", "back", "sign", "course", "sight", "world", "close", "saw", "best", "fill", "late", "silent", "open", "noon", "seat", "cell", "take", "between", "it", "hundred", "hat", "until", "either", "play", "triangle", "stay", "separate", "season", "tool", "direct", "part", "student", "path", "ear", "grow", "ago", "main", "was", "rule", "element", "thing", "place", "common", "led", "support", "mean"}
                , "quietchord"));
        // 3
        System.out.println(new Q691().minStickers(new String[]{"with", "example", "science"}, "thehat"));
        // 3
        System.out.println(new Q691().minStickers(new String[]{"this", "island", "keep", "spring", "problem", "subject"}, "gasproper"));
        // -1
        System.out.println(new Q691().minStickers(new String[]{"notice", "possible"}, "basicbasic"));
        // 3
        System.out.println(new Q691().minStickers1(new String[]{"control", "heart", "interest", "stream", "sentence", "soil", "wonder", "them", "month", "slip", "table", "miss", "boat", "speak", "figure", "no", "perhaps", "twenty", "throw", "rich", "capital", "save", "method", "store", "meant", "life", "oil", "string", "song", "food", "am", "who", "fat", "if", "put", "path", "come", "grow", "box", "great", "word", "object", "stead", "common", "fresh", "the", "operate", "where", "road", "mean"}
                , "stoodcrease"));
    }

    // 使用位图作为key
    public int minStickers(String[] stickers, String target) {
        int[] stickerMarks = new int[stickers.length];
        int[][] stickerCount = new int[stickers.length][26];
        for (int i = 0; i < stickers.length; i++) {
            String sticker = stickers[i];
            for (int j = 0; j < sticker.length(); j++) stickerMarks[i] |= 1 << (sticker.charAt(j) - 'a');
            for (int j = 0; j < sticker.length(); j++)
                stickerCount[i][sticker.charAt(j) - 'a']++;
        }
        int[] mem = new int[1 << target.length()];
        Arrays.fill(mem, -100);
        return dfs(target, stickerMarks, stickerCount, (1 << target.length()) - 1, 0, mem);
    }

    int dfs(String target, int[] stickersMark, int[][] stickersCount, int targetMask, int count, int[] mMap) {
        int ret = Integer.MAX_VALUE, targetMark = 0;
        if (targetMask == 0) return count;
        if (mMap[targetMask] != -100) return mMap[targetMask];
        for (int i = 0; i < target.length(); i++)
            if ((targetMask & (1 << i)) > 0) targetMark |= 1 << (target.charAt(i) - 'a');
        for (int i = 0; i < stickersMark.length; i++) {
            if ((stickersMark[i] & targetMark) == 0) continue;
            int newTargetKey = targetMask;
            int[] cCount = new int[26], stickerCount = stickersCount[i];
            for (int j = 0; j < target.length(); j++) {
                if ((targetMask & (1 << j)) == 0) continue;
                char c = target.charAt(j);
                if (++cCount[c - 'a'] <= stickerCount[c - 'a']) {
                    newTargetKey &= ~(1 << j);
                }
            }
            int val = dfs(target, stickersMark, stickersCount, newTargetKey, count, mMap);
            if (val == -1) continue;
            ret = Math.min(ret, val + 1);
        }
        if (ret == Integer.MAX_VALUE) ret = -1;
        mMap[targetMask] = ret;
        return ret;
    }

    // 使用字符串作为key
    public int minStickers1(String[] stickers, String target) {
        int[] targetCount = new int[26], stickerMarks = new int[stickers.length];
        int[][] stickerCount = new int[stickers.length][26];
        for (int i = 0; i < target.length(); i++) targetCount[target.charAt(i) - 'a']++;
        for (int i = 0; i < stickers.length; i++) {
            String sticker = stickers[i];
            for (int j = 0; j < sticker.length(); j++) stickerMarks[i] |= 1 << (sticker.charAt(j) - 'a');
            for (int j = 0; j < sticker.length(); j++)
                stickerCount[i][sticker.charAt(j) - 'a']++;
        }
        return solve(stickerMarks, stickerCount, targetCount, 0, new HashMap<>());
    }

    int solve(int[] stickersMark, int[][] stickersCount, int[] targetCount, int count, Map<String, Integer> mMap) {
        StringBuilder sb = new StringBuilder();
        for (int num : targetCount) sb.append(num).append(":");
        String targetKey = sb.toString();
        if (mMap.containsKey(targetKey)) return mMap.get(targetKey);
        int targetMark = 0, ret = Integer.MAX_VALUE;
        for (int i = 0; i < targetCount.length; i++) {
            if (targetCount[i] != 0) targetMark |= 1 << i;
        }
        if (targetMark == 0) return count;
        for (int i = 0; i < stickersMark.length; i++) {
            if ((stickersMark[i] & targetMark) == 0) continue;
            int[] newTargetCount = new int[26];
            for (int j = 0; j < 26; j++) newTargetCount[j] = Math.max(0, targetCount[j] - stickersCount[i][j]);
            int val = solve(stickersMark, stickersCount, newTargetCount, count, mMap);
            if (val == -1) continue;
            ret = Math.min(ret, val + 1);
        }
        if (ret == Integer.MAX_VALUE) ret = -1;
        mMap.put(targetKey, ret);
        return ret;
    }
}
