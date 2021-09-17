//problem link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/
//problem statement: remove duplicate sin ll given its head

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head== null){
            return null;
        }
        ListNode first= new ListNode(head.val,head.next);
        while(head.next!= null && head.next.val== head.val){
            head= head.next;
        }
        first.next= deleteDuplicates(head.next);
        return first;
    }
}