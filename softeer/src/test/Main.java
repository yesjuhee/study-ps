package test;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

/**
 * 구: 영역의 개수, 영역의 크기, 오름차순 출력
 * DFS -> 인접 행렬 DFS
 * 행렬 자체를 visited로 사용
 * <p>
 * 자료구조
 * n: 그래프 크기
 * List<Integer> size : 계산한 사이즈를 저장할 배열
 * int count : 발견한 영역 개수
 * int size_count : 영역 크기 카운트
 * int[] dx, int[] dy : 이동 벡터
 * <p>
 * 알고리즘
 * 1. 그래프 입력 -> 2차원 배열로 저장
 * 2. 2중 for 문으로 DFS
 * 3. main에서는 개수 체크, DFS 돌 때 사이즈 체크
 * 4. 오름차순으로 정렬해서 결과 출력
 */

class Main {
    private int n;
    private int[][] graph;
    private int count;
    private int size_count;
    private List<Integer> size = new ArrayList<>();
    private int[] dx = {-1, 0, 1, 0}; // 북, 동, 남, 서
    private int[] dy = {0, 1, 0, -1};


    public void solution() throws Exception {
        // 그래프 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 전체 DFS
        count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 1) {
                    count++;
                    size_count = 0;
                    dfs(i, j);
                    size.add(size_count);
                }
            }
        }

        // 크기 정렬
        Collections.sort(size);

        // 출력
        StringBuilder sb = new StringBuilder();
        sb.append(count).append('\n');
        for (int size : size) {
            sb.append(size).append(' ');
        }
        System.out.println(sb);

        br.close();
    }

    private void dfs(int x, int y) {
        graph[x][y] = 0;
        size_count++;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
                continue;
            }
            if (graph[nx][ny] == 1) {
                graph[nx][ny] = 0;
                dfs(nx, ny);
            }
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}



