//problem link: https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/
//problem statement: get inorder traversal of tree

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
    
    public void addNodes(TreeNode root, List<Integer> list){
        if(root== null){
            return;
        }
        addNodes(root.left, list);
        list.add(root.val);
        addNodes(root.right, list);
    }
    
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list= new ArrayList<>();
        addNodes(root, list);
        return list;
    }
}