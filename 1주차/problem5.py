def solution(stones, k): 
    end= max(stones) # 징검다리의 시작점과 끝점 정의
    start = 0
    answer = 0
    while (start<=end): #징검다리의 시작점과 끝점이 만날때까지 반복
        count=0
        maxnum=0
        mid=(start+end)//2
        for x in stones: # 징검다리 수 - mid 가 0 미만의 수인 경우의 연속 최대 수를 구함
            if x - mid <= 0:
                count+=1
                if count > maxnum:
                    maxnum = count
            else:
                count = 0
        if maxnum < k:        # 연속된 0이하의 수 최대값이 k ㅣ미만이면 중간값 +1 의 값으로 설정
            start = mid +1 # 스타트 값을 합쳐질 때까지 반복하고 mid 값일때 경우를 계산한 것이므로
        else:
            end = mid -1
            answer = mid #k 값 이상이면 정답값 정의한다
    return answer
