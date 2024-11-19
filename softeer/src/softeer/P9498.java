package softeer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 제대로된 수식
 * (1)
 * <p>
 * ((1)+(1))
 * (1)+(1)+(1)
 * <p>
 * 1. ( ) 사이에는 1을 넣는다
 * 2. ((, )) 는 넘어간다
 * 3. )( 사이에는 + 를 넣는다
 * <p>
 * ((1)+(1))+(1)
 * <p>
 * 스택? 아니면 그냥 문자열 처리 해도 될듯?
 */

public class P9498 {
    String input;
    String output;

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        input = br.readLine();
        String str1 = input.replaceAll("\\(\\)", "\\(1)");
        output = str1.replaceAll("\\)\\(", "\\)+(");
        System.out.println(output);
    }

    public static void main(String[] args) throws IOException {
        new P9498().solution();
    }
}
