//problem link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/
//problem statement: sorted array to height balanced BST 


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
    
    public TreeNode getTree(int[] nums, int low, int high){
        if(low<= high){
            int mid= (low+high)/2;
            TreeNode root= new TreeNode(nums[mid]);
            root.left= getTree(nums, low, mid-1);
            root.right= getTree(nums, mid+1, high);
            return root;
        }
        return null;
        
    }
    
    public TreeNode sortedArrayToBST(int[] nums) {
        TreeNode root= getTree(nums, 0, nums.length-1);
        return root;
    }
}