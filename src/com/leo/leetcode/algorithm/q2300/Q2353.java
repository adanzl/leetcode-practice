package com.leo.leetcode.algorithm.q2300;

import java.util.HashMap;
import java.util.Map;
import java.util.TreeSet;

import static com.leo.utils.LCUtil.stringToIntegerArray;
import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 设计一个支持下述操作的食物评分系统：
 * 1、修改 系统中列出的某种食物的评分。
 * 2、返回系统中某一类烹饪方式下评分最高的食物。
 * 实现 FoodRatings 类：
 * 1、FoodRatings(String[] foods, String[] cuisines, int[] ratings) 初始化系统。食物由 foods、cuisines 和 ratings 描述，长度均为 n 。
 * 2、foods[i] 是第 i 种食物的名字。
 * 3、cuisines[i] 是第 i 种食物的烹饪方式。
 * 4、ratings[i] 是第 i 种食物的最初评分。
 * 5、void changeRating(String food, int newRating) 修改名字为 food 的食物的评分。
 * 6、String highestRated(String cuisine) 返回指定烹饪方式 cuisine 下评分最高的食物的名字。如果存在并列，返回 字典序较小 的名字。
 * 注意，字符串 x 的字典序比字符串 y 更小的前提是：x 在字典中出现的位置在 y 之前，也就是说，要么 x 是 y 的前缀，或者在满足 x[i] != y[i] 的第一个位置 i 处，x[i] 在字母表中出现的位置在 y[i] 之前。
 * 提示：
 * 1、1 <= n <= 2 * 10^4
 * 2、n == foods.length == cuisines.length == ratings.length
 * 3、1 <= foods[i].length, cuisines[i].length <= 10
 * 4、foods[i]、cuisines[i] 由小写英文字母组成
 * 5、1 <= ratings[i] <= 10^8
 * 6、foods 中的所有字符串 互不相同
 * 7、在对 changeRating 的所有调用中，food 是系统中食物的名字。
 * 8、在对 highestRated 的所有调用中，cuisine 是系统中 至少一种 食物的烹饪方式。
 * 9、最多调用 changeRating 和 highestRated 总计 2 * 104 次
 * 链接：https://leetcode.cn/problems/design-a-food-rating-system
 */
public class Q2353 {

    public static void main(String[] args) {
//        FoodRatings foodRatings = new FoodRatings(stringToStringArray("[\"kimchi\", \"miso\", \"sushi\", \"moussaka\", \"ramen\", \"bulgogi\"]")
//                , stringToStringArray("[\"korean\", \"japanese\", \"japanese\", \"greek\", \"japanese\", \"korean\"]")
//                , stringToIntegerArray("[9, 12, 8, 15, 14, 7]"));
//        // "kimchi"
//        System.out.println(foodRatings.highestRated("korean"));
//        // "ramen"
//        System.out.println(foodRatings.highestRated("japanese"));
//        // "ramen" 是分数最高的日式料理，评分为 14 。
//        foodRatings.changeRating("sushi", 16); // "sushi" 现在评分变更为 16 。
//        // "sushi"
//        System.out.println(foodRatings.highestRated("japanese")); // 返回
//        foodRatings.changeRating("ramen", 16); // "ramen" 现在评分变更为 16 。
//        // "ramen"
//        System.out.println(foodRatings.highestRated("japanese")); // 返回
//        // "sushi" 和 "ramen" 的评分都是 16 。
//        // 但是，"ramen" 的字典序比 "sushi" 更小。
        FoodRatings foodRatings = new FoodRatings(stringToStringArray("[\"tjokfmxg\",\"xmiuwozpmj\",\"uqklk\",\"mnij\",\"iwntdyqxi\",\"cduc\",\"cm\",\"mzwfjk\"]")
                , stringToStringArray("[\"waxlau\",\"ldpiabqb\",\"ldpiabqb\",\"waxlau\",\"ldpiabqb\",\"waxlau\",\"waxlau\",\"waxlau\"]")
                , stringToIntegerArray("[9,13,7,16,10,17,16,17]"));
        foodRatings.changeRating("tjokfmxg", 19);
        System.out.println(foodRatings.highestRated("waxlau"));
        foodRatings.changeRating("uqklk", 7);
        System.out.println(foodRatings.highestRated("waxlau"));
        System.out.println(foodRatings.highestRated("waxlau"));
        foodRatings.changeRating("tjokfmxg", 14);
        System.out.println(foodRatings.highestRated("waxlau"));
        System.out.println(foodRatings.highestRated("waxlau"));
        foodRatings.changeRating("tjokfmxg", 4);
        System.out.println(foodRatings.highestRated("waxlau"));
        foodRatings.changeRating("mnij", 18);
        System.out.println(foodRatings.highestRated("waxlau"));
    }


    static class FoodRatings {

        Map<String, String> foodsCuisineMap = new HashMap<>(); // food-cuisine
        Map<String, Integer> foodsRatingMap = new HashMap<>(); // food-cuisine
        Map<String, TreeSet<Object[]>> cMap = new HashMap<>(); // cuisine- rating-name

        public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
            int n = foods.length;
            for (int i = 0; i < n; i++) {
                cMap.putIfAbsent(cuisines[i], new TreeSet<>((o1, o2) -> (int) o1[0] != (int) (o2[0]) ? (int) o2[0] - (int) (o1[0]) : ((String) o1[1]).compareTo((String) o2[1])));
                foodsCuisineMap.put(foods[i], cuisines[i]);
                foodsRatingMap.put(foods[i], ratings[i]);
                cMap.get(cuisines[i]).add(new Object[]{ratings[i], foods[i]});
            }
        }

        public void changeRating(String food, int newRating) {
            String cuisine = foodsCuisineMap.get(food);
            int rating = foodsRatingMap.get(food);
            cMap.get(cuisine).remove(new Object[]{rating, food});
            cMap.get(cuisine).add(new Object[]{newRating, food});
            foodsRatingMap.put(food, newRating);
        }

        public String highestRated(String cuisine) {
            if (!cMap.containsKey(cuisine) || cMap.get(cuisine).isEmpty()) return "";
            return (String) cMap.get(cuisine).first()[1];
        }
    }

}
