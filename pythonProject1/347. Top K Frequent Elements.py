def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    for n in nums:
        count[n] = count.get(n, 0) + 1
    print("count", count)
    for n, c in count.items():
        freq[c].append(n)
    print("freq",freq)
    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
        print("res",res)
s=topKFrequent([1,1,1,1,1],1)
print(s)
