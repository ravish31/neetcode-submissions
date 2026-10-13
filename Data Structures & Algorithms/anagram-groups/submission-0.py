class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A=defaultdict(list)
        for s in strs:
            k=''.join(sorted(s))
            A[k].append(s)
        #print(type(A.values()))
        return list(A.values())
        