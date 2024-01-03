class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Approach 2:
        # Create a count dict. Go through the dict until it has elements. Each iteration, create a new row in the final matrix and reduce the count of each element in the dict by 1 and add the element to the final matrix

        counts = dict(collections.Counter(nums))
        matrix = []
        counter = 0

        while counter<len(nums):
            temp = []
            for key, val in counts.items():
                if val>0:
                    temp.append(key)
                    counts[key] -= 1
            if temp:
                matrix.append(temp)
            counter+=1
        
        # print(matrix)
        return matrix

        # Approach 1:
        # if every element is duplicate, then will require length of nums number of rows in final matrix so start with that. When a duplicate element is found, increment the value in the dict so that the value of the element in the dict tells us the row number it should be inserted into.

        matrix = [[] for _ in range(len(nums))]
        # print(matrix)
        seen = {}

        for n in nums:
            if n in seen:
                matrix[seen[n]].append(n)
                seen[n]+=1
            else:
                matrix[0].append(n)
                seen[n]=1
        # print(matrix)
        new_matrix = list(filter(None, matrix))
        # print(new_matrix)
        return new_matrix
        