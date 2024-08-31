class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # t: O(n)
        # s: O(n)
        if len(cards)==1:
            return -1
        
        card_index = {}
        min_picks = math.inf
        for right,card in enumerate(cards):
            if card in card_index:
                left = card_index[card]
                min_picks = min(min_picks, right-left+1)
            card_index[card] = right
        return min_picks if min_picks!=math.inf else -1