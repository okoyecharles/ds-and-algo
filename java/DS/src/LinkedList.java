public class LinkedList {
    ListNode head;
    int length = 0;

    public LinkedList() {
        head = null;
    }

    public void insert(int val) {
        ListNode curr = head;
        ListNode newNode = new ListNode(val);
        length++;

        if (curr == null) {
            head = newNode; 
            return;
        }

        while (curr.next != null) {
            curr = curr.next;
        }
        curr.next = newNode;
    }

    public void printValues() {
        ListNode curr = head;
        
        System.out.println("All list values : ");
        while (curr != null) {
            System.out.println(curr.val);
            curr = curr.next;
        } 
    }
}
