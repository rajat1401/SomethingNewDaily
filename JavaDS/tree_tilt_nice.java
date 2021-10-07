//problem link: https://leetcode.com/problems/binary-tree-tilt/submissions/
//problem statement: Given the root of a binary tree, return the sum of every tree node's tilt.
/*
The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if there the node does not have a right child.
*/

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
class TreeTilt {
    
    public static int sum= 0;
    
    public static int tilt(TreeNode root){
        if(root== null){
            return 0;
        }
        int a= tilt(root.left);
        int b= tilt(root.right);
        sum+= Math.abs(a-b);
        return root.val + a + b;
    }
    
    public int findTilt(TreeNode root) {
        if(root== null){
            return 0;
        }
        int a= tilt(root.left);
        int b= tilt(root.right);
        int tmp= sum;
        sum= 0;
        return tmp + Math.abs(a-b);
        
    }
}