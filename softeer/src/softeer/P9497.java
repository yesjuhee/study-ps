package softeer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * N*N 크기. 1~N수. N개의 구역
 * 각 행과 열에 겹치는 수 x
 * 같은 구역에 겹치는 수 x
 * <p>
 * DFS + 숫자로 구역 판단 + 2중 for문으로 반복
 */

public class P9497 {
    private int n;
    private int[][] graph;
    private int[][] visited; // 양의 정수로 방문 표시 -> 출력에도 사용
    int zoneNumber; // visited에 표시할 구역 번호
    private boolean[] numberUsed; // 한번의 DFS에서 N개의 숫자 사용 표시

    int[] dx = {1, -1, 0, 0}; // 상 하 좌 우
    int[] dy = {0, 0, -1, 1};

    public void solution() throws IOException {
        // 입력 및 초기화
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        visited = new int[n][n];
        numberUsed = new boolean[n + 1];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 2중 for문으로 전체 DFS
        zoneNumber = 1; // 초기값
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j] != 0) { // 이미 방문함
                    continue;
                }
                dfs(i, j);
                zoneNumber++; // 다음 번호
                numberUsed = new boolean[n + 1]; // 초기화
            }
        }

        // 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sb.append(visited[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);

        br.close();
    }

    private void dfs(int x, int y) {
        visited[x][y] = zoneNumber; // 방문 처리
        numberUsed[graph[x][y]] = true; // 숫자 사용 표시
        // 다음 노드 방문
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            // 범위 체크, 숫자 중복 체크, 방문 체크
            if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
                continue;
            }
            if (numberUsed[graph[nx][ny]]) {
                continue;
            }
            if (visited[nx][ny] != 0) {
                continue;
            }
            dfs(nx, ny);
        }
    }

    public static void main(String[] args) throws IOException {
        new P9497().solution();
    }
}
