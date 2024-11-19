package programmers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

/**
 * 시간 덧셈 함수 필요
 * <p>
 * 자료구조
 * List<Job> jobs: 작업 중인 것 리스트
 * String[] complete: 끝난 작업 순서대로 이름 저장
 * Queue<Job> preempted: 중단된 작업 리스트
 * Time cur : 진행 시간
 * <p>
 * 알고리즘
 * 1. Job 배열 생성
 * 2. startHour 오름차순 정렬
 * 3. 작업 선택 (새작업 or preempted)
 * 3. 다음 작업 시작 시간과 비교, 다 끝낼 수 있으면 끝내기, 못끝내면 작업 하고 preempted에 보관
 */

class Time {
    public int hour;
    public int min;

    public Time(int hour, int min) {
        this.hour = hour;
        this.min = min;
    }

    public int diff(Time smallTime) {
        int diff = 0;
        if (hour > smallTime.hour) {
            diff += 60 * (hour - smallTime.hour);
        }
        diff += min - smallTime.min;
        return diff;
    }
}

class Job {
    public String name;
    public Time start;
    public int playTime;

    public Job(String name, String hour, String min, String playTime) {
        this.name = name;
        this.start = new Time(Integer.parseInt(hour), Integer.parseInt(min));
        this.playTime = Integer.parseInt(playTime);
    }
}

public class LV2_176962 {
    private List<Job> jobs = new ArrayList<>();
    private List<String> completed = new ArrayList<>();
    private Stack<Job> preempted = new Stack<>();

    public String[] solution(String[][] plans) {
        // Job 배열 생성
        for (String[] job : plans) {
            jobs.add(new Job(job[0],
                    job[1].substring(0, 2),
                    job[1].substring(3),
                    job[2]));
        }
        // startHour 오름차순 정렬
        jobs.sort((job1, job2) -> {
            if (job1.start.hour == job2.start.hour) {
                return Integer.compare(job1.start.min, job2.start.min);
            }
            return Integer.compare(job1.start.hour, job2.start.hour);
        });

        // 반복해서 선택 -> jobs에서 하나씩 꺼내서 판단
        // 모든 작업은 본인 시작시간~다음시작시간만큼 여유 있음
        // 여유시간 >= 작업시간 -> 작업 끝내고 남는 시간에 preemptive job
        // 여유시간 < 작업시간 -> 작업을 못끝내고 preemption
        for (int i = 0; i < jobs.size() - 1; i++) {
            Job curJob = jobs.get(i);
            Job nextJob = jobs.get(i + 1);
            Time curStartTime = curJob.start;
            Time nextStartTime = nextJob.start;
            int diff = nextStartTime.diff(curStartTime);
            if (diff >= curJob.playTime) { // curJob 작업 완료
                completed.add(curJob.name);
                runPreemptive(diff - curJob.playTime); // 남은 시간만큼 preemptive job
                continue;
            }
            // diff < curJob.playTime : 시간 부족
            curJob.playTime -= diff;
            preempted.add(curJob);
        }
        // 마지막 작업이라면, 자기 먼저 하고 나머지 preemptive job 시행
        completed.add(jobs.get(jobs.size() - 1).name); // 마지막 작업 수행
        runAllPreemptive(); // 나머지 preemptive 다 실행

        return completed.toArray(String[]::new);
    }

    private void runAllPreemptive() {
        while (!preempted.isEmpty()) {
            Job job = preempted.pop();
            completed.add(job.name);
        }
    }

    private void runPreemptive(int min) {
        while (min > 0) {
            if (preempted.isEmpty()) {
                return;
            }
            Job job = preempted.pop();
            if (job.playTime == min) {
                completed.add(job.name);
                return;
            }
            if (job.playTime > min) { // 다 시행 못함
                job.playTime -= min;
                preempted.add(job);
                return;
            }

            min -= job.playTime;   // 이 작업 끝내고 다음 작업도 시행
            completed.add(job.name);
        }
    }

    public static void main(String[] args) {
        String[][] plans = {{"korean", "11:40", "30"},
                {"english", "12:10", "20"},
                {"math", "12:30", "40"}};
        System.out.println(Arrays.toString(new LV2_176962().solution(plans)));
    }
}
