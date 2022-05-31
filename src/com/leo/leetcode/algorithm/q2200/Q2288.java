package com.leo.leetcode.algorithm.q2200;

/**
 * 句子 是由若干个单词组成的字符串，单词之间用单个空格分隔，其中每个单词可以包含数字、小写字母、和美元符号 '$' 。如果单词的形式为美元符号后跟着一个非负实数，那么这个单词就表示一个价格。
 * 例如 "$100"、"$23" 和 "$6.75" 表示价格，而 "100"、"$" 和 "2$3" 不是。
 * 注意：本题输入中的价格均为整数。
 * 给你一个字符串 sentence  和一个整数 discount 。对于每个表示价格的单词，都在价格的基础上减免 discount% ，并 更新 该单词到句子中。所有更新后的价格应该表示为一个 恰好保留小数点后两位 的数字。
 * 返回表示修改后句子的字符串。
 * 提示：
 * 1、1 <= sentence.length <= 10^5
 * 2、sentence 由小写英文字母、数字、' ' 和 '$' 组成
 * 3、sentence 不含前导和尾随空格
 * 4、sentence 的所有单词都用单个空格分隔
 * 5、所有价格都是 正 整数且不含前导零
 * 6、所有价格 最多 为  10 位数字
 * 7、0 <= discount <= 100
 * 链接：https://leetcode.cn/problems/apply-discount-to-prices
 */
public class Q2288 {
    public static void main(String[] args) {
        // "there are $0.50 $1.00 and 5$ candies in the shop"
        System.out.println(new Q2288().discountPrices("there are $1 $2 and 5$ candies in the shop", 50));
        // "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"
        System.out.println(new Q2288().discountPrices("1 2 $3 4 $5 $6 7 8$ $9 $10$", 100));
    }

    public String discountPrices(String sentence, int discount) {
        String[] strings = sentence.split(" ");
        StringBuilder ret = new StringBuilder();
        for (String str : strings) {
            if (str.length() > 0 && str.charAt(0) == '$') {
                String sub = str.substring(1);
                if (isNum(sub)) {
                    double num = Double.parseDouble(sub);
                    double number = num - num * discount / 100;
                    ret.append("$").append(String.format("%.2f", number)).append(" ");
                } else {
                    ret.append(str).append(" ");
                }
            } else {
                ret.append(str).append(" ");
            }
        }
        return ret.substring(0, ret.length() - 1);
    }

    boolean isNum(String str) {
        if (str.length() == 0) return false;
        for (char c : str.toCharArray()) if (!Character.isDigit(c)) return false;
        return true;
    }
}
