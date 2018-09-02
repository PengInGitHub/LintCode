/**
 * Definition for ListNode
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

public class Solution {
    /**
     * @param head: a ListNode
     * @param val: An integer
     * @return: a ListNode
     */
    public ListNode removeElementsVersion1(ListNode head, int val) {
        // write your code here
        
        if(head==null)return head;
        
        //use two pointers
        ListNode pre = head;
        ListNode cur = head.next;
        //          1->2->3->3->4->5->3
        //pre       ->current 
        //          1->2->4->5
        while(cur != null){
            //remove
            if(cur.val==val){
                pre.next = cur.next;
            }else{
                pre = cur;
            }
            cur = cur.next;
        }
        if (head.val == val){
            return head.next;
        }
        return head;
    }
    public ListNode removeElements(ListNode head, int val) {
        // write your code here
        //head needs a pre node
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        //now head has a made-up starting node
        head = dummy;
        //head.next is the original head
        while(head.next != null ){
            if(head.next.val==val){
                //remove
                head.next=head.next.next;
            }else{
                head = head.next;
            }
        }
        return dummy.next;
    }    
}































