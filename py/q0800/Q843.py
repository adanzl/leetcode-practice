"""
 * 给你一个由 不同 字符串组成的单词列表 words ，其中 words[i] 长度均为 6 。words 中的一个单词将被选作秘密单词 secret 。
 * 另给你一个辅助对象 Master ，你可以调用 Master.guess(word) 来猜单词，其中参数 word 长度为 6 且必须是 words 中的字符串。
 * Master.guess(word) 将会返回如下结果：
 * 1、如果 word 不是 words 中的字符串，返回 -1 ，或者
 * 2、一个整数，表示你所猜测的单词 word 与 秘密单词 secret 的准确匹配（值和位置同时匹配）的数目。
 * 每组测试用例都会包含一个参数 allowedGuesses ，其中 allowedGuesses 是你可以调用 Master.guess(word) 的最大次数。
 * 对于每组测试用例，在不超过允许猜测的次数的前提下，你应该调用 Master.guess 来猜出秘密单词。最终，你将会得到以下结果：
 * 1、如果你调用 Master.guess 的次数大于 allowedGuesses 所限定的次数或者你没有用 Master.guess 猜到秘密单词，
 *  则得到 "Either you took too many guesses, or you did not find the secret word." 。
 * 2、如果你调用 Master.guess 猜到秘密单词，且调用 Master.guess 的次数小于或等于 allowedGuesses ，
 *  则得到 "You guessed the secret word correctly." 。
 * 生成的测试用例保证你可以利用某种合理的策略（而不是暴力）猜到秘密单词。
 * 提示：
 * 1、1 <= words.length <= 100
 * 2、words[i].length == 6
 * 3、words[i] 仅由小写英文字母组成
 * 4、words 中所有字符串 互不相同
 * 5、secret 存在于 words 中
 * 6、10 <= allowedGuesses <= 30
 * 链接：https://leetcode.cn/problems/guess-the-word/
"""

from functools import cache
from typing import List

#
# @lc app=leetcode.cn id=843 lang=python3
#
# [843] 猜猜这个单词
#


# @lc code=start
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:

    def __init__(self, words, s: str) -> None:
        self.words = words[:]
        self.s = s
        self.cnt = 0

    def guess(self, word: str) -> int:
        if word not in self.words: return -1
        ans = 0
        self.cnt += 1
        for c1, c2 in zip(self.s, word):
            if c1 == c2: ans += 1
        return ans


class Solution:

    def findSecretWord(self, words: List[str], master: 'Master') -> None:

        @cache
        def match(s1, s2):
            return sum([1 for c1, c2 in zip(s1, s2) if c1 == c2])

        while words:
            t = []
            wf, cv = '', -10**10  # 与其他匹配最多的单词
            for i in range(len(words)):
                ss = sum([match(words[i], words[j]) for j in range(len(words))])
                if cv < ss:
                    cv = ss
                    wf = words[i]
            v = master.guess(wf)
            if v == 6: return
            for w in words:
                if wf == w: continue
                c = match(w, wf)
                if v == 0:
                    if c == v: t.append(w)
                else:
                    if c >= v: t.append(w)
            words = t

    def func(self, secret, words, allowedGuesses):
        master = Master(words, secret)
        self.findSecretWord(words, master)
        # print('====>', master.cnt)
        if master.cnt <= allowedGuesses:
            return 'You guessed the secret word correctly.'
        return "Either you took too many guesses, or you did not find the secret word."


# @lc code=end

if __name__ == '__main__':
    # You guessed the secret word correctly.
    print(Solution().func("vftnkr", [
        "mjpsce", "giwiyk", "slbnia", "pullbr", "ezvczd", "dwkrmt", "qgzebh", "wvhhlm", "kqbmny", "zpvrkz", "pdwxvy", "gilywa", "gmrrdc", "vvqvla", "rmjirt", "qmvykq", "mhbmuq", "unplzn", "qkcied",
        "eignxg", "fbfgng", "xpizga", "twubzr", "nnfaxr", "skknhe", "twautl", "nglrst", "mibyks", "qrbmpx", "ukgjkq", "mhxxfb", "deggal", "bwpvsp", "uirtak", "tqkzfk", "hfzawa", "jahjgn", "mteyut",
        "jzbqbv", "ttddtf", "auuwgn", "untihn", "gbhnog", "zowaol", "feitjl", "omtiur", "kwdsgx", "tggcqq", "qachdn", "dixtat", "hcsvbw", "chduyy", "gpdtft", "bjxzky", "uvvvko", "jzcpiv", "gtyjau",
        "unsmok", "vfcmhc", "hvxnut", "orlwku", "ejllrv", "jbrskt", "xnxxdi", "rfreiv", "njbvwj", "pkydxy", "jksiwj", "iaembk", "pyqdip", "exkykx", "uxgecc", "khzqgy", "dehkbu", "ahplng", "jomiik",
        "nmcsfe", "bclcbp", "xfiefi", "soiwde", "tcjkjp", "wervlz", "dcthgv", "hwwghe", "hdlkll", "dpzoxb", "mpiviy", "cprcwo", "molttv", "dwjtdp", "qiilsr", "dbnaxs", "dbozaw", "webcyp", "vftnkr",
        "iurlzf", "giqcfc", "pcghoi", "zupyzn", "xckegy"
    ], 12))
    # You guessed the secret word correctly.
    print(Solution().func("ccoyyo", [
        "wichbx", "oahwep", "tpulot", "eqznzs", "vvmplb", "eywinm", "dqefpt", "kmjmxr", "ihkovg", "trbzyb", "xqulhc", "bcsbfw", "rwzslk", "abpjhw", "mpubps", "viyzbc", "kodlta", "ckfzjh", "phuepp",
        "rokoro", "nxcwmo", "awvqlr", "uooeon", "hhfuzz", "sajxgr", "oxgaix", "fnugyu", "lkxwru", "mhtrvb", "xxonmg", "tqxlbr", "euxtzg", "tjwvad", "uslult", "rtjosi", "hsygda", "vyuica", "mbnagm",
        "uinqur", "pikenp", "szgupv", "qpxmsw", "vunxdn", "jahhfn", "kmbeok", "biywow", "yvgwho", "hwzodo", "loffxk", "xavzqd", "vwzpfe", "uairjw", "itufkt", "kaklud", "jjinfa", "kqbttl", "zocgux",
        "ucwjig", "meesxb", "uysfyc", "kdfvtw", "vizxrv", "rpbdjh", "wynohw", "lhqxvx", "kaadty", "dxxwut", "vjtskm", "yrdswc", "byzjxm", "jeomdc", "saevda", "himevi", "ydltnu", "wrrpoc", "khuopg",
        "ooxarg", "vcvfry", "thaawc", "bssybb", "ccoyyo", "ajcwbj", "arwfnl", "nafmtm", "xoaumd", "vbejda", "kaefne", "swcrkh", "reeyhj", "vmcwaf", "chxitv", "qkwjna", "vklpkp", "xfnayl", "ktgmfn",
        "xrmzzm", "fgtuki", "zcffuv", "srxuus", "pydgmq"
    ], 10))
    # You guessed the secret word correctly.
    print(Solution().func("acckzz", ["acckzz", "ccbazz", "eiowzz", "abcczz"], 10))
    # You guessed the secret word correctly.
    print(Solution().func("hamada", ["hamada", "khaled"], 10))
    # You guessed the secret word correctly.
    print(Solution().func("khaled", ["hamada", "khaled"], 10))
