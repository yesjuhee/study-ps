n = 5
build_frame = [[0,0,0,1],[0,1,0,1],[0,2,0,1],[0,1,1,1]]
result = []

# frame 하나씩 확인
for frame in build_frame:
    x = frame[0]
    y = frame[1]
    a = frame[2]
    b = frame[3]

    # 설치 vs 삭제
    if b == 1:
        # 설치
        # 기둥 vs 보
        if a == 0:
            # 기둥
            # 바닥 위의 기둥인 경우 설치 가능
            if (y == 0):
                result.append([x, y, a])
            # 기둥 위에 설치하는 경우 설치 가능
            elif (result.count([x, y-1, 0]) == 1):
                result.append([x, y, a])  
            # 보의 한쪽 끝에 설치하는 경우 설치 가능
            elif (result.count([x, y, 1]) == 1 or result.count([x-1, y, 1]) == 1):
                result.append([x, y, a])
        elif a == 1:
            # 보
            # 한쪽 끝이 기둥 위인 경우 설치 가능
            if (result.count([x, y-1, 0])== 1 or result.count([x+1, y-1, 0]) == 1):
                result.append([x, y, a])
            # 양쪽 끝에 보가 있는 경우 설치 가능
            elif (result.count([x+1, y, 1])==1 and result.count([x-1, y, 1])==1):
                result.append([x, y, a])
    elif b == 0:
        # 삭제
        # 기둥 vs 보
        if a == 0:
            # 기둥
            # 위에 기둥이 있는 경우
            if (result.count([x, y+1, 0]) == 1):
                # 연결된 보가 업다면 삭제 불가
                if (result.count([x-1, y+1, 1]) == 0 and result.count([x, y+1, 1]) == 0):
                    continue
            # 위의 오른쪽에 보가 있는 경우
            if (result.count([x, y+1, 1]) == 1):
                # 반대쪽에 기둥이 없고, 양쪽 보가 연결되어있지 않으면 삭제 불가능
                if (result.count([x+1, y, 0])  == 0 and (result.count([x-1, y+1, 1]) == 0 or result.count([x+1, y+1, 1]) == 0)):
                    continue
            # 위의 왼쪽에 보가 있는 경우
            if (result.count([x-1, y+1, 1]) == 1):
                # 반대쪽에 기둥이 없고, 양쪽 보가 연결되어있지 않으면 삭제 불가능
                if (result.count([x-1, y, 0]) == 0 and (result.count([x-2, y+1, 1]) == 0 or result.count([x, y+1, 1]) == 0)):
                    continue
        elif a == 1:
            # 보
            # 왼쪽 위에 기둥이 있는 경우
            if (result.count([x, y, 0]) == 1):
                # 해당 기둥의 왼쪽에 보가 없으면서 아래에 기둥이 없다면 삭제 불가능
                if (result.count([x-1, y, 1]) == 0 and result.count([x, y-1, 0]) == 0):
                    continue
            # 오른쪽 위에 기둥이 있는 경우
            if (result.count([x+1, y, 0]) == 1):
                # 해당 기둥의 오른쪽에 보가 없으면서 아래에 기둥이 없다면 삭제 불가능
                if (result.count([x+1, y, 1]) == 0 and result.count([x+1, y-1, 0]) == 0):
                    continue
            # 오른쪽에 연결된 보가 있는 경우
            if (result.count([x+1, y, 1]) == 1):
                # 보에 연결된 기둥이 없다면 삭제 불가능
                if (result.count([x+1, y-1, 0]) == 0 and result.count([x+2, y-1, 0]) == 0):
                    continue
            # 왼쪽에 연결된 보가 있는 경우
            if (result.count([x-1, y, 1]) == 1):
                # 보에 연결된 기둥이 없다면 삭제 불가능
                if (result.count([x-1, y-1, 0]) == 0 and result.count([x, y-1, 0]) == 0):
                    continue
        # 모든 조건을 통과한 경우 삭제
        result.remove([x, y, a])
# 결과 정렬
result.sort()
print(result)