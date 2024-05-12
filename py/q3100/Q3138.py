"""
 * 给你一个字符串 s ，它由某个字符串 t 和它的 同位字符串 连接而成。
 * 请你返回字符串 t 的 最小 可能长度。
 * 同位字符串 指的是重新排列一个单词得到的另外一个字符串，原来字符串中的每个字符在新字符串中都恰好只使用一次。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/minimum-length-of-anagram-concatenation/
"""
import copy


class Solution:

    def minAnagramLength(self, s: str) -> int:
        pre_cnt, n = [[0] * 26], len(s)
        for c in s:
            cnt = copy.copy(pre_cnt[-1])
            cnt[ord(c) - ord('a')] += 1
            pre_cnt.append(cnt)

        def check(ln):
            val = pre_cnt[ln]
            for i in range(ln + ln, n + 1, ln):
                for a, b, c in zip(pre_cnt[i], pre_cnt[i - ln], val):
                    if a - b != c:
                        return False
            return True

        arr = set()
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                arr.add(i)
                arr.add(n // i)
        arr = sorted(arr)
        for v in arr:
            if check(v):
                return v
        return n


if __name__ == '__main__':
    # 15
    print(Solution().minAnagramLength("gonwueihxyrvyikvoixnywyirehkgukunwhxyveyigoriieoynhurykwxgviohinygikuxwyvreiinogehukwvryyxkgwyyoixuirhvenykorinieywgvxhuyrywveiukiohngxywnoihkvryiuegxrvnoygywhiuekixoivnxyegikrhwyunwhyygikureoixvyuhegxwkvinoiyrivkxenryogwyuhixiehnygkroyuiwvvinroxyhuyegwkirvuxigyieownyhkoynhigkyvwiurxekiweyniovhxugryuyivxkwiyorhegnivriohwuxyengykoyrukvghxyneiwiynyixukvighewrovhiuiweryxnygokgwoyyixkuvihenrgixuhnyerkwyviovnhrygyxukioweioeiykhiurvnwxygvrygweixouiyknh"))
    # 2
    print(Solution().minAnagramLength("abba"))
    # 5
    print(Solution().minAnagramLength("lbuorourlb"))
    # 4
    print(Solution().minAnagramLength("cdef"))
