class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        holder = []
        for i,j in enumerate(nums):
            holder.append([i,j])
        holder.sort(key=lambda x:x[1])
        print(holder)
        i,j = 0,len(nums)-1
        while i<j:
            sum = holder[i][1]+holder[j][1]
            if sum==target:
                return [min(holder[i][0],holder[j][0]),max(holder[i][0],holder[j][0])]
            elif sum<target:
                i+=1
            else:
                j-=1
        return []