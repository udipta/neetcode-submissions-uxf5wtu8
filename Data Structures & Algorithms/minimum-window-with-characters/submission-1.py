from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map1, map2 = defaultdict(int), Counter(t)
        mct, dmct = 0, len(t)
        i = j = -1
        ans = ""

        while True:
            flag1 = flag2 = False
            # Acquire 
            while i < len(s) - 1 and mct < dmct:
                i += 1
                char = s[i]
                map1[char]+=1
                if map1[char] <= map2[char]:
                    mct += 1
            
                flag1 = True

            # Release and collect answer
            while j < i and mct == dmct:
                pans = s[j+1:i+1]
                if ans == "" or len(ans) > len(pans):
                    ans = pans
                j += 1
                char = s[j]
                if map1[char] == 1:
                    del map1[char]
                else:
                    map1[char]-=1
                
                if map1[char] < map2[char]:
                    mct -= 1

                flag2 = True
            
            if not flag1 and not flag2:
                break
        return ans