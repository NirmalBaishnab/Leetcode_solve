class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dd = {}
        frequency = [[] for i in range(len(nums)+ 1)]

        for i in nums:
            dd[i] = 1 + dd.get(i, 0)
        
        for number, count in dd.items():
            frequency[count].append(number)

        res = []

        for i in range(len(frequency)-1, -1, -1):
            for n in frequency[i]:
                res.append(n)
            if len (res) == k:
                return  res
