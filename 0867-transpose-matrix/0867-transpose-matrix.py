class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ans=[]
        for j in range(len(matrix[0])):
            row=[]
            for i in range(len(matrix)):
                row.append(matrix[i][j])
            ans.append(row)
        return ans