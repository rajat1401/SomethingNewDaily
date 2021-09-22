//problem link: https://leetcode.com/problems/invert-binary-tree/submissions/
//problem statement: invert a tree

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
    
    public void construct(TreeNode root, TreeNode inroot){
        if(root.left!= null){
            inroot.right= new TreeNode(root.left.val);
            construct(root.left,inroot.right);
        }
        if(root.right!= null){
            inroot.left= new TreeNode(root.right.val);
            construct(root.right, inroot.left);
        }
    }
    
    public TreeNode invertTree(TreeNode root) {
        if(root== null){
            return null;
        }
        TreeNode inroot= new TreeNode(root.val);
        construct(root,inroot);
        return inroot;
    }
}