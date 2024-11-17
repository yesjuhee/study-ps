import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 1. 입력 받아서 배열에 저장
 * 2. 배열 정렬
 * 3. 투포인터로 더한 값 확인
 */
class P008_1253_좋은수구하기 {
    private int n;
    private long[] arr;
    private int count = 0;

    public void answer() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 1. 입력
        n = Integer.parseInt(br.readLine());
        arr = new long[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        // 2. 입력 배열 정렬
        Arrays.sort(arr);

        // 3. 투포인터
        for (int k = 0; k < n; k++) {
            long target = arr[k];
            int i = 0;
            int j = n - 1;

            while (i < j) {
                if (i == k) {
                    i++;
                    continue;
                }
                if (j == k) {
                    j--;
                    continue;
                }

                if (arr[i] + arr[j] > target) {
                    j--;
                    continue;
                }
                if (arr[i] + arr[j] < target) {
                    i++;
                    continue;
                }

                count++; // arr[i] + arr[j] == target
                break;
            }
        }

        // 4. 출력
        System.out.println(count);
    }

    public static void main(String[] args) throws IOException {
        new P008_1253_좋은수구하기().answer();
    }
}
