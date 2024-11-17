import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * 자료구조
 * N : 정점의 개수
 * M : 간선의 개수
 * graph : 그래프의 간접리스트
 * visited : 방문 boolean 그래프
 * count : 연결 요소 개수 카운트
 * <p>
 * 알고리즘
 * 1. 전체 그래프 입력
 * 2. 각 노드에 대해 N번 DFS 시행, 만약 방문했다면 시행하지 않음
 * 3. 전체 시행 횟수만큼 count에 더해서 최종 출력
 */

public class P023_11724_연결요소의개수 {
    private int N;
    private int M;
    private List<List<Integer>> graph;
    private boolean[] visited;
    private int count = 0;

    public void dfs(int node) {
        visited[node] = true;
        for (Integer adjNode : graph.get(node)) {
            if (!visited[adjNode]) {
                dfs(adjNode);
            }
        }
    }

    public void answer() throws IOException {
        // 1. 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        visited = new boolean[N];
        graph = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken()) - 1;
            int node2 = Integer.parseInt(st.nextToken()) - 1;
            graph.get(node1).add(node2);
            graph.get(node2).add(node1);
        }

        // 2. 방문하지 않은 노드에 대해서 DFS 시행
        for (int node = 0; node < N; node++) {
            if (!visited[node]) {
                dfs(node);
                count++;
            }
        }

        // 3. 출력
        System.out.println(count);
    }

    public static void main(String[] args) throws IOException {
        new P023_11724_연결요소의개수().answer();
    }
}
