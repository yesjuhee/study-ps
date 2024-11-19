package programmers;

import java.util.Arrays;

public class LV2_01_퍼즐게임챌린지 {
    public int solution(int[] diffs, int[] times, long limit) {
        int left = 1;
        int right = Arrays.stream(diffs).max().getAsInt();
        int mid = (left + right) / 2;
        while (left < right) {
            if (solve(diffs, times, limit, mid)) {
                // 풀린다 -> 작은 값으로 이동
                right = mid;
            } else {
                // 안풀린다 -> 큰 값으로 이동
                left = mid + 1;
            }
            mid = (right + left) / 2;
        }
        // left = right = mid 일 때 탈출
        return mid;
    }

    private boolean solve(int[] diffs, int[] times, long limit, int level) {
        // 풀 수 있냐 없냐의 여부는 앞의 문제부터 하나씩 해결을 했을 때, 총 시간이 limit를 넘지 않느냐 차이
        // 첫 번째 문제 반영
        long totalTime = times[0];
        int time_prev = times[0];
        for (int i = 1; i < diffs.length; i++) {
            int time_cur = times[i];
            if (diffs[i] <= level) {
                totalTime += time_cur;
                time_prev = time_cur;
                continue;
            }
            // diff > level
            totalTime += (long) (diffs[i] - level) * (time_cur + time_prev) + time_cur;
            time_prev = time_cur;
        }

        return totalTime <= limit;
    }
}
