class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Given array 1 2 3 4 5 6 1 and k=3
        # Combo 1:            k k k    window_sum = [k]+[k]+[k]
        # Combo 2:    k       i k k    add [k] from front and remove [i]
        # Combo 3:    k k         k
        # Combo 4:    k k k 

        # Given array 1 2 3 4 5 6 1 and k=4
        # Combo 1:    k k k k
        # Combo 2:    k k k       k
        # Combo 3:    k k       k k
        # Combo 4:    k       k k k
        # Combo 5:          k k k k
        def score_helper(cards, k):
            window_sum = sum([cards[x] for x in range(len(cards)-1, len(cards)-k-1, -1)])
            max_sum = window_sum
            right = k

            for left in range(0, k):
                window_sum = window_sum + cards[left] - cards[len(cards)-right]
                right-=1
                max_sum = max(max_sum, window_sum)

            return max_sum
            


        # all combinations
        def brute_force(cards, left, right, k):
            if k==0:
                return 0
            
            if left>right:
                return -1
            
            leftsum = cards[left] + dfs(cards, left+1, right, k-1)
            rightsum = cards[right] + dfs(cards, left, right-1, k-1)

            total_sum = max(leftsum, rightsum)
            return total_sum
        
        # return dfs(cardPoints, 0, len(cardPoints)-1, k)

        return score_helper(cardPoints, k)