class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        r1, r2 = 0, len(matrix)-1
        c1, c2 = 0, len(matrix[0])-1
        
        size = len(matrix)*len(matrix[0])
        result = []
        while r1 <= r2 and c1 <= c2 and len(result) <= size:
            for i in range(c1, c2+1):
                result.append(matrix[r1][i])
            r1+=1
            
            for i in range(r1, r2+1):
                result.append(matrix[i][c2])
            c2-=1
            
            if r1 <= r2:
                for i in range(c2, c1-1, -1):
                    result.append(matrix[r2][i])
                r2 -= 1
            
            if c1 <= c2:
                for i in range(r2, r1-1, -1):
                    result.append(matrix[i][c1])
                c1+=1
        return result