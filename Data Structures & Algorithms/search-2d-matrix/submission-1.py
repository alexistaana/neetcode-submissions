class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # if it's O(log(m*n)) it is just a loop within a loop where matrix(m) into matrix(n)
        # just find the left and right within each matrix[m] and go through a binary search on each! ez pz
        for m in range(len(matrix)):
            left = 0
            print(len(matrix[m]))
            right = len(matrix[m]) - 1
            while left <= right:
                mid = (right + left) // 2
                
                if left > right:
                    break

                if (target > matrix[m][right]) or (target < matrix[m][left]): # goes out of matrix[m] if range is out of bounds from target
                    break

                if matrix[m][mid] == target:
                    return True

                if matrix[m][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

        return False 