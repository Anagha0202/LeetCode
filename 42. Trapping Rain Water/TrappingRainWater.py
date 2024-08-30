class Solution:
    def trap(self, height: List[int]) -> int:
        # Two Pointer
        # Space optimized
        # t: O(n)
        # s: O(1)
        # Using 2 pointer, left_max stores max height seen on left side until current position, right_max stores max height on right until current position. Since we consider the minimum of left_max and right_max, at any point if one is lesser than other, that height defines the max water level possible. 
        left_ptr, right_ptr = 0, len(height)-1
        left_max, right_max = height[left_ptr], height[right_ptr]
        rain_water = 0
        while left_ptr<right_ptr:
            if right_max<left_max:
                right_ptr -= 1
                right_max = max(right_max, height[right_ptr])
                water_level = right_max - height[right_ptr]
                rain_water += water_level if water_level>0 else 0

            else:
                left_ptr += 1
                left_max = max(left_max, height[left_ptr])
                water_level = left_max - height[left_ptr]
                rain_water += water_level if water_level>0 else 0
        
        return rain_water

        # DP - max_left and max_right saves the pre-computed values
        # t: O(n)
        # s: O(n)
        # for each position, find highest on left and right, min(left,right)-current height gives the water thta can be stored at current position

        max_left, max_left_ht = [], 0 # max ht on left side of leftmost will always be 0. Similarly for right
        # max left height
        for index in range(len(height)):
            max_left.append(max_left_ht)
            max_left_ht = max(max_left_ht, height[index])
        
        max_right, max_right_ht = [], 0
        for index in range(len(height)-1, -1, -1):
            max_right.append(max_right_ht)
            max_right_ht = max(max_right_ht, height[index])
        max_right = max_right[::-1]
        
        # print(height)
        # print(max_left)
        # print(max_right)

        rain_water = 0
        for index, ht in enumerate(height):
            water_level = min(max_left[index],max_right[index]) - ht
            rain_water += water_level if water_level>0 else 0
        
        return rain_water