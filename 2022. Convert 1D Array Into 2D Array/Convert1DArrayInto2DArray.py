class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []

        # Approach 1:
        row = []
        result = []
        for ptr in range(0, len(original), n):
            row = original[ptr:ptr+n]
            result.append(row)

        return result

        # Approach 2:
        result= []
        row = []
        for ptr in range(len(original)):
            row.append(original[ptr])
            if len(row)==n:
                result.append(row)
                row = []
        return result
