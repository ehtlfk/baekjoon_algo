import java.util.PriorityQueue;
import java.util.Arrays;

class string_test {
    public static void main(String args[]) {
        int[] answer = {};
        String[] operations = new String[] { "I 16", "D 1" };
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>();
        String insert = "I";
        String delete = "D";
        for (String o : operations) {
            String[] tmp = o.split(" ");
            System.out.println(tmp[0]);
            System.out.println(tmp[0] == "I");
            System.out.println("I".getClass());
            if (tmp[0] == "I") {
                minHeap.add(Integer.parseInt(tmp[1]));
                maxHeap.add(Integer.parseInt(tmp[1]));
                System.out.println(minHeap);
                System.out.println(maxHeap);
            } else if (tmp[1] == "1" && !maxHeap.isEmpty()) {
                maxHeap.poll();
            } else if (tmp[1] == "-1" && !minHeap.isEmpty()) {
                minHeap.poll();
            }
        }
        if (minHeap.isEmpty() && maxHeap.isEmpty()) {
            answer = new int[] { 0, 0 };
        } else {
            answer = new int[] { 7, 56 };
        }

        System.out.println(answer);
    }
}