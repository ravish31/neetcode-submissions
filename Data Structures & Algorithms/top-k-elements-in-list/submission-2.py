class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        A={}
        for elem in nums:
            A[elem]=1+A.get(elem,0)
        #print(A.items())
        freq_list=list(A.items())
        freq_list.sort(key=lambda x:x[1],reverse=True)
        #print(freq_list)
        res=[]
        for i in range(k):
            res.append(freq_list[i][0])
        return res

