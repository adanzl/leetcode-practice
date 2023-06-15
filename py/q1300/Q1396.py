"""
 * 地铁系统跟踪不同车站之间的乘客出行时间，并使用这一数据来计算从一站到另一站的平均时间。
 * 实现 UndergroundSystem 类：
 * 1、void checkIn(int id, string stationName, int t)
 *      通行卡 ID 等于 id 的乘客，在时间 t ，从 stationName 站进入
 *      乘客一次只能从一个站进入
 * 2、void checkOut(int id, string stationName, int t)
 *      通行卡 ID 等于 id 的乘客，在时间 t ，从 stationName 站离开
 * 3、double getAverageTime(string startStation, string endStation)
 *      返回从 startStation 站到 endStation 站的平均时间
 *      平均时间会根据截至目前所有从 startStation 站 直接 到达 endStation 站的行程进行计算，也就是从 startStation 站进入并从 endStation 离开的行程
 *      从 startStation 到 endStation 的行程时间与从 endStation 到 startStation 的行程时间可能不同
 *      在调用 getAverageTime 之前，至少有一名乘客从 startStation 站到达 endStation 站
 * 你可以假设对 checkIn 和 checkOut 方法的所有调用都是符合逻辑的。如果一名乘客在时间 t1 进站、时间 t2 出站，那么 t1 < t2 。所有时间都按时间顺序发生。
 * 提示：
 * 1、1 <= id, t <= 10^6
 * 2、1 <= stationName.length, startStation.length, endStation.length <= 10 次
 * 3、所有字符串由大小写英文字母与数字组成
 * 4、总共最多调用 checkIn、checkOut 和 getAverageTime 方法 2 * 10^4
 * 5、与标准答案误差在 10^-5 以内的结果都被视为正确结果
 * 链接：https://leetcode.cn/problems/design-underground-system/
"""


class UndergroundSystem:

    def __init__(self):
        self.startInfo = dict()
        self.table = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.startInfo[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startTime = self.startInfo[id][1]
        index = (self.startInfo[id][0], stationName)
        rec = self.table.get(index, (0, 0))
        self.table[index] = (rec[0] + t - startTime, rec[1] + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        index = (startStation, endStation)
        sum, amount = self.table[index]
        return sum / amount

if __name__ == '__main__':
    #
    # =============================
    undergroundSystem = UndergroundSystem()
    undergroundSystem.checkIn(45, "Leyton", 3)
    undergroundSystem.checkIn(45, "Leyton", 4)
    undergroundSystem.checkOut(45, "Waterloo", 15)
    print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))  #
    undergroundSystem.checkOut(45, "Waterloo", 18)
    print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))  #
    # =============================
    undergroundSystem = UndergroundSystem()
    undergroundSystem.checkIn(45, "Leyton", 3)
    undergroundSystem.checkIn(32, "Paradise", 8)
    undergroundSystem.checkIn(27, "Leyton", 10)
    undergroundSystem.checkOut(45, "Waterloo", 15)  # 乘客 45 "Leyton" -> "Waterloo" ，用时 15-3 = 12
    undergroundSystem.checkOut(27, "Waterloo", 20)  # 乘客 27 "Leyton" -> "Waterloo" ，用时 20-10 = 10
    undergroundSystem.checkOut(32, "Cambridge", 22)  # 乘客 32 "Paradise" -> "Cambridge" ，用时 22-8 = 14
    print(undergroundSystem.getAverageTime("Paradise", "Cambridge"))  # 返回 14.00000 。只有一个 "Paradise" -> "Cambridge" 的行程，(14) / 1 = 14
    print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))  # 返回 11.00000 。有两个 "Leyton" -> "Waterloo" 的行程，(10 + 12) / 2 = 11
    undergroundSystem.checkIn(10, "Leyton", 24)
    print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))  # 返回 11.00000
    undergroundSystem.checkOut(10, "Waterloo", 38)  # 乘客 10 "Leyton" -> "Waterloo" ，用时 38-24 = 14
    print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))  # 返回 12.00000 。有三个 "Leyton" -> "Waterloo" 的行程，(10 + 12 + 14) / 3 = 12
    # =============================
    undergroundSystem = UndergroundSystem()
    undergroundSystem.checkIn(10, "Leyton", 3)
    undergroundSystem.checkOut(10, "Paradise", 8)  # 乘客 10 "Leyton" -> "Paradise" ，用时 8-3 = 5
    print(undergroundSystem.getAverageTime("Leyton", "Paradise"))  # 返回 5.00000 ，(5) / 1 = 5
    undergroundSystem.checkIn(5, "Leyton", 10)
    undergroundSystem.checkOut(5, "Paradise", 16)  # 乘客 5 "Leyton" -> "Paradise" ，用时 16-10 = 6
    print(undergroundSystem.getAverageTime("Leyton", "Paradise"))  # 返回 5.50000 ，(5 + 6) / 2 = 5.5
    undergroundSystem.checkIn(2, "Leyton", 21)
    undergroundSystem.checkOut(2, "Paradise", 30)  # 乘客 2 "Leyton" -> "Paradise" ，用时 30-21 = 9
    print(undergroundSystem.getAverageTime("Leyton", "Paradise"))  # 返回 6.66667 ，(5 + 6 + 9) / 3 = 6.66667
