/*
 * 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
 * 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
 * 假设每一种面额的硬币有无限个。
 * 题目数据保证结果符合 32 位带符号整数。
 * 提示：
 * 1、1 <= coins.length <= 300
 * 2、1 <= coins[i] <= 5000
 * 3、coins 中的所有值 互不相同
 * 4、0 <= amount <= 5000
 * 链接：https://leetcode-cn.com/problems/coin-change-2
 */
package main

import (
	"fmt"
	"util"
)

func change(amount int, coins []int) int {
	dp := make([]int, amount+1)
	dp[0] = 1
	for _, coin := range coins {
		for i := coin; i <= amount; i++ {
			dp[i] += dp[i-coin]
		}
	}
	return dp[amount]
}

func main() {
	// 4
	fmt.Println(change(5, LCUtil.StringToIntArray("[1, 2, 5]")))
	// 0
	fmt.Println(change(3, LCUtil.StringToIntArray("[2]")))
	// 1
	fmt.Println(change(10, LCUtil.StringToIntArray("[10]")))
	// 1
	fmt.Println(change(0, LCUtil.StringToIntArray("[1,2,5]")))
}
