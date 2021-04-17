import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.ArrayList;

// 위상정렬 문제 가장 마지막에 방문하는 공항부터 answer에 추가됨, 결국 문자열 순으로 방문해도 가장 마지막, 꼬리부분부터 answer에 저장하게 됨,
class Solution {
    public String[] solution(String[][] tickets) {
        ArrayList<String> answer = new ArrayList<>();

        HashMap<String, PriorityQueue<String>> airports = new HashMap<>();
        for (String[] ticket : tickets) {
            if (!airports.containsKey(ticket[0])) {
                airports.put(ticket[0], new PriorityQueue<>());
            }
            airports.get(ticket[0]).add(ticket[1]);
        }
        dfs(airports, answer, "ICN");
        String[] ret = new String[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            ret[i] = answer.get(answer.size() - 1 - i);
        }
        return ret;
    }

    void dfs(HashMap<String, PriorityQueue<String>> airports, ArrayList<String> answer, String node) {

        if (airports.containsKey(node)) {
            while (!airports.get(node).isEmpty()) {
                String tmp = airports.get(node).peek();
                airports.get(node).poll();
                dfs(airports, answer, tmp);
            }
        }
        answer.add(node);

    }
}