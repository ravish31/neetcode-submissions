class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A=defaultdict(list)
        for s in strs:
            k=[0]*26
            for a in s:
                k[ord(a)-ord('a')]+=1
            A[tuple(k)].append(s)
        #print(type(A.values()))
        return list(A.values())
        
        