class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        answer = 0
        n = len(nums)
        left = 0
        pairs = defaultdict(int)
        cnt = 0

        for i in range(n):
            x = nums[i]
            cnt += pairs[x]
            pairs[x] += 1

            while cnt >= k:
                answer += (n - i)
                # 윈도우 좁히기
                pairs[nums[left]] -= 1
                cnt -= pairs[nums[left]]
                left += 1
        
        return answer
                

        