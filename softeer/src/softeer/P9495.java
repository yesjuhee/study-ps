package softeer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.lang.Math.abs;
import static java.lang.Math.max;

/**
 * 최대 인기도 -> DP?
 * N명과 순서대로 만나야 함
 * <p>
 * 인기도 차이가 친화력보다 작아야지 +1
 * <p>
 * 구하고자 하는 것: N번 유명인을 만났을 때 최대값
 * 이 유명인을 만나느냐 만나지 않느냐의 차이
 * 이전 값에 영향을 받음
 * dp[i][0] = i번째를 만나지 않았을 때의 최대값 = max(d[i-1][0], max[d[i-1][1])
 * dp[i][1] = i번째를 만났을 때의 최대값 => 두 케이스를 계산해서 최대값
 * dp 0(만나지않음) 1(만남)
 * 0        0       0
 * 1        0       1
 * 2        1       1
 * 3        1       2
 */

public class P9495 {
    private int n;
    private int[][] dp;
    private int[][] celeb;

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        dp = new int[n + 1][2];
        celeb = new int[n + 1][2];
        for (int i = 1; i <= n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            celeb[i][0] = Integer.parseInt(st.nextToken());
            celeb[i][1] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= n; i++) {
            // i번쨰 방문 안함
//            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]);
            dp[i][0] = dp[i - 1][1];
            // i번째 방문 함
            if (abs(dp[i - 1][1] - celeb[i][0]) <= celeb[i][1]) { // +1 가능
                dp[i][1] = dp[i - 1][1] + 1;
                continue;
            }
            dp[i][1] = dp[i - 1][1];
        }

        System.out.println(max(dp[n][0], dp[n][1]));
    }

    public static void main(String[] args) throws IOException {
        new P9495().solution();
    }
}
