class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # t: O(n)
        # s: O(n)
        #if the totatl amount of gas is less than the total cost then its not possible to make a loop starting from any index
        if sum(gas)<sum(cost):
            return -1
        
        #We create a difference array which stores the difference between how much is added and how much is spent at each station
        diff = [gas[x]-cost[x] for x in range(len(gas))]

        #we add the diff to the total each time and if the total becomes negative then we know its not possible to travel ahead
        #We can check only till the end of the array no matter where we started because we know that a unique solution has to exist and if total is still positive till the end of the array then it has lesser chances of becoming negative while completing the loop
        total = 0
        startIndex = 0
        i = startIndex
        while i<len(diff):
            total+=diff[i]
            if total<0:
                total=0
                #we set startIndex to i+1 because if total has become negative then the net sum of all the previous index was smaller than then present one which made the total negative
                startIndex=i+1
            i+=1
        return startIndex