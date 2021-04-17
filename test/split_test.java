public class split_test {
    public static void main(String args[]) throws Exception {
        String[] input;
        input = "1 2 3 3 5 6 7".split(" ");
        // System.out.println(input[0].getClass());
        System.out.println(Integer.parseInt(input[0]) * 10);
    }
}
