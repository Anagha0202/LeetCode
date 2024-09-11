class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Brute Force: Merge Sort + Binary Search
        t: O(nlogn + logn)
        s: O(n)
        
        Approach 1: Linear Search 
        Go through each element and check if key is found
        -works on non sorted array
        t: O(n)
        s: O(1)
        
        Approach 2: Binary Search 
        Idenitfy splited array 
        Run binary search on each individual half
        t: O(n+logn)
        s: O(1)

        Optimized Approach: Binary Seacrh 
        Binary Search over the whole array looking for target. 
        given mid, 
        if we are in left sorted part
        if [left] < [mid]
            if target > nums[mid] and target < [low]:
                low = mid+1
            else:
                high = mid-1
        if we are in right sorted part
            if target > nums[mid] and target < [high]:
                low = mid+1
            else:
                high = mid -1
        t: O(logn)
        s: O(1)                    

        """
        low, high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)//2

            if target==nums[mid]:
                return mid 

            #left sorted half
            if nums[low]<=nums[mid]:
                if target<nums[mid] and target>=nums[low]:
                    high = mid-1
                else:
                    low = mid+1
            
            #right sorted half
            else:
                if target>nums[mid] and target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1

        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1

        split = 0
        for index in range(len(nums)-1):
            if nums[index+1]<nums[index]:
                split = index+1
                break
        # print(split)
        
        # low = 8 high = 8
        # mid = 8
        def binary_search(low, high, nums, target):
            while low<=high:
                mid = (low+high)//2
                
                if nums[mid]==target:
                    return mid
                elif target<nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            return -1
        
        ans1 = binary_search(0, split-1, nums, target)
        ans2 = binary_search(split, len(nums)-1, nums, target)
        # print(ans1, ans2)
        if ans1!=-1: return ans1
        if ans2!=-1: return ans2
        return -1