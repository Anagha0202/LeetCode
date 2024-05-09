class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        decrease = 0
        happiness.sort()
        total = 0
        for _ in range(k):
            temp = (happiness.pop() - decrease)
            total += temp if temp > 0 else 0
            decrease += 1
        return total