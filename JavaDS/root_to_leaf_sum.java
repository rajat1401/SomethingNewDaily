//problem link: https://leetcode.com/problems/sum-root-to-leaf-numbers/submissions/
//problem statement: find sum of all root-to-leaf numbers in a tree

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
    
    public static int sum= 0;
    
    public void addSum(TreeNode root, String s){
        s= s + Integer.toString(root.val);
        if(root.left== null && root.right== null){
            sum+= Integer.valueOf(s);
        }
        if(root.left!= null){
            addSum(root.left,s);
        }
        if(root.right!= null){
            addSum(root.right, s);
        }
    }
    
    public int sumNumbers(TreeNode root) {
        String s= "";
        addSum(root, s);
        int tmp= sum;
        sum= 0;
        return tmp;
    }
}