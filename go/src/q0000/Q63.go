/*
 * 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
 * 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
 * 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
 * 网格中的障碍物和空位置分别用 1 和 0 来表示。
 * 提示：
 * 1、m == obstacleGrid.length
 * 2、n == obstacleGrid[i].length
 * 3、1 <= m, n <= 100
 * 4、obstacleGrid[i][j] 为 0 或 1
 * 链接：https://leetcode-cn.com/problems/unique-paths-ii
 */
package main

import (
	"fmt"
	. "util"
)

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	if obstacleGrid[0][0] == 1 {
		return 0
	}
	var rows, cols = len(obstacleGrid), len(obstacleGrid[0])
	dp := make([]int, cols+1)
	dp[0] = 1
	for i := 0; i < rows; i++ {
		if i != 0 {
			dp[0] = 0
		}
		for j := 0; j < cols; j++ {
			nv := 0
			if obstacleGrid[i][j] == 0 {
				nv = dp[j+1] + dp[j]
			}
			dp[j+1] = nv
		}
	}
	return dp[cols]
}

func main() {
	// 2
	fmt.Println(uniquePathsWithObstacles(StringToInt2dArray("[[0,0,0],[0,1,0],[0,0,0]]")))
	// 0
	fmt.Println(uniquePathsWithObstacles(StringToInt2dArray("[[0,0],[0,1]]")))
	// 1
	fmt.Println(uniquePathsWithObstacles(StringToInt2dArray("[[0,1],[0,0]]")))
}
