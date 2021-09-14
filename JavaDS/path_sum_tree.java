//problem link: https://leetcode.com/problems/path-sum/submissions/
//problem statement: given a target, check if any path has that exact sum

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    public boolean checkAtNode(TreeNode root, int targetSum, int curSum){
        if(root.left== null && root.right== null && root.val+curSum== targetSum){
            return true;
        }
        boolean left= false;
        boolean right= false;
        if(root.left!= null){
            left= checkAtNode(root.left,targetSum,root.val+curSum);
        }
        if(root.right!= null){
            right= checkAtNode(root.right, targetSum, root.val+curSum);
        }
        return (left || right);
    }
    
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root== null){
            return false;
        }
        return checkAtNode(root, targetSum, 0);
    }
}