package softeer;

import java.io.IOException;

/**
 * N대의 자동차 생산
 * i번째 자동차, si단계의 생산 프로세스, 1/si 만큼 차지
 * 각 1초마다
 * 1. 모든 생산 프로세스들은 자신의 크기만큼 뒤로 움직인다. (1/si)
 * 단, 이동시에 다른 프로세스와 겹치면 이동x
 * 슬롯을 통과하여 0,1 밖으로 나오면 프로세스는 완료로 판단
 * => 1초를 통과했다면, 1/si * si 단계를 모두 거쳤다는 뜻
 * 2. 생산 프로세스는 슬롯에 할당하거나 할당하지 않을 수 있다.
 * 할당할 경우 0부터 차지한다. 겹치게 할당할 수는 없다.
 */

/**
 * 예시
 * 1 2 => 3초
 * 최소 공배수: 2
 * 2, 1
 * A A
 * 0 B
 * B 0
 * <p>
 * 1, 2, 3
 * 최소공배수:6, 슬롯크기:6
 * 6,3,2
 * A A A A A A
 * 0 0 0 B B B
 * B B B 0 C C
 * 0 0 C C 0 0
 * C C 0 0 0 0
 * 5초
 */

public class P9496 {
    public void solution() throws IOException {
    }

    public static void main(String[] args) throws IOException {
    }
}
