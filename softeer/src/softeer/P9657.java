package softeer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P9657 {
    private int n;
    private int m;
    private int[][] grid;
    private int l1, r1, l2, r2; // 1씩 빼서 저장
    private int[] rowCount; // 각 행의 환경파괴범 수 (크기 n)

    public void solution() throws IOException {
        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        grid = new int[n][m];
        rowCount = new int[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        st = new StringTokenizer(br.readLine());
        l1 = Integer.parseInt(st.nextToken()) - 1;
        r1 = Integer.parseInt(st.nextToken()) - 1;
        st = new StringTokenizer(br.readLine());
        l2 = Integer.parseInt(st.nextToken()) - 1;
        r2 = Integer.parseInt(st.nextToken()) - 1;

        // 각 행의 1을 다 더하기
        for (int i = 0; i < n; i++) {
            rowCount[i] = Arrays.stream(grid[i]).sum();
        }

        // 나무 공격 만큼 빼기
        for (int i = l1; i <= r1; i++) {
            if (rowCount[i] != 0) {
                rowCount[i] -= 1;
            }
        }
        for (int i = l2; i <= r2; i++) {
            if (rowCount[i] != 0) {
                rowCount[i] -= 1;
            }
        }

        // 결과값 출력
        System.out.println(Arrays.stream(rowCount).sum());
    }

    public static void main(String[] args) throws IOException {
        new P9657().solution();
    }
}
