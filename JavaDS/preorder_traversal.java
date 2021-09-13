//problem link: https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/
//problem statement: preorder traversal of a tree 

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
        list.add(root.val);
        addNodes(root.left, list);
        addNodes(root.right, list);
    }
    
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> list= new ArrayList<>();
        addNodes(root, list);
        return list;
    }
}