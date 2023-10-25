public class Main {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        int[] values = {1, 2, 4, 10, 69, 100, 10102};

        for (int value: values) {
           list.insert(value); 
        }

        list.printValues();
    }
}
