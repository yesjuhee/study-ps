# 문자열 압축

s = "a"
length = len(s)

# 문자열 길이가 1일 때 예외 처리
if length == 1:
    answers = [1]
else:
    answers = [10000] * (length // 2)

# 모든 단위의 경우의 수
for unit in range(1, length // 2 + 1):
    pointer = 0
    answer = 0

    # 단위로 나누어 떨어지지 않는 경우
    remainder = length % unit
    if remainder != 0:
        answer += remainder

    match_list = []
    piece = s[pointer : pointer + unit]
    match_list.append(piece) # 압축 대상 문자열을 리스트에 넣어준다.

    # 포인터를 옮겨가며 전체 압축 길이 구하기
    while pointer <= (length - unit):
        
        # piece와 일치하는 문자열이 있는지 확인하여 match_list에 추가하기
        next_piece = s[pointer + unit : (pointer + unit) + unit]
        
        # 일치한다면, match_list에 추가
        if (piece == next_piece):
            match_list.append(next_piece)
            pointer += unit
        # 일치하지 않는다면, 해당 match_list는 마감하고 정답에 추가
        else:
            if len(match_list) == 1:
                # 압축 되지 않은 경우
                answer += unit
            else:
                # 압축된 경우
                count = len(match_list)
                answer += len(str(count)) + unit
            match_list.clear()
            pointer += unit
            piece = s[pointer : pointer + unit]
            match_list.append(piece) # 압축 대상 문자열을 리스트에 넣어준다.
        
    # 해당 단위의 답을 기록한다.
    answers[unit - 1] = answer
    
print(min(answers))

'''
문제에서 요구하는 요구사항을 따라서 풀면 된다.
다만 과정이 복잡해서 중간에 실수를 하기 쉽기 때문에 테스트를 많이 진행해야 한다.
또한 주어진 테스트케이스 말고 예외적인 상황에서 발생하는 것들을 놓치기 쉽기 때문에 조심해야 한다. (문자열의 길이가 1인 경우)
'''