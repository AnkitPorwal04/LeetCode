class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        Integer[][] dp = new Integer[201][201];
        return helper(triangle, 0, 0, dp);
    }

    private int helper(List<List<Integer>> triangle, int rowIndex, int cRowIndex, Integer[][] dp) {
        if (rowIndex == triangle.size()) {
            return 0;
        }

        if (dp[rowIndex][cRowIndex] != null) {
            return dp[rowIndex][cRowIndex];
        }

        int result = triangle.get(rowIndex).get(cRowIndex) + 
        Math.min(helper(triangle, rowIndex + 1, cRowIndex, dp), helper(triangle, rowIndex + 1, cRowIndex + 1, dp));

        dp[rowIndex][cRowIndex] = result;

        return dp[rowIndex][cRowIndex];
    }
}
