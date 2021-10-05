//problem link: https://leetcode.com/problems/diameter-of-binary-tree/submissions/
//problem statement: find diameter of binary tree

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
class Diameter {
    public static int maxd= 0;
    
    public int diameter(TreeNode root){
        if(root== null){
            return -1;
        }
        if(root.left== null && root.right== null){
            return 0;
        }
        int a= diameter(root.left);
        int b= diameter(root.right);
        int d= a+b+2;
        maxd= Math.max(maxd, d);
        return 1+Math.max(a,b);
    }
    
    public int diameterOfBinaryTree(TreeNode root) {
        diameter(root);
        int tmp= maxd;
        maxd= 0;
        return tmp;
    }
}