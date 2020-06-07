from typing import List
import collections


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if beginWord == endWord:
            return [beginWord]
        wordId = {}
        idWord = []
        for i in range(len(wordList)):
            wordId[wordList[i]] = i
            # print(i)
        idWord = wordList + [beginWord]
        wordId[beginWord] = i + 1
        if not endWord in wordId:
            return []
        # print(wordId)
        # print(idWord)
        # return 1
        neighbor = collections.defaultdict(set)
        length = len(beginWord)
        for w1 in idWord:
            # neighbor[w1] = set()
            for w2 in idWord:
                if wordId[w1] in neighbor[wordId[w2]]:
                    neighbor[wordId[w1]].add(wordId[w2])
                    continue
                diff = 0
                for a, b in zip(w1, w2):
                    if a != b:
                        diff += 1
                        if diff > 1:
                            break
                if diff == 1:
                    neighbor[wordId[w1]].add(wordId[w2])
        # print(neighbor)
        # print(1)
        self.ans = []
        # visited = set()
        pre = collections.deque([[wordId[beginWord]]])
        post = collections.deque([[wordId[endWord]]])
        pre_visited = {wordId[beginWord]}
        post_visited = {wordId[endWord]}
        pre_cur_visited = collections.defaultdict(list)
        pre_cur_visited[wordId[beginWord]].append(0)
        post_cur_visited = collections.defaultdict(list)
        post_cur_visited[wordId[endWord]].append(0)
        while pre and post:
            if len(pre) > len(post):
                pre, post = post, pre
                pre_visited, post_visited = post_visited, pre_visited
                pre_cur_visited, post_cur_visited = post_cur_visited, pre_cur_visited
            size = len(pre)
            pre_cur_visited = collections.defaultdict(list)
            flag = False
            idx = 0
            for i in range(size):
                seq = pre.pop()
                if seq[-1] in post_cur_visited:
                    for idx in post_cur_visited[seq[-1]]:
                        idx = len(post) - idx - 1
                        tmp = seq + post[idx][-2::-1] if seq[0] == wordId[beginWord] else post[idx] + seq[-2::-1]
                        # print(seq, post[idx], post_cur_visited, post, pre)
                        # print(len(seq), len(post[idx]), i)
                        self.ans.append(tmp)
                        flag = True
                if flag:
                    # if i == size - 1:
                    #     print('pre:', pre)
                    #     print(self.ans)
                    continue
                   
                
                for id in neighbor[seq[-1]]:
                    if not id in pre_visited:
                        pre_cur_visited[id].append(idx)
                        pre.appendleft(seq+[id])
                        idx += 1
            if flag:
                break
            pre_visited.update(pre_cur_visited.keys())

        for seq in self.ans:
            for i in range(len(seq)):
                seq[i] = idWord[seq[i]]
            # print(len(seq))
        return self.ans

if __name__ == "__main__":
    s = Solution()
    beginWord = "cet"
    endWord = "ism"
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    # wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
    # wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
    print(s.findLadders(beginWord, endWord, wordList))


