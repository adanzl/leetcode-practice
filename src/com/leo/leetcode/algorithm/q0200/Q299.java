package com.leo.leetcode.algorithm.q0200;

/**
 * 你在和朋友一起玩 猜数字（Bulls and Cows）游戏，该游戏规则如下：
 * 1、你写出一个秘密数字，并请朋友猜这个数字是多少。
 * 2、朋友每猜测一次，你就会给他一个提示，告诉他的猜测数字中有多少位属于数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位属于数字猜对了但是位置不对（称为“Cows”, 奶牛）。
 * 3、朋友根据提示继续猜，直到猜出秘密数字。
 * 请写出一个根据秘密数字和朋友的猜测数返回提示的函数，返回字符串的格式为 xAyB ，x 和 y 都是数字，A 表示公牛，用 B 表示奶牛。
 * 1、xA 表示有 x 位数字出现在秘密数字中，且位置都与秘密数字一致。
 * 2、yB 表示有 y 位数字出现在秘密数字中，但位置与秘密数字不一致。
 * 请注意秘密数字和朋友的猜测数都可能含有重复数字，每位数字只能统计一次。
 * 说明: 你可以假设秘密数字和朋友的猜测数都只包含数字，并且它们的长度永远相等。f
 * 链接：https://leetcode-cn.com/problems/bulls-and-cows
 */

public class Q299 {

    public static void main(String[] args) {
        // "0A4B"
        System.out.println(new Q299().getHint("1122", "2211"));
        // "1A3B"
        System.out.println(new Q299().getHint("1807", "7810"));
        // "1A1B"
        System.out.println(new Q299().getHint("1123", "0111"));
    }

    public String getHint(String secret, String guess) {
        int A = 0, B = 0;
        int[] markS = new int[10], markG = new int[10];
        char[] strS = secret.toCharArray(), strG = guess.toCharArray();
        for (int i = 0; i < secret.length(); i++) {
            if (strS[i] == strG[i]) A++;
            else {
                markS[strS[i] - '0']++;
                markG[strG[i] - '0']++;
            }
        }
        for (int i = 0; i < markG.length; i++) B += Math.min(markS[i], markG[i]);
        StringBuilder stringBuilder = new StringBuilder(); // 这个地方使用StringBuilder会快很多
        return stringBuilder.append(A).append('A').append(B).append('B').toString();
    }

}
