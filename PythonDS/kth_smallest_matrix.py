#problem link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/submissions/
#problem statement: kth smallest element in sorted matrix using heap

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n= len(matrix)
        if(k<= n):
            matrix= matrix[:k][:k]
        q= []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(q, matrix[i][j])
        last= heapq.nsmallest(k, q)[-1]
        return last