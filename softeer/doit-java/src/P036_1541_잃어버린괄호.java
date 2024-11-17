import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

/**
 * 자료구조
 * numberSum: addExp를 통해 계산한 정수 배열
 * result: 결과값
 * <p>
 * 알고리즘
 * 1. 마이너스 기준으로 split
 * 2. split 한 문자열들을 + 로 split 해서 모두 더하기
 * 3. 더한 값들을 처음부터 모두 빼기
 * 4. 결과값
 */

public class P036_1541_잃어버린괄호 {
    List<Integer> numberSum = new ArrayList<>();
    int result = 0;

    public void answer() throws IOException {
        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), "-");
        // split 한 문자열을 모두 더하기
        while (st.hasMoreTokens()) {
            String addExp = st.nextToken();
            int sum = Arrays.stream(addExp.split("\\+")).mapToInt(Integer::parseInt).sum();
            numberSum.add(sum);
        }
        // 더한 값들을 처음부터 모두 빼기
        result = numberSum.get(0);
        for (int i = 1; i < numberSum.size(); i++) {
            result -= numberSum.get(i);
        }
        System.out.println(result);
    }

    public static void main(String[] args) throws IOException {
        new P036_1541_잃어버린괄호().answer();
    }
}
