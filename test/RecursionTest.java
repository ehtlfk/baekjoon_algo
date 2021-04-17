class RecursionTest {
    public int solution(int[] numbers, int target) {
        int[] answer = new int[] { 0 };
        dfs(numbers.length, 0, 0, target, answer, numbers);
        return answer[0];
    }

    public void dfs(int n, int k, int total, int target, int[] answer, int[] numbers) {
        if (total == target) {
            answer[0]++;
            return;
        }
        if (n == k) {
            return;
        }
        dfs(n, k + 1, total + numbers[k], target, answer, numbers);
        dfs(n, k + 1, total - numbers[k], target, answer, numbers);

    }
}
