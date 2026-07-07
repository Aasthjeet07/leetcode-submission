from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        counts = Counter(nums)
        s = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        print(counts)

        for key,freq in s:
            ans.append(key)
            print(key)
            if len(ans) == k:
                break
        return ans

            
        