class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {} # store  number -> occurance

        # associate number with its count
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
                
        heap = list(counts.items())
        topk = heapq.nlargest(k,heap,key=lambda x:x[1])

        # grab k most
        result = []
        for l1,l2 in topk:
            result.append(l1)

        return result


'''
most frequent --> maxheap

1 pass for counts of num

store as a list of tuples
[(occurances,number),...]

can grab the top k most occurnace
'''