package doit;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

/**
 * 자료구조
 * n : 데이터 개수
 * l : 최소값을 구하는 범위
 * Deque<doit.Node> deque : 데이터를 담을 덱 자료구조
 * doit.Node: index와 value를 가지는 클래스
 */

/**
 * 알고리즘
 * for(n만큼 반복)
 * now : 현재 데이터 값
 * 1. 덱의 뒤에서부터 now보다 큰 값은 제거하기 (최소값이 될 수 없는 값)
 * 2. 덱의 마지막 위치에 now값 저장하기
 * 3. 덱의 앞에서 L의 범위를 벗어난 값 제거하기
 * 4. 덱의 첫번째 데이터 출력하기
 */

class Node {
    public int index;
    public int value;

    public Node(int index, int value) {
        this.index = index;
        this.value = value;
    }
}

public class P010_11003_최소값찾기 {
    private int N;
    private int L;
    private Deque<Node> deque = new LinkedList<>();

    public void answer() throws IOException {
        // 1. N, L 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());

        // 2. N번 입력 받으면서 for문 반복
        StringBuilder sb = new StringBuilder();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int now = Integer.parseInt(st.nextToken());

            // 덱의 뒤에서부터 now 보다 큰 값 제거
            while (!deque.isEmpty() && deque.getLast().value > now) {
                deque.removeLast();
            }
            // 덱의 마지막 위치에 now 값 저장
            deque.addLast(new Node(i, now));
            // 덱의 앞에서 L 범위를 벗어난 값은 제거
            if (deque.getFirst().index <= i - L) {
                deque.removeFirst();
            }
            // 덱의 첫번째 데이터 출력
            sb.append(deque.getFirst().value).append(" ");
        }

        // 3. 출력
        System.out.println(sb);
        br.close();
    }

    public static void main(String[] args) throws IOException {
        new P010_11003_최소값찾기().answer();
    }
}
