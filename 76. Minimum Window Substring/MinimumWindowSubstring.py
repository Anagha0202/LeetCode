class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Take a window of characters from i to j 
        #     If need character is found:
        #         update have dict, 
        #         if count is exactly what is in need dict:
        #             update have count
        #     move j forward and repeat until substring is found. 
        #     store the indexes and length
        # Move i forward until have count < need count i.e window fails
        #     => then move j forward and repeat
        if len(s)<len(t):
            return ""
        
        needdict = collections.Counter(t)
        needcount = len(needdict)
        havedict = {x:0 for x in needdict.keys()}
        havecount = 0
        resi, resj, reslen = 0, 0, math.inf
        i, j = 0, 0
        
        while i<=j and j<len(s):
            # print("i={} j={} s[j]={}".format(i, j, s[j]))
            if s[j] in needdict:
                havedict[s[j]]+=1
                if havedict[s[j]] == needdict[s[j]]:
                    havecount+=1
            # print("havecount={} needcount={}".format(havecount, needcount))
            while havecount==needcount:
                print("newlen=", (j-i+1))
                if (j - i + 1) < reslen:
                    resi = i
                    resj = j
                    reslen = j-i+1
                    # print("Current result ={} resi={} resj={}".format(reslen, resi, resj))
                if s[i] in needdict:
                    havedict[s[i]]-=1
                    havecount = havecount-1 if havedict[s[i]]<needdict[s[i]] else havecount
                i+=1
                # print("Current i =", i)
            j+=1
        
        return s[resi:resj+1] if reslen!=math.inf else ""
