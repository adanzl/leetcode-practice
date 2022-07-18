package com.leo.leetcode.algorithm.q0400;

/**
 * 有 buckets 桶液体，其中 正好有一桶 含有毒药，其余装的都是水。它们从外观看起来都一样。
 * 为了弄清楚哪只水桶含有毒药，你可以喂一些猪喝，通过观察猪是否会死进行判断。
 * 不幸的是，你只有 minutesToTest 分钟时间来确定哪桶液体是有毒的。
 * 喂猪的规则如下：
 * 1、选择若干活猪进行喂养
 * 2、可以允许小猪同时饮用任意数量的桶中的水，并且该过程不需要时间。
 * 3、小猪喝完水后，必须有 minutesToDie 分钟的冷却时间。在这段时间里，你只能观察，而不允许继续喂猪。
 * 4、过了 minutesToDie 分钟后，所有喝到毒药的猪都会死去，其他所有猪都会活下来。
 * 5、重复这一过程，直到时间用完。
 * 6、给你桶的数目 buckets ，minutesToDie 和 minutesToTest ，返回 在规定时间内判断哪个桶有毒所需的 最小 猪数 。
 * 提示：
 * 1、1 <= buckets <= 1000
 * 2、1 <= minutesToDie <= minutesToTest <= 100
 * 链接：https://leetcode.cn/problems/poor-pigs
 */
public class Q458 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q458().poorPigs(1, 1, 1));
        // 5
        System.out.println(new Q458().poorPigs(1000, 15, 60));
        // 2
        System.out.println(new Q458().poorPigs(4, 15, 15));
        // 2
        System.out.println(new Q458().poorPigs(4, 15, 30));
    }

    /**
     * 经过所有实验，一只小猪能有多少种状态？第一轮就死、第二轮死、...、第n轮死，以及生还，所以一共有n + 1种状态
     * n + 1种状态所携带的信息为log_2(n + 1)比特，这也是一只小猪最多提供的信息量
     * 而”buckets瓶液体中哪一瓶是毒“这件事，也有buckets种可能性，所以需要的信息量是log_2(buckets)
     * 注：以上所有事件、状态都是先验等概的，所以可以直接对2取对数得到信息熵
     */
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int n = minutesToTest / minutesToDie, ret = 0;
        double max = 1;
        while (max < buckets) {
            ret++;
            max = Math.pow(n + 1, ret);
        }
        return ret;
    }
}
