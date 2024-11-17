import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P026_1260_DFSBFS {
    private int N;
    private int M;
    private int V;
    private List<List<Integer>> graph;
    private boolean[] dVisited;
    private int[] bVisited;
    private StringBuilder sb = new StringBuilder();

    public void answer() throws IOException {
        // 1. 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());
        dVisited = new boolean[N + 1];
        bVisited = new int[N + 1];
        graph = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());
            graph.get(node1).add(node2);
            graph.get(node2).add(node1);
        }
        // 2. 번호 순으로 정렬
        for (List<Integer> list : graph) {
            Collections.sort(list);
        }
        // 3. DFS
        dfs(V);
        sb.append("\n");
        // 4. BFS
        bfs(V);
        // 5. 출력
        System.out.println(sb);
    }

    private void dfs(int node) {
        dVisited[node] = true;
        sb.append(node).append(" ");
        for (Integer adjNode : graph.get(node)) {
            if (!dVisited[adjNode]) {
                dfs(adjNode);
            }
        }
    }

    private void bfs(int node) {
        Queue<Integer> queue = new LinkedList<>();
        int depth = 0;

        bVisited[node] = ++depth;
        sb.append(node).append(" ");
        queue.add(node);

        while (!queue.isEmpty()) {
            Integer now = queue.poll();
            depth++;
            for (Integer adjNode : graph.get(now)) {
                if (bVisited[adjNode] == 0) {
                    bVisited[adjNode] = depth;
                    sb.append(adjNode).append(" ");
                    queue.add(adjNode);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        new P026_1260_DFSBFS().answer();
    }
}
