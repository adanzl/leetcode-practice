package com.leo.leetcode.algorithm.q0900;

import static com.leo.utils.LCUtil.stringToStringArray;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 给你一个日志数组 logs。每条日志都是以空格分隔的字串，其第一个字为字母与数字混合的 标识符 。
 * 有两种不同类型的日志：
 * 1、字母日志：除标识符之外，所有字均由小写字母组成
 * 2、数字日志：除标识符之外，所有字均由数字组成
 * 请按下述规则将日志重新排序：
 * 1、所有 字母日志 都排在 数字日志 之前。
 * 2、字母日志 在内容不同时，忽略标识符后，按内容字母顺序排序；在内容相同时，按标识符排序。
 * 3、数字日志 应该保留原来的相对顺序。
 * 返回日志的最终顺序。
 * 提示：
 * 1、1 <= logs.length <= 100
 * 2、3 <= logs[i].length <= 100
 * 3、logs[i] 中，字与字之间都用 单个 空格分隔
 * 4、题目数据保证 logs[i] 都有一个标识符，并且在标识符之后至少存在一个字
 * 链接：https://leetcode-cn.com/problems/reorder-data-in-log-files
 */
public class Q937 {

    public static void main(String[] args) {
        // ["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
        System.out.println(Arrays.toString(new Q937().reorderLogFiles(stringToStringArray("[\"a1 9 2 3 1\",\"g1 act car\",\"zo4 4 7\",\"ab1 off key dog\",\"a8 act zoo\",\"a2 act car\"]"))));
        // ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
        System.out.println(Arrays.toString(new Q937().reorderLogFiles(stringToStringArray("[\"dig1 8 1 5 1\",\"let1 art can\",\"dig2 3 6\",\"let2 own kit dig\",\"let3 art zero\"]"))));
        // ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
        System.out.println(Arrays.toString(new Q937().reorderLogFiles(stringToStringArray("[\"a1 9 2 3 1\",\"g1 act car\",\"zo4 4 7\",\"ab1 off key dog\",\"a8 act zoo\"]"))));
    }

    public String[] reorderLogFiles(String[] logs) {
        List<String[]> arr = new ArrayList<>();
        List<String> ret = new ArrayList<>();
        for (String log : logs) {
            int idx = log.indexOf(" ") + 1;
            if (Character.isDigit(log.charAt(idx))) continue;
            arr.add(new String[]{log, log.substring(idx), log.substring(0, idx - 1)});
        }
        arr.sort((o1, o2) -> o1[1].equals(o2[1]) ? o1[2].compareTo(o2[2]): o1[1].compareTo(o2[1]));
        for (String[] str : arr) ret.add(str[0]);
        for (String log : logs) {
            int idx = log.indexOf(" ") + 1;
            if (!Character.isDigit(log.charAt(idx))) continue;
            ret.add(log);
        }
        return ret.toArray(new String[0]);
    }
}
