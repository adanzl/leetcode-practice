package com.leo.leetcode.algorithm.q0500;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 假设 Andy 和 Doris 想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
 * 你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设答案总是存在。
 * 提示:
 * 1、1 <= list1.length, list2.length <= 1000
 * 2、1 <= list1[i].length, list2[i].length <= 30
 * 3、list1[i] 和 list2[i] 由空格 ' ' 和英文字母组成。
 * 4、list1 的所有字符串都是 唯一 的。
 * 5、list2 中的所有字符串都是 唯一 的。
 * 链接：https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists
 */
public class Q599 {

    public static void main(String[] args) {
        // ["Shogun"]
        System.out.println(Arrays.toString(new Q599().findRestaurant(
                stringToStringArray("[\"Shogun\", \"Tapioca Express\", \"Burger King\", \"KFC\"]"),
                stringToStringArray("[\"Piatti\", \"The Grill at Torrey Pines\", \"Hungry Hunter Steakhouse\", \"Shogun\"]"))));
        // ["Shogun"]
        System.out.println(Arrays.toString(new Q599().findRestaurant(
                stringToStringArray("[\"Shogun\", \"Tapioca Express\", \"Burger King\", \"KFC\"]"),
                stringToStringArray("[\"KFC\", \"Shogun\", \"Burger King\"]"))));
    }

    public String[] findRestaurant(String[] list1, String[] list2) {
        int len = Integer.MAX_VALUE;
        List<String> ret = new ArrayList<>();
        for (int i = 0; i < list1.length; i++) {
            for (int j = 0; j < list2.length; j++) {
                if (list1[i].equals(list2[j])) {
                    if (i + j < len) {
                        len = i + j;
                        ret = new ArrayList<>();
                        ret.add(list1[i]);
                    } else if (i + j == len) {
                        ret.add(list1[i]);
                    }
                }
            }
        }
        return ret.toArray(new String[0]);
    }
}
